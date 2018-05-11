import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Initialize SQLAlchemy
app.config.update(dict(
    SQLALCHEMY_DATABASE_URI="sqlite:///database.db",
    SECRET_KEY="R_L'ThemUt7_-Zm"
))
db = SQLAlchemy()
db.init_app(app)

# Load the views
from app import views

# Load the config file
app.config.from_object('config')
