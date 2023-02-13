from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_login
import flask_bcrypt
from grocery_app.config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

login_manager = flask_login.LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)

from grocery_app.models import User


@login_manager.user_loader
def user_loader(id):
    user = User.query.get(id)
    return user


bcrypt = flask_bcrypt.Bcrypt(app)
