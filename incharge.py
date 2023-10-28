from flask import Blueprint, render_template, url_for, redirect, session, request
from database import *

incharge_bp = Blueprint('incharge', __name__)

@incharge_bp.route('/incharge_dashboard', methods = ['GET', 'POST'])
def incharge_dashboard():
    data = []
    internships = get_all_internships()
    for internship in internships:
        data.append(
            {
                "name":get_student_name(internship.prn).split()[0].lower().capitalize() +' '+ get_student_name(internship.prn).split()[1].lower().capitalize() +' '+ get_student_name(internship.prn).split()[2].lower().capitalize(),
                "internship":internship,
                "is_pending": internship.status == "pending",
                "is_approved": internship.status == "Approved",
                "is_rejected": internship.status == "Rejected",
                "is_completed":internship.status == "completed"
            }
        )
    return render_template('incharge_dashboard.html', data = data)

@incharge_bp.route('/view_internship/<int:internship_id>', methods = ['GET', 'POST'])
def view_internship(internship_id):
    id = internship_id
    internship = get_internship(id)
    student = get_student(internship.prn)

    session['internship_id'] = id

    is_acknowledged = internship.status == 'Approved' or internship.status == 'Rejected' or internship.status == 'completed' 
    has_offer_letter = internship.offer_letter == 'submitted'
    has_certificate = internship.certificate == 'submitted'
    has_report = internship.report == 'submitted'
    has_feedback = internship.feedback == 'submitted'


    return render_template('internship_view.html', internship = internship, student = student, is_acknowledged = is_acknowledged, has_offer_letter = has_offer_letter, has_certificate = has_certificate, has_report = has_report, has_feedback = has_feedback)

@incharge_bp.route('/approve', methods = ['POST'])
def approve():
    if request.method == 'POST' and request.form['action'] == 'Approve':
        set_internship_status(session.get('internship_id'), 'Approved')
    return redirect(url_for('incharge.incharge_dashboard'))

@incharge_bp.route('/reject', methods = ['POST'])
def reject():
    if request.method == 'POST' and request.form['action'] == 'Reject':
        set_internship_status(session.get('internship_id'), 'Rejected')
    return redirect(url_for('incharge.incharge_dashboard'))

@incharge_bp.route('/view_report')
def view_report():
    internship = get_internship(session.get('internship_id'))
    student = get_student(internship.prn)
    report = get_report(session.get('internship_id'))
    signature_url = url_for('static', filename=f"student/{internship.prn}/signature/signature.png")
    return render_template('report_view.html' , report = report, internship = internship, student = student)

@incharge_bp.route('/view_feedback')
def view_feedback():
    internship = get_internship(session.get('internship_id'))
    student = get_student(internship.prn)
    report = get_report(session.get('internship_id'))
    feedback = get_feedback(session.get('internship_id'))

    signature_url = url_for('static', filename=f'students/{internship.prn}/signature/signature.png')

    return render_template('feedback_view.html', feedback = feedback, internship = internship, student = student, report = report,signature = signature_url)


