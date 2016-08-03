from flask import Flask, g
from flask.ext.login import LoginManager
import models


# Define variables
DEBUG = True
PORT = 8000
HOST = '0.0.0.0'


# create a flask Constructor
app = Flask(__name__)


# create a secret key
app.secret_key = 'auoesh.beoehgh.32.tibe.jeen'

# create a login manager
login_manager = LoginManager()
login_manager.init_app(app)  # sets up the login manager for the app
login_manager.login.view = 'login'


@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id ==  userid)
    except models.DoesNotExist:  # exception got from peewee
        return None



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