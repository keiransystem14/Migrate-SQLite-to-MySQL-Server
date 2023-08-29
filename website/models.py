from website import app_db
from flask_login import UserMixin
from sqlalchemy import func

"""

Create two class for objects called Note and User and then associate the note with the user account by create a relationship between those two classes. 

"""

class Note(app_db.Model):
    id = app_db.Column(app_db.Integer, primary_key=True)
    data = app_db.Column(app_db.String(10000)) #error with forgetting to include .String.
    date = app_db.Column(app_db.DateTime(timezone=True), default=func.now())
    user_id = app_db.Column(app_db.Integer,app_db.ForeignKey('user.id'))

class User(app_db.Model, UserMixin):
    id = app_db.Column(app_db.Integer, primary_key=True)
    email = app_db.Column(app_db.String(150), unique=True)
    password = app_db.Column(app_db.String(150))
    first_name = app_db.Column(app_db.String(150)) 
    Notes = app_db.relationship('Note')