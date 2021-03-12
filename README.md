[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# RESTFUL-DJANGO-PYTHON-ROOM-BOOKING-SYSTEM
 * RESTFUL DJANGO BACKEND API FOR ROOM BOOKING SYSTEM

## To run system
 * Open folder in IDE
 * Open terminal
 * Type 'pipenv shell' in the terminal to get into the virtual environment
 * Type 'python manage.py runserver' in the terminal to run the server

 ## To run API CRUD commands
 * Open Postman
 ### To get all data
 * Create workspace and select GET command
 * Provide the url for API list /url/api/
 * You should have Python code for getting list, then you can send the request
 ### To get specific data
 * Select GET command
 * Provide the url for API list /url/api/1/
 * You should have Python code for getting specific list, then you can send the request
 ### To post data
 * Select POST command
 * Provide the url for API list /url/api/
 * In the headers parameters provide KEY (Content-Type) and VALUE (application/json)
 * You should have Python code for posting list, then you can send the request
 ### To delete data
 * Select DEL command
 * Provide the url for API list /url/api/1/
 * You should have Python code for deleting list, then you can send the request
 * It can only recommended to delete one by one /1/ /2/ /3/ ...
 ### To update data
 * Select PUT command
 * Provide the url for API list /url/api/1/
 * Modify the information in the BODY parameter
 * You should have Python code for updating list, then you can send the request

 ## Navigation of the system
 * You can test the API by the Postman Software tools
 * URL /api - displays all bookings
 * URL /api/1 - displays the specific booking

## Usage
* GET BOOKING
* CREATE BOOKING
* UPDATE BOOKING
* DELETE BOOKING

## Technology
 * Python 3.9.1 64-bit
 * Django RESTFUL Framework
 * Django cors headers

 ## Tested with Postman
 
## Contributing
* Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

