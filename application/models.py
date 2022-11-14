from .database import db
from wtforms import StringField


class Club(db.Model):
    __tablename__ = 'Club'
    name = db.Column(db.String())
    description = db.Column(db.String())
    logo = db.Column(db.LargeBinary)
    tags = db.Column(db.String())
    club_id = db.Column(db.Integer(),primary_key=True)
    images = db.Column(db.LargeBinary)
    social_links = db.Column(db.String())

class Student(db.Model):
    __tablename__ = "Student"
    name = db.Column(db.String())
    srn = db.Column(db.String(),primary_key=True)
    branch = db.Column(db.String())
    email_id = db.Column(db.String())
    roles = db.Column(db.String())

class Announcement(db.Model):
    __tablename__ = "Announcement"
    announcement_id = db.Column(db.Integer,primary_key=True)
    club_id = db.Column(db.Integer)
    description = db.Column(db.String())
    url = db.Column(db.String())
    image = db.Column(db.LargeBinary)



