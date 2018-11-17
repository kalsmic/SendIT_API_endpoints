# SendIT_API_endpoints
SendIT is a courier service that helps users deliver parcels to different destinations. SendIT provides courier quotes based on weight categories.

[![Build Status](https://travis-ci.org/kalsmic/SendIT_API_endpoints.svg?branch=develop)](https://travis-ci.org/kalsmic/SendIT_API_endpoints)
[![Coverage Status](https://coveralls.io/repos/github/kalsmic/SendIT_API_endpoints/badge.svg?branch=revise_app_structure)](https://coveralls.io/github/kalsmic/SendIT_API_endpoints?branch=revise_app_structure)
 [![Maintainability](https://api.codeclimate.com/v1/badges/e99a380566f753e21417/maintainability)](https://codeclimate.com/github/kalsmic/SendIT_API_endpoints/maintainability)


**SENDIT API ENDPOINTS**

| EndPoint | Functionality  |
| ------------ | ------------ |
|GET /parcels   | Fetch all parcel delivery orders  |
|GET /parcels/<parcelId>   | Fetch a specific parcel delivery order  |
|GET /users/<userId>/parcels |Fetch all parcel delivery orders by a specific user|
|PUT /parcels/<parcelId>/cancel | Cancel the specific parcel delivery order |
|POST /parcels | Create a parcel delivery order|

How to set up the project
Open the terminal and run the following commands
```bash

    $ > git clone https://github.com/kalsmic/SendIT_API_endpoints.git
    $ > cd sendIT
    $ > git checkout develop
    $ > python3 -m venv venv
    $ > source venv/bin.activate
    $ > pip3 install -r requirements.txt
    $ > EXPORT FLASK_APP
    $ > flask run
    Open http://127.0.0.1:5000/  in your web browser.
   ```
### How to run tests
- Open terminal from root folder of the project.
- Enter the commnad bellow in the treminla to run the tests
```bash
  $ > pytest
  ```
