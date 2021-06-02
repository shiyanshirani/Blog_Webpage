from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask-login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '7b8549b703e554ac883b29c2ad68df22'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
LoginManager = LoginManager(app)

from flaskblog import routes