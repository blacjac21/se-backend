from flask import Flask
from flask_cors import CORS, cross_origin
import json

# LOCAL IMPORTS
from application.config import Config
from application.database import db
from application.models import *


# Initializing flask app
app = Flask(__name__,template_folder="templates")
app.config.from_object(Config)
db.init_app(app)
app.app_context().push()


# Setting up cross origin resource sharing
cors = CORS(app)  
app.config['CORS_HEADERS'] = 'Content-Type'
from application.controllers import *
# Running
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)