from flask import Flask, request,jsonify
from flask_cors import CORS, cross_origin
import json

# Initializing flask app
app = Flask(__name__)
  
cors = CORS(app)  
app.config['CORS_HEADERS'] = 'Content-Type'

# Route for seeing a data
@app.route('/dec', methods=['GET'])
def declaration():
    args = request.args
    k = args.get("foldername")
    down(k)
    i = getDecDeets(k)
    return i

@app.route('/misc', methods=['GET'])
def key():
    args = request.args
    k = args.get("filename")
    i = show(k)
    return i
      
# Running app
if __name__ == '__main__':
    app.run(debug=True)