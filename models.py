# import everything from peewee
from peewee import *
import datetime # import datetime


# set up database
DATABASE = SqliteDatabase('social.db')


# create a users' model
class Users(Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length=100)
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin = Boolean(default=False)

    class Meta:
        database = DATABASE
        order_by = ('-joined_at',)  # list users in a descending order

