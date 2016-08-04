from flask import Flask, g, render_template, redirect, flash, url_for
from flask.ext.login import LoginManager

import forms
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
login_manager.login_view = 'login'



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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        flash('Registration successful!', 'success')
        models.User.create_user(
            username=form.uername.data,
            email=form.email.data,
            password=form.password.data
        )
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/')
def index():
    return "Welcome to my social app!"


# start the server
if __name__ == "__main__":
    models.initialize()
    try:
        models.User.create_user(
            username='harrisonkamau',
            email='kamauharry@yahoo.com',
            password='password',
            admin=True
        )
    except ValueError:
        pass

    app.run(debug=DEBUG, port=PORT, host=HOST)