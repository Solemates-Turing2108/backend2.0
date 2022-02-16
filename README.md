## Solemates - Backend Flask App

Many people need only one out of a pair of shoes that they buy. Solemates ([FE deployed endpoint](https://komodo-frontend.herokuapp.com)) ([BE deployed endpoint](https://turingsolemates.herokuapp.com/)) was created to connect people who have an extra shoe with those who need just one shoe. Once logged in, the user can browse shoes, filtered by size, side and style, and be connected to the seller via email if they find anything they like.    

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
```
        - As a raw jason body: 
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
           {
                "buyer_id": "buyer_id"
            }

      - Response:
       `Email has been successfully been sent to the seller`
  
Type: [Photo](#photo)
    - Arguments: 
        ```
          argument :keyword, String, required: true
        ```
  - **Get Photos**: all photos (user uploaded as well as those saved from Unsplash)
    - Type: [Photo](#photo)
    - Arguments: none

#### Users
  - **Get User**: user by ID
    - Type: [User](#user)
    - Arguments: 
        ```
          argument :id, ID, required: true
        ```
  - **Get Users**: all users
    - Type: [User](#user)
    - Arguments: none

#### Trips 
  - **Get Trip**: get a trip by ID
    - Type: [Trip](#trip)
    - Arguments: 
        ```
          argument :id, ID, required: true
        ```
        
        
# External APIs
This API consumes the following APIs:
- [Twilio](https://www.twilio.com/docs/sms/api) to send text messages
- [MapQuest Geocoding API](https://developer.mapquest.com/documentation/geocoding-api/) to provide map image

# Database Schema

<img width="1096" alt="Screen Shot 2022-01-13 at 5 00 21 PM" src="https://user-images.githubusercontent.com/86392608/149428762-bd0fd620-42f6-4c31-ac1f-e62c784de567.png">


# Contributors
- Jacob Yarborough |  [Github](https://github.com/jacobyarborough)   |   [LinkedIn](https://www.linkedin.com/in/jacob-yarborough/)
- Haewon Jeon      |  [Github](https://github.com/haewonito)   |   [LinkedIn](linkedin.com/in/haewonito/)
- Matt Holmes      |  [Github](https://github.com/matthewjholmes)   |   [LinkedIn](https://www.linkedin.com/in/matthew-j-holmes/)
- Stephanie Helm   |  [Github](https://github.com/stephaniemhelm)   |   [LinkedIn](https://www.linkedin.com/in/stephanie-helm-a4a032220/)
- Micha Bernhard   |  [Github](https://github.com/michab17)   |   [LinkedIn](https://www.linkedin.com/in/micha-bernhard/)







# Flask Project

## Steps

#### 1) Create a new virtual conda environment, activate that environment
This is not necessary, but will make deploying to heroku more efficient. When you pip freeze your requierment's file, you
will only capture the libraries necessary to run your app. 

#### 2) pip install requirements
Likely Need
- flask
- python-dotenv
- pandas
- gunicorn

if you are using postgres
- sqlalchemy
- psycopg2 (if this gives you an error, try psycopg2-binary)

#### 3) pip freeze > requirements.txt 
This step has already been done for you. Only repeat if you have add new libraries not included here

#### 4) delete the dataclasse library from the requirements.txt
If you remake the requirements.txt file, delete the dataclasse library. It throws an error in Heroku

### 5) in Heroku add a config variable that is your database url 

The config variable called DATABASE_URL that automatically populates with the Heroku Postgres Add-on is missing 'ql' at the end of 'postgres' at the start of the url. You can not edit this directly. So you need to make a new key:value pair below it. 

For this app I called the new DATABASE_URL just URL. 

### 6) Make sure you have a .env file on the same level as thr app.py. Assign the url for the postgres database to the same variable name as you did in Heroku. For this app, my .env contains:

URL = postgresql://.....(full url from heroku postgres config variables)

