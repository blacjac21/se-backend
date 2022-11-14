from flask import Flask
from flask_cors import CORS, cross_origin
import json

# LOCAL IMPORTS
from application.config import Config
from application.database import db
from application.models import *

# Initializing flask app
app = Flask(__name__)
app.config.from_object(Config)

# Setting up cross origin resource sharing
cors = CORS(app)  
app.config['CORS_HEADERS'] = 'Content-Type'
      
# Running
if __name__ == '__main__':
    app.run(debug=True,port=8080)