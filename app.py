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
from flask_mail import Mail, Message



#################################################
# Database Setup
#################################################

#make sure you have your own .env on your computer
#comment out when you plan to deploy from heroku

# uri = os.getenv('URI')


#uncomment line below when you want to deploy to heroku
uri = os.environ.get("URI")
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

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'haewon208@gmail.com'
app.config['MAIL_PASSWORD'] = email_password
# app.config['MAIL_DEBUG'] = True  #this and below wasn't there for https://mailtrap.io/blog/flask-email-sending/  if this is true, it will give you some error messages when it doesn't work
# app.config['DEBUG'] = True  #this and below wasn't there for https://mailtrap.io/blog/flask-email-sending/  if this is true, it will give you some error messages when it doesn't work
# app.config['TESTING'] = False #this one and the below together will make sure the emails aren't actually sent for testing
app.config['MAIL_DEFAULT_SENDER'] = 'haewon208@gmail.com'  #if you don't specify the sender, this will be sent
# or you can also add:
# app.config['MAIL_DEFAULT_SENDER'] = ('Haewon from the Solemates', 'anthony@prettyprinted.com')
app.config['MAIL_MAX_EMAILS'] = 10 #just for preventing accidents when you are testing. None by default
# app.config['MAIL_SUPPRESS_SEND'] = False #then if testing is true, the suppress_send is true too.
app.config['MAIL_ASCII_ATTACHMENTS'] = False #convert
# app.config['MAIL_SERVER']='smtp.gmail.com'   # location/address of your mail server   'localhost' if youa re running the server
# app.config['MAIL_PORT'] = 587  # port where the email is sent through your server. depends on your email provider  typically 25 or 465
# app.config['MAIL_USE_TLS'] = True # you probably need to play around with ssl and tls, switch it around with false and true and see which one works
# app.config['MAIL_USE_SSL'] = False
# app.config['MAIL_USERNAME'] = 'haewon208@gmail.com'
# app.config['MAIL_PASSWORD'] = 'Qwer1234_5Turing'
# # app.config['MAIL_DEBUG'] = True  #this and below wasn't there for https://mailtrap.io/blog/flask-email-sending/  if this is true, it will give you some error messages when it doesn't work
# # app.config['DEBUG'] = True  #this and below wasn't there for https://mailtrap.io/blog/flask-email-sending/  if this is true, it will give you some error messages when it doesn't work
# # app.config['TESTING'] = False #this one and the below together will make sure the emails aren't actually sent for testing
# app.config['MAIL_DEFAULT_SENDER'] = 'haewon208@gmail.com'  #if you don't specify the sender, this will be sent
# # or you can also add:
# # app.config['MAIL_DEFAULT_SENDER'] = ('Haewon from the Solemates', 'anthony@prettyprinted.com')
# app.config['MAIL_MAX_EMAILS'] = 10 #just for preventing accidents when you are testing. None by default
# # app.config['MAIL_SUPPRESS_SEND'] = False #then if testing is true, the suppress_send is true too.
# app.config['MAIL_ASCII_ATTACHMENTS'] = False #convert characters to ASCII for attachments (which has way less characters than unicode)

#instantiate flask mail
mail = Mail(app)



# create route that renders index.html template
# @app.route("/", methods=["GET","POST"])
# def home():
    # return render_template("index.html")

@app.route("/")
def index():
    return "Welcome to Solemates!"

#user3 has haewon208 and user4 has haewon201 email
#shoe22 has user4
#request needs { "buyer_id": 3}
# @app.route('/api/v1/shoes/<id>/email')
# def send_mail(id):
#     session = Session(engine)
#     shoe = session.query(ShoesObject).get(id)
#     seller_id = shoe.user_id
#     seller = session.query(UsersObject).get(seller_id)
#     seller_email = seller.email
#     buyder_id = request.json["buyer_id"]
#     buyer = session.query(UsersObject).get(buyer_id)
#     buyer_email = buyer.email
#     # msg = Message('Hey There', sender='email')  Hey there=title, we don't need sender because we configed it, then recipients
#     msg = Message('Hey There', recipients=[seller_email, buyer_email])
#     #or to add more recipient, you can also do:
#     #msg.add_recipient('more1@gmail.com')
#     #msg.add_recipient('more2@gmail.com')
#     # msg.body = 'This is v2 fourth test email from Haewon\'s app. You don\'t have to reply.'
#     msg.body = 'f"{buyer_email}" has expressed interest in the shoe f"{shoe.id}"! The seller\'s email address is f"{seller_email}".'
#     # you can also do: making it bold for fun.  If you do both, the html will be sent
#     # msg.html = '<b>This is a test email sent from Haewon\'s app. You don\'t have to reply.</b>'
#     mail.send(msg)
#     return "Email has been successfully been sent to the seller"

#make an endpoint for data you are using in charts. You will use JS to call this data in
#using d3.json("/api/data")
@app.route("/api/v1/shoes")
def data():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    #Query Database. Check SqlAlchemy documentation for how to query

    #Convert your query object into a list or dictionary format so it can
    # be jsonified

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

@app.route('/api/v1/shoes/search')
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

if __name__ == '__main__':
    #delete debug part
    app.run(debug=True)
