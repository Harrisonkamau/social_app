from flask import Flask, g
import models


# Define variables
DEBUG = True
PORT = 8000
HOST = '0.0.0.0'


# create a flask Constructor
app = Flask(__name__)


@app.before_request
def before_request():
    """Connect to the database before each request"""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """Close the database after each request"""
    g.db.close()
    return response


# start the server
if __name__ == "__main__":
    app.run(debug=DEBUG, port=PORT, host=HOST)