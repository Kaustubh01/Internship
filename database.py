from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    prn = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    password = db.Column(db.String(255))


class Internship(db.Model):

    internship_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    prn = db.Column(db.Integer)
    organization = db.Column(db.String)
    employer = db.Column(db.String)

def add_student():
    student = Student(prn = 2, name="Omkar")
    db.session.add(student)
    db.session.commit()

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
    


def add_internship(prn, organization, employer):
    internship = Internship(prn = prn, organization = organization, employer = employer)
    db.session.add(internship)
    db.session.commit()

def get_internships_organizations(prn):
    return Internship.query.filter_by(prn=prn).all()


def init_app(app):
    db.init_app(app)

