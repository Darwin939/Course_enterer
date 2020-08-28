from flask import Flask,render_template,request , redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager , login_required
from config import Config
from flask_login import UserMixin

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config.from_object(Config)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.init_app(app)

from .view import  *



