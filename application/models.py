from .database import db
from wtforms import StringField
from dataclasses import dataclass

@dataclass
class Club(db.Model):
    __tablename__ = 'Club'
    name: str
    description: str
    logo:str
    tags:str
    club_id:int
    images:str
    social_links:str

    name = db.Column(db.String())
    description = db.Column(db.String())
    logo = db.Column(db.String())
    tags = db.Column(db.String())
    club_id = db.Column(db.Integer(),primary_key=True)
    images = db.Column(db.String())
    social_links = db.Column(db.String())

@dataclass
class Student(db.Model):
    __tablename__ = "Student"
    name:str
    srn:str
    branch :str
    email_id:str
    roles :str
    name = db.Column(db.String())
    srn = db.Column(db.String(),primary_key=True)
    branch = db.Column(db.String())
    email_id = db.Column(db.String())
    roles = db.Column(db.String())

@dataclass
class Announcement(db.Model):
    __tablename__ = "Announcement"
    announcement_id : int
    club_id :int
    description : str
    url :str
    image : str

    announcement_id = db.Column(db.Integer,primary_key=True)
    club_id = db.Column(db.Integer)
    description = db.Column(db.String())
    url = db.Column(db.String())
    image = db.Column(db.String())



