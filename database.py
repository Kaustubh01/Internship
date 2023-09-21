from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker

db = SQLAlchemy()

class Student(db.Model):
    prn = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    password = db.Column(db.String(255))


class Internship(db.Model):

    internship_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    prn = db.Column(db.Integer)
    year = db.Column(db.String)
    std_class = db.Column(db.String)
    roll_no = db.column(db.Integer)
    organization = db.Column(db.String)
    duration = db.Column(db.String)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    work_time =db.Column(db.String)
    days = db.Column(db.Integer)
    status = db.Column(db.String, default='pending')

def get_student(prn):
    return Student.query.get(prn)

def update_password(password, prn):
    student = Student.query.get(prn)
    if student:
        student.password = password
        db.session.commit()
        print('password updated')

def authenticate_student(prn, password):
    student = Student.query.get(prn)
    if student.password == password:
        print('student is registered')
        return True
    return False

def check_registration(prn):
    student = Student.query.get(prn)
    if student.password is not None:
        return True
    


def add_internship(prn, organization, year, roll_no, duration, start_date, end_date, work_time, days, std_class):
    internship = Internship(prn = prn, year = year , roll_no = roll_no, organization = organization, duration = duration, start_date = start_date, end_date = end_date, work_time=work_time, days = days, std_class = std_class)
    db.session.add(internship)
    db.session.commit()

def get_internships_organizations(prn):
    return Internship.query.filter_by(prn=prn).all()

def get_all_internships():
    return Internship.query.all()

def get_student_name(prn):
    student = Student.query.get(prn)
    return student.name


def init_app(app):
    db.init_app(app)