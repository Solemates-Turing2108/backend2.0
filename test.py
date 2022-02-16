import app
from app import ShoesObject, UsersObject
import pytest

from flask import Flask, render_template, request, jsonify, make_response
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

from flask_cors import CORS

test_app = Flask(__name__)
CORS(test_app)

#comment out when you plan to deploy from heroku
uri = os.getenv('URI')
#uncomment line below when you want to deploy to heroku
# uri = os.environ.get("URI")

email_password = os.environ.get("EMAIL_PASSWORD")
engine = create_engine(f'{uri}')

Base = automap_base()

Base.prepare(engine, reflect=True)

ShoesObject = Base.classes.shoe
UsersObject = Base.classes.user

# #
# # def test_example_postgres(postgresql):
# #     """Check main postgresql fixture."""
# #     cur = postgresql.cursor()
# #     cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
# #     postgresql.commit()
# #     cur.close()

def test_add_user():
    user = UsersObject(name="test", email="test@email.com")

    assert user.name == 'test'
    assert user.email == 'test@email.com'
    assert type(user) is UsersObject
#
# app.config['TESTING'] = True

@test_app.route("/")
def index():
    return "Welcome to Solemates!"

def test_home_page_get():
    with test_app.test_client() as test_client:

        response = test_client.get('/')
        assert response.status_code == 200
        assert b"Welcome to Solemates!" in response.data



@test_app.route("/api/v1/shoes")
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

def test_shoes_page_get():
    with test_app.test_client() as test_client:

        response = test_client.get('/api/v1/shoes')
        assert response.status_code == 200
        assert b"side" in response.data
        assert b"size" in response.data
        assert b"brand" in response.data
        assert b"description" in response.data
        # assert b"Welcome to Solemates!" in response.data


# @test_app.route('/api/v1/shoes', methods=['POST'])
# def add_shoe():
#     session = Session(engine)
#
#     shoe = ShoesObject(side=request.json["side"], brand=request.json["brand"], photo_url=request.json["photo_url"], style=request.json["style"], size=request.json["size"], description=request.json["description"], user_id=request.json["user_id"])
#
#     session.add(shoe)
#     session.commit()
#     return  ("the shoe " + " has been successfully created.")
#     session.close()
#
# def test_shoe_page_post():
#     with test_app.test_client() as test_client:
#         response = test_client.post('/api/v1/shoes')
#         assert response.status_code == 405


    # rv = c.post('/api/v1/shoes', json={
    #                                         "side": "left",
    #                                         "style": "boots",
    #                                         "size": 18,
    #                                         "photo_url": "url",
    #                                         "description": "cool shoes",
    #                                         "brand": "cool brand",
    #                                         "user_id": 4
    #                                     })
    # json_data = rv.get_json()
    # assert json_data == "the shoe has been successfully created."
    # # assert verify_token(email, json_data['token'])
