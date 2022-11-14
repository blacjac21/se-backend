import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG = True
    SQLITE_DB_DIR = os.path.join(basedir,"../DB")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(SQLITE_DB_DIR,"clubs.sqlite3")
    SQLALCHEMY_TRACK_MODIFICATIONS = True