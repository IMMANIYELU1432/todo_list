from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo_list.db'
db = SQLAlchemy(app)
from todo_list import routes
from todo_list import models