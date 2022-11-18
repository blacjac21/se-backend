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
        Club.create(club_id = data['club_id'],description=data['description'],logo=data['logo'],tags=data['tags'],name=data['name'],images=data['images'],social_links=data['social_links'])
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
        #print(k)
        #for i in k:
        #   print(row2dict(i))
        return jsonify(k)

    def post(self):
        data = request.get_json()
        cid = Club.query.filter_by(name = data['club_name']).first()
        #print("cid",cid.club_id)
        Announcement.create(announcement_name= data['announcement_name'],club_id=cid.club_id,club_name=data['club_name'],description=data['description'],image=data['image'],url=data['url'])
        return jsonify({'Announcement created with':data})

api.add_resource(Square, '/square/<int:num>')
api.add_resource(Clubs,'/clubs')
api.add_resource(Students,'/students')
api.add_resource(Announcements,'/announcements')

