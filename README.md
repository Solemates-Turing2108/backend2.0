## Solemates - Backend Flask App

Not everyone requires two shoes. This app was inspired by a post of someone with one leg showing off their shoe collection and stating that luckily they had a friend who was missing an opposite leg, and was the same size shoe and had similar styles in footware. So we decided to create an app for people to find their Solemate. <br>
([FE deployed endpoint](https://solemateturing.herokuapp.com/)) <br>
([BE deployed endpoint](https://turingsolemates.herokuapp.com/))<br>
Once logged in, the user can browse shoes, filtered by size, side and style, and be connected to the seller via email if they find anything they like. Frontend Github repository can be found [here](https://github.com/Solemates-Turing2108/frontend2.0)   

#### What can I do on Solemates?
  - Create a user account
  - Post a shoes you want to sell or share
  - View available shoes
  - Search shoes by side, size and style
  - Get buyer's contact information for the shoes you are interested in.

#### Stack
- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) 	![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white) 	![CircleCI](https://img.shields.io/badge/circle%20ci-%23161616.svg?style=for-the-badge&logo=circleci&logoColor=white) ![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white) 
- pgAdmin4, SQLAlchemy, Pytest


# Readme Content
- [Local Setup](#local-setup)
- [API Endpoints](#api-endpoints)
- [Contributors](#contributors)

# Local Setup
- Versions
  - Python 3.9.10
  - Flask 2.0.2
- Fork and clone the repository
- `cd` into your local repo version and install all the libraries specified in requirements.txt
- This is not necessary, but if you want to be safe, create a virtual environment and activate it in the terminal:
  - `python3 -m venv .venv` (.venv is just the name of the virtual environment, so it can be anything you want)
  - `source .venv/bin/activate`
- Run your own development server. In the terminal, run:
  - `python3 app.py`
  - Your terminal will show you the url of your local server 
- Create a .env file on the same level as the app.py. Assign the url for the postgres database in the form of:
  - `URL = postgresql://(full url from heroku postgres config variables)`


# API Endpoints
Endpoint : https://turingsolemates.herokuapp.com/

  - **View all shoes**: 
    - Request: GET '/api/v1/shoes'
    - Response:
     ```
              {
              "shoes": [
                  {
                    "description": "comfortable shoes",
                    "id": 1,
                    "brand": "Nike",
                    "side": "right",
                    "size": 9,
                    "style": "sneakers",
                    "user_id": 1,
                    "photo_url": "some_url"
                  },
                  {
                    "description": "comfortable shoes",
                    "id": 2,
                    "brand": "Nike",
                    "side": "right",
                    "size": 9,
                    "style": "sneakers",      ,
                    "user_id": 2,
                    "photo_url": "some_url"
         
                  }
                ]
               }
      ```
 - **Search one shoe by id**: 
    - Request: GET '/api/v1/shoes/<id>'
    - Response:
     ```
                  {
                    "id": 1,
                    "brand": "Nike",
                    "side": "right",
                    "size": 9,
                    "style": "sneakers",
                    "description": "comfortable shoes",
                    "user_id": 1,
                    "photo_url": "some_url"
                  }
    ```
  
 - **Add a shoe**: 
    - Request: POST '/api/v1/shoes'
     - As a raw JSON body: 
      ```
                             {
                                  "side": "side",
                                  "style": "style",
                                  "size": size,
                                  "photo_url": "url",
                                  "description": "description",
                                  "brand": "brand",
                                  "user_id": user_id
                              }
      ```
    - Response:
       `The shoe "{id}" has been successfully created.`
  
  - **Delete a shoe**: 
    - Request: POST '/api/v1/shoes/<id>'
    - Response:
       `The shoe " + {id} + " has been deleted!`
  
  - **Filter by size, side and style **: 
    - Request: GET '/api/v1/shoes/search'
     - As a raw JSON body: 
     ```
                           {
                                "side": "side",
                                "style": "style",
                                "size": size
                            }
     ```
    - Response:
      `The shoe "{id}" has been successfully created.`
  
  
  - **Add a user**: 
    - Request: POST '/api/v1/users'
     - As a raw JSON body:
    ```
                             {
                                  "name": "name",
                                  "email": "email"
                              }
    ```
    - Response:
        ```
              {
              "shoes": [
                  {
                    "description": "comfortable shoes",
                    "id": 1,
                    "brand": "Nike",
                    "side": "right",
                    "size": 9,
                    "style": "sneakers",
                    "user_id": 1,
                    "photo_url": "some_url"
                  },
                  {
                    "description": "comfortable shoes",
                    "id": 2,
                    "brand": "Nike",
                    "side": "right",
                    "size": 9,
                    "style": "sneakers",      ,
                    "user_id": 2,
                    "photo_url": "some_url"
         
                  }
                ]
               }
      ```
  

# Contributors
- Matthew Kimball  |  [Github](https://github.com/mekimball)   |   [LinkedIn](https://www.linkedin.com/in/mekimba)
- Haewon Jeon      |  [Github](https://github.com/haewonito)   |   [LinkedIn](linkedin.com/in/haewonito)


