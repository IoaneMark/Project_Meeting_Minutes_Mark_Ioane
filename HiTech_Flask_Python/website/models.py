from datetime import datetime
from turtle import title
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(111))
    topic = db.Column(db.String(111))
    datetime = db.Column(db.String(300))
    attendee = db.Column(db.String(150))
    raised = db.Column(db.String(100))
    actions = db.Column(db.String(100))
    actionsby = db.Column(db.String(100))
    information = db.Column(db.String(300))
    completion = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    meetings = db.relationship('Meeting')