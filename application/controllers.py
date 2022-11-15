from flask import render_template,Flask,jsonify
from flask import request,redirect
from flask import current_app as app
from flask_restful import Resource, Api

#LOCAL IMPORTS
from application.models import Student,Club,Announcement

app = Flask(__name__)
api = Api(app)
  
'''
@app.route('/allstudents', methods=['GET'])
def allstudents():
    k = Student.query.all()
    return render_template("potato.html",data = k,head="Students")

@app.route('/allclubs', methods=['GET'])
def allclubs():
    k = Club.query.all()
    return render_template("potato.html",data = k,head="Clubs")

@app.route('/allannouncements', methods=['GET'])
def allannouncements():
    k = Announcement.query.all()
    return render_template("potato.html",data = k,head="Announcements")
'''
def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d


class Square(Resource):
    def get(self, num):
        return jsonify({'square': num**2})
  
class Clubs(Resource):
    def get(self):
        k = Club.query.all()
        #print(k)
        #for i in k:
        #    print(row2dict(i))
        return jsonify(k)
    def post(self):
        data = request.get_json()
        #print(data)
        return jsonify({'data':data})


class Students(Resource):
    def get(self):
        k = Student.query.all()
        #print(k)
        #for i in k:
            #print(i.__dict__)
            #print(row2dict(i))
        return jsonify(k)

    def post(self):
        data = request.get_json()
        #print(data)
        return jsonify({'Student data updated with':data})


class Announcements(Resource):
    def get(self):
        k = Announcement.query.all()
        print(k)
        for i in k:
            print(row2dict(i))
        return jsonify(k)

api.add_resource(Square, '/square/<int:num>')
api.add_resource(Clubs,'/clubs')
api.add_resource(Students,'/students')
api.add_resource(Announcements,'/announcements')

