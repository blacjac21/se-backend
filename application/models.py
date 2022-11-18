from .database import db
from wtforms import StringField
from dataclasses import dataclass

@dataclass
class Club(db.Model):
    __tablename__ = 'Club'
    name:str
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

    def __init__(self,name:str,description: str,logo:str,tags:str,club_id:int, images:str,social_links:str):
        self.name = name
        self.description = description
        self.logo = logo
        self.tags = tags
        self.club_id = club_id
        self.images = images 
        self.social_links = social_links

    @staticmethod
    def create(name:str,description: str,logo:str,tags:str,club_id:int, images:str,social_links:str):
        newclub = Club(name,description,logo,tags,club_id,images,social_links)
        db.session.add(newclub)
        db.session.commit()

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

    def __init__(self,name:str,srn:str,branch:str,email_id:str,roles:str):
        self.name = name
        self.srn = srn
        self.branch = branch
        self.email_id = email_id
        self.roles = roles

    @staticmethod
    def create(name:str,srn: str,branch:str,email_id:str,roles:str):
        newStud = Student(name,srn,branch,email_id,roles)
        db.session.add(newStud)
        db.session.commit()

@dataclass
class Announcement(db.Model):
    __tablename__ = "Announcement"
    announcement_id : int
    announcement_name : str
    club_id :int
    club_name : str
    description : str
    url :str
    image : str

    announcement_id = db.Column(db.Integer,primary_key=True)
    announcement_name = db.Column(db.String())
    club_id = db.Column(db.Integer)
    club_name = db.Column(db.String())
    description = db.Column(db.String())
    url = db.Column(db.String())
    image = db.Column(db.String())

    def __init__(self,announcement_name:str,club_id:int,club_name:str,description:str,image:str,url:str):
        self.announcement_name = announcement_name
        self.club_id = club_id
        self.club_name = club_name
        self.description = description
        self.image = image
        self.url = url

    @staticmethod
    def create(announcement_name:str,club_id:int,club_name:str,description:str,image:str,url:str):
        newannouncement = Announcement(announcement_name,club_id,club_name,description,image,url)
        db.session.add(newannouncement)
        db.session.commit()

