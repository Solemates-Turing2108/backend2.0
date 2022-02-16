from app import ShoesObject, UsersObject
import pytest

from flask import Flask, render_template, request, jsonify, make_response

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()


test_app = Flask(__name__)

uri = os.getenv('URI')

engine = create_engine(f'{uri}')
Base = automap_base()
Base.prepare(engine, reflect=True)

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

def test_example_postgres(postgresql):
    """Check main postgresql fixture."""
    cur = postgresql.cursor()
    cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
    postgresql.commit()
    cur.close()

def test_add_user():
    user = UsersObject(name="test", email="test@email.com")

    assert user.name == 'test'
    assert user.email == 'test@email.com'
    assert type(user) is UsersObject

def test_add_shoe():
    shoe = ShoesObject(side="left", style="sneaker", size=7, photo_url='test_url', description='this is a test', brand='test_brand', user_id=3)

    assert shoe.side == 'left'
    assert shoe.style == 'sneaker'
    assert shoe.size == 7
    assert shoe.photo_url == 'test_url'
    assert shoe.description == 'this is a test'
    assert shoe.brand == 'test_brand'
    assert shoe.user_id == 3
    assert type(shoe) is ShoesObject
