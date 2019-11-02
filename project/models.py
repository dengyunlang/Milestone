# models.py
from flask_login import UserMixin

from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(1000))
    role = db.Column(db.Integer) # 0 is user, 1 is delegate
    attamptlogtime = db.Column(db.Integer)

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    username = db.Column(db.String(100), unique=True)
    action = db.Column(db.String(100))

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    candidateid = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100))
    totalballot = db.Column(db.Integer)

