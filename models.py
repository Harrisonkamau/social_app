# import modules
import datetime
from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin
from peewee import *



# set up database
DATABASE = SqliteDatabase('social.db')


# create a users' model
class Users(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length=100)
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin = Boolean(default=False)

    class Meta:
        database = DATABASE
        order_by = ('-joined_at',)  # list users in a descending order

    @classmethod # without this, a user instance has to be created every time a new user is to be created
    def create_user(cls, username, email, password, admin=False):
        username = username,
        email = email,
        password = generate_password_hash(password)
        is_admin = admin



