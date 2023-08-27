from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Internship(db.Model):
    prn = db.Column(db.Integer, primary_key = True)
    organization = db.Column(db.String)
    duration = db.Column(db.String)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    offer_letter = db.Column(db.BLOB)