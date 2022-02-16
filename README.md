## Solemates - Backend Flask App

Many people need only one out of a pair of shoes that they buy. Solemates ([FE deployed endpoint](https://komodo-frontend.herokuapp.com)) ([BE deployed endpoint](https://turingsolemates.herokuapp.com/)) was created to connect people who have an extra shoe with those who need just one shoe. Once logged in, the user can browse shoes, filtered by size, side and style, and be connected to the seller via email if they find anything they like. Frontend Github repository can be found ([here](https://github.com/Solemates-Turing2108/frontend2.0))   

#### What can I do on Solemates?
  - Create a user account
  - Post a shoes you want to sell or share
  - Get an email alert when someone is interested in your shoe
  - View available shoes
  - Search shoes by side, size and style
  - Get buyer's contact information for the shoes you are interested in.

#### Stack
- Python, Flask, Pytest, PostgreSQL, pgAdmin4, SQLAlchemy, Heroku, CircleCI


# Readme Content
- [Local Setup](#local-setup)
- [External APIs](#external-apis)
- [Database Schema](#database-schema)
- [Contributors](#contributors)

# Local Setup.
- Versions
  - Python 3.9.10
  - Flask 2.0.2
- Fork and clone the repository
- `cd` in your local repo version and install all the libraries specified in requires.txt
- This is not necessary, but if you want to be safe, create a virtual environment and activate it in the terminal:
  - `python3 -m venv .venv` (.venv is just the name of the virtual environment, so it can be anything you want)
  - `source .venv/bin/activate`
- Run your own development server. In the terminal, run:
  - `python3 app.py`
  - Your terminal will show you the url of your local server 
- Create a .env file on the same level as the app.py. Assign the url for the postgres database in the form of:
  - `URL = postgresql://(full url from heroku postgres config variables)`
- We have also hidden the password of the gmail we used. Change the email address in app.py to something you can use and put its password in the .env file as:
  - `EMAIL_PASSWORD = your_password`


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
     - As a raw jason body: 
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
     - As a raw jason body: 
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
     - As a raw jason body:
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
  
  
  - **Send an email to the potential seller and buyer with each other's email**: 
    - Request: GET '/api/v1/shoes/<id>/email'
        As a raw jason body: 
        ```
           {
                "buyer_id": "buyer_id"
            }
        ```
     - Response:
      `Email has been successfully been sent to the seller`
  

# Contributors
- Matthew Kimball  |  [Github](https://github.com/mekimball)   |   [LinkedIn](https://www.linkedin.com/in/mekimba)
- Haewon Jeon      |  [Github](https://github.com/haewonito)   |   [LinkedIn](linkedin.com/in/haewonito)


