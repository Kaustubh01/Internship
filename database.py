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
    days = db.Column(db.String)
    status = db.Column(db.String, default='pending')
    feedback = db.Column(db.String)
    report = db.Column(db.String)
class Report(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    std_mobile = db.Column(db.Integer)
    std_email = db.Column(db.String)
    roll_as_intern = db.Column(db.String)
    emp_email = db.Column(db.String)
    supervisor_name = db.Column(db.String)
    supervisor_email = db.Column(db.String)
    supervisor_phone = db.Column(db.Integer)
    project_title = db.Column(db.String)
    project_desc = db.Column(db.String)
    resources = db.Column(db.String)
    learnings = db.Column(db.String)

class Feedback(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    question_1 = db.Column(db.Integer)
    question_2 = db.Column(db.Integer)
    question_3 = db.Column(db.Integer)
    question_4 = db.Column(db.Integer)
    question_5 = db.Column(db.Integer)
    question_6 = db.Column(db.Integer)
    question_7 = db.Column(db.Integer)
    question_8 = db.Column(db.Integer)


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

def set_internship_status(id, updated_status):
    internship = Internship.query.get(id)
    if internship:
        internship.status = updated_status
        db.session.commit()
        print('internship status updated')

def update_internship_feedback_status(id):
    internship = Internship.query.get(id)
    if internship:
        internship.feedback = "submitted"
        db.session.commit()
        print('internship status updated')
        
def update_internship_report_status(id):
    internship = Internship.query.get(id)
    if internship:
        internship.report = "submitted"
        db.session.commit()
        print('internship status updated')  

def set_internship_report(id, std_mobile, std_email, roll_as_intern,emp_email, supervisor_name,supervisor_email,supervisor_phone, project_title, project_desc,resources, learnings):
    report = Report(id = id,std_mobile=std_mobile, std_email=std_email,roll_as_intern=roll_as_intern,emp_email=emp_email,supervisor_name=supervisor_name,supervisor_email=supervisor_email,supervisor_phone=supervisor_phone,project_title=project_title,project_desc=project_desc,resources=resources,learnings=learnings)
    db.session.add(report)
    db.session.commit()

def set_internship_feedback(id,question_1,question_2,question_3,question_4,question_5,question_6,question_7,question_8):
    feedback = Feedback(id = id,question_1 = question_1,question_2 = question_2,question_3 = question_3, question_4 = question_4,question_5 = question_5, question_6 = question_6, question_7= question_7, question_8 = question_8)
    db.session.add(feedback)
    db.session.commit()

def init_app(app):
    db.init_app(app)