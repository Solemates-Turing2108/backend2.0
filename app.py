#IMPORT NECESSARY LIBRARIES
#import joblib  #for importing your machine learning model
from flask import Flask, render_template, request, jsonify, make_response
import pandas as pd


# SQLALCHEMY SETUP
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import psycopg2

#os allows you to call in environment variables
# we will set the remote environment variables in heroku
from dotenv import load_dotenv
import os

load_dotenv()

#email
# from flask_mail import Mail, Message

from flask_cors import CORS
app = Flask(__name__)
CORS(app)


#################################################
# Database Setup
#################################################

#make sure you have your own .env on your computer
#comment out when you plan to deploy from heroku

uri = os.getenv('URI')


#uncomment line below when you want to deploy to heroku
# uri = os.environ.get("URI")

email_password = os.environ.get("EMAIL_PASSWORD")

engine = create_engine(f'{uri}')


# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

#my table in pgadmin (postgres) is named envdata
ShoesObject = Base.classes.shoe
UsersObject = Base.classes.user

# create instance of Flask app
app = Flask(__name__)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.route("/")
def index():
    return "Welcome to Solemates!"

@app.route("/api/v1/shoes")
def data():

    session = Session(engine)

    SData = session.query(ShoesObject).all()
    myData = []

    for shoe in SData:

        fullSdata = {}

        fullSdata = {
            "id": shoe.id,
            "side": shoe.side,
            "style": shoe.style,
            "size": shoe.size,
            "photo_url": shoe.photo_url,
            "description": shoe.description,
            "brand":shoe.brand,
            "user_id":shoe.user_id
        }

        myData.append(fullSdata)

    return {"shoes": myData}
    session.close()

@app.route('/api/v1/shoes/<id>')
def get_shoe(id):
    session = Session(engine)
    shoe = session.query(ShoesObject).get(id)

    if shoe is None:
        return ("the shoe is not found")

    shoe_data = {
                    "id": shoe.id,
                    "side": shoe.side,
                    "style": shoe.style,
                    "size": shoe.size,
                    "photo_url": shoe.photo_url,
                    "description": shoe.description,
                    "brand": shoe.brand,
                    "user_id": shoe.user_id
                }
    return (shoe_data)
    session.close()

@app.route('/api/v1/shoes', methods=['POST'])
def add_shoe():
    session = Session(engine)

    shoe = ShoesObject(side=request.json["side"], brand=request.json["brand"], photo_url=request.json["photo_url"], style=request.json["style"], size=request.json["size"], description=request.json["description"], user_id=request.json["user_id"])

    session.add(shoe)
    session.commit()
    return  ("the shoe " + f"{shoe.id}" + " has been successfully created.")
    session.close()

@app.route('/api/v1/users', methods=['POST'])
def add_user():
    session = Session(engine)

    user = UsersObject(name=request.json["name"], email=request.json["email"])

    session.add(user)
    session.commit()
    return  ("the user " + f"{user.name}" + " has been successfully created.")
    session.close()

@app.route('/api/v1/shoes/<id>', methods=['DELETE'])
def delete_shoe(id):
    session = Session(engine)
    shoe = session.query(ShoesObject).get(id)

    if shoe is None:
        return ("the shoe is not found")

    session.delete(shoe)
    session.commit()
    return ("the shoe " + f"{shoe.id}" + " has been deleted!")
    session.close()



@app.route('/api/v1/users/<id>/shoes')
def get_user_shoes(id):

    session = Session(engine)

    shoes = session.query(ShoesObject).filter_by(user_id = id)
    myData = []

    for shoe in shoes:

        fullSdata = {}

        fullSdata = {
            "id": shoe.id,
            "side": shoe.side,
            "style": shoe.style,
            "size": shoe.size,
            "photo_url": shoe.photo_url,
            "description": shoe.description,
            "brand":shoe.brand,
            "user_id":shoe.user_id
        }

        myData.append(fullSdata)

    return {"shoes": myData}

    session.close()

@app.route('/api/v1/shoes/search', methods=['POST'])
def search_shoe():
    session = Session(engine)

    side_query = request.json["side"]
    style_query = request.json["style"]
    size_query = request.json["size"]

    filtered_shoes = session.query(ShoesObject).filter_by(side = side_query, style = style_query, size = size_query)
    myData = []

    for shoe in filtered_shoes:

        fullSdata = {}

        fullSdata = {
            "id": shoe.id,
            "side": shoe.side,
            "style": shoe.style,
            "size": shoe.size,
            "photo_url": shoe.photo_url,
            "description": shoe.description,
            "brand":shoe.brand,
            "user_id":shoe.user_id
        }

        myData.append(fullSdata)

    return {"shoes": myData}
    session.close()

@app.route('/api/v1/shoes/<id>/user')
def get_user_email(id):
    session = Session(engine)
    shoe = session.query(ShoesObject).get(id)

    if shoe is None:
        return ("the shoe is not found")

    user_id = shoe.user_id
    user = session.query(UsersObject).get(user_id)

    user_data = {
                    "user_email": user.email
                }

    return (user_data)
    session.close()

if __name__ == '__main__':
    #delete debug part
    app.run(debug=True)
