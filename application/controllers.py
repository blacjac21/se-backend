from flask import render_template
from flask import request,redirect
from flask import current_app as app

#LOCAL IMPORTS
from application.models import *


@app.route('/allclub', methods=['GET'])
def all():
    pass

@app.route('/misc', methods=['GET'])
def misc():
    pass