from flask import Blueprint, render_template, url_for, redirect, session,request, jsonify
from database import *
import datetime

report_bp = Blueprint('report',__name__)



@report_bp.route('/data')
def data():
    internships = get_all_internships()
    years = {}

    for internship in internships:
        if internship.status == 'completed':
            year = internship.year
            if year in years:
                years[year] +=1
            else:
                years[year] = 1
    
    print(years)

    company_data = {
    "years": list(years.keys()),
    "students": list(years.values()),
    # "color": ["red", "green", "blue", "orange"]
    }
    return jsonify(company_data)

@report_bp.route('/report-nav')
def report_nav():
    return render_template('report-nav.html')

@report_bp.route('/last-three-years')
def last_three_years():
    return render_template('last-three-years.html')