from flask import render_template
from flask import request,redirect
from flask import current_app as app

#LOCAL IMPORTS
from application.models import Student,Club,Announcement


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
