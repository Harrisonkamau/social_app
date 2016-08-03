from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Regexp
from models import User


class RegisterForm(Form):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Regexp(
                r'^[a-zA-z0-9_]+',
                message='User name should be one word,letters, numbers and underscores only'
            ),
            name_exists
        ]
    )