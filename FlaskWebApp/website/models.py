from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000)) ##Stock name
    #date = db.Column(db.DateTime(timezone=True), default=func.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    price = db.Column(db.Float)

class College(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #professor_id = db.Column(db.Integer, db.ForeignKey('Professor.id'))
    link = db.Column(db.String(1000))
    area = db.Column(db.String(1000))
    sop = db.Column(db.String(100000))
    comment = db.Column(db.String(10000))
    professors = db.relationship('Professor')
    poi = db.Column(db.String(1000))
    poi_link = db.Column(db.String(1000))
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    notes = db.relationship('Note')
    colleges = db.relationship('College')
class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    college_id = db.Column(db.Integer, db.ForeignKey('college.id'))
    name = db.Column(db.String(1000))
    link = db.Column(db.String(1000))
    note = db.Column(db.String(1000))
    #colleges = db.relationship('College')