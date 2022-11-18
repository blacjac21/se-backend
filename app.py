from flask import Flask
from flask_cors import CORS, cross_origin
import json
from flask_restful import Resource, Api
from application.controllers import app,api

# LOCAL IMPORTS
from application.config import Config
from application.database import db
from application.models import *


# Initializing flask app
#app = Flask(__name__,template_folder="templates")
app.config.from_object(Config)
db.init_app(app)
app.app_context().push()

api = Api(app)

# Setting up cross origin resource sharing
cors = CORS(app)  
app.config['CORS_HEADERS'] = 'Content-Type'
from application.controllers import *
# Running
if __name__ == '__main__':
    app.run(host='10.20.205.97',port=8080)