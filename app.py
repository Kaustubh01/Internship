from flask import Flask, redirect, url_for, request, render_template, session
from datetime import datetime
import os
from database import Student,init_app, add_internship,get_student,  get_internships_organizations, update_password, authenticate_student, check_registration, get_all_internships, get_student_name,set_internship_report,set_internship_feedback, set_internship_status,update_internship_feedback_status,update_internship_report_status,update_internship_offer_letter_status, update_internship_certificate_status, get_internship, get_feedback, get_report



app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Password@localhost/internship'


init_app(app)
@app.route('/', methods=['GET', 'POST'])
def index():
    selected_button = request.form.get('redirect_button')

    if selected_button == 'register':
        return redirect(url_for('register'))
    elif selected_button == 'login':
        return redirect(url_for('login'))
    elif selected_button == 'login_incharge':
        return redirect(url_for('incharge_login'))
    return render_template('index.html')
   

@app.route('/incharge_login', methods=['GET','POST'])
def incharge_login():
    if request.method == 'POST':
        return redirect(url_for('incharge_dashboard'))

    return render_template('incharge_login.html')

@app.route('/incharge_dashboard', methods = ['GET', 'POST'])
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
            }
        )
        print()
    return render_template('incharge_dashboard.html', data = data)

@app.route('/view_internship/<int:internship_id>', methods = ['GET', 'POST'])
def view_internship(internship_id):
    id = internship_id
    internship = get_internship(id)
    student = get_student(internship.prn)

    session['internship_id'] = id

    is_acknowledged = internship.status == 'Approved' or internship.status == 'Rejected'
    has_offer_letter = internship.offer_letter == 'submitted'
    has_certificate = internship.certificate == 'submitted'
    has_report = internship.report == 'submitted'
    has_feedback = internship.feedback == 'submitted'


    return render_template('internship_view.html', internship = internship, student = student, is_acknowledged = is_acknowledged, has_offer_letter = has_offer_letter, has_certificate = has_certificate, has_report = has_report, has_feedback = has_feedback)

@app.route('/approve', methods = ['POST'])
def approve():
    if request.method == 'POST' and request.form['action'] == 'Approve':
        set_internship_status(session.get('internship_id'), 'Approved')
    return redirect(url_for('incharge_dashboard'))

@app.route('/reject', methods = ['POST'])
def reject():
    if request.method == 'POST' and request.form['action'] == 'Reject':
        set_internship_status(session.get('internship_id'), 'Rejected')
    return redirect(url_for('incharge_dashboard'))

@app.route('/view_report')
def view_report():
    internship = get_internship(session.get('internship_id'))
    student = get_student(internship.prn)
    report = get_report(session.get('internship_id'))
    signature_url = url_for('static', filename=f"student/{internship.prn}/signature/signature.png")
    return render_template('report_view.html' , report = report, internship = internship, student = student)

@app.route('/view_feedback')
def view_feedback():
    internship = get_internship(session.get('internship_id'))
    student = get_student(internship.prn)
    report = get_report(session.get('internship_id'))
    feedback = get_feedback(session.get('internship_id'))

    signature_url = url_for('static', filename=f'students/{internship.prn}/signature/signature.png')

    return render_template('feedback_view.html', feedback = feedback, internship = internship, student = student, report = report,signature = signature_url)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        prn_number = request.form['prn_number']
        prn_id = Student.query.get(prn_number)
        if not check_registration(prn_number):
            if prn_id:
                session['prn']= prn_number
                session['student']= get_student(prn_number).name
                folder_name = session.get('prn')
                base_directory = "static/students"

                student_folder_path = os.path.join(base_directory, folder_name)
                os.makedirs(student_folder_path)
                print('folder created')
                
                return redirect(url_for('set_password'))
            else:
                return "you are not registered yet"
        else:
            return "you already have an account go to login"
    return render_template('register.html',name = session.get('student'))

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        prn = request.form.get('prn')
        session['prn'] = prn
        session['student']= get_student(prn).name
        if authenticate_student(prn, password):
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid Credentials'
    return render_template('login.html')


@app.route('/set_password',methods = ['POST','GET'])
def set_password():
    

    if request.method =='POST':

        if 'file' not in request.files:
            return "No file part"
    
        file = request.files['file']

        if file.filename == '':
            return "No selected file"

        if file:
            file.filename= 'signature.png'
            base_directory = f"static/students/{session.get('prn')}"

            signature_folder_path = os.path.join(base_directory, 'signature')
            os.makedirs(signature_folder_path)
            file.save(f"{signature_folder_path}/" + file.filename)

        password = request.form.get('password')
        username = request.form.get('username')
        update_password(password, session.get('prn'))

        return redirect(url_for('dashboard'))
    return render_template('set_password.html',name = session.get('student'))


@app.route('/dashboard')
def dashboard():
    data = []
    internships = get_internships_organizations(session.get('prn'))
    for internship in internships:
        data.append({
            "status":internship.status =="Approved",
            "internship":internship,
            "is_completed":internship.end_date <=datetime.now().date(),
            "has_report":internship.report == 'submitted',
            "has_feedback":internship.feedback == 'submitted',
            "has_offer_letter":internship.offer_letter == 'submitted',
            "has_certificate":internship.certificate == 'submitted'
        })
    student_name = session.get('student')
    first_name = student_name.split()[1].lower().capitalize()


    return render_template('dashboard.html', student_name = first_name,data = data)


@app.route('/add_new_internship', methods=['POST','GET'])
def add_new_internship():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if request.method == 'POST':
        academic_year = request.form.get('academic_year')
        student_class = request.form.get('class')
        roll_no = request.form.get('roll_no')
        organization_name = request.form.get('organization_name')
        duration = request.form.get('duration')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        work_time = request.form.get('work_time')

        selected_days = request.form.getlist('selected_days')
        days_string = ', '.join([str(day) for day in selected_days])


        add_internship(prn= session.get('prn'), organization= organization_name, year = academic_year, duration= duration, start_date= start_date, end_date=end_date, work_time= work_time, days=days_string, std_class=student_class)
        
        return redirect(url_for('dashboard'))
    return render_template('request_internship.html',days = days)

@app.route('/upload_offer_letter/<int:internship_id>', methods=['GET', 'POST'])
def upload_file(internship_id):
    id = internship_id
    if request.method == 'POST':

        if 'file' not in request.files:
            return "No file part"
    
        file = request.files['file']

        if file.filename == '':
            return "No selected file"

        if file:
            base_directory = f"students/{session.get('prn')}"

            offer_letter_folder_path = os.path.join(base_directory, 'offer_letter')
            if not os.path.exists(offer_letter_folder_path):
                os.makedirs(offer_letter_folder_path)
            new_filename = f'{id}.pdf'
            file.filename = new_filename
            file.save(f"{offer_letter_folder_path}/" + file.filename)
            update_internship_offer_letter_status(id)
            return redirect(url_for('dashboard'))
    
    return render_template('upload.html')

@app.route('/certificate/<int:internship_id>', methods = ['GET', 'POST'])
def upload_certificate(internship_id):
    id = internship_id
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
    
        file = request.files['file']

        if file.filename == '':
            return "No selected file"

        if file:
            base_directory = f"students/{session.get('prn')}"

            completion_certificate_folder_path = os.path.join(base_directory, 'completion_certificate')
            if not os.path.exists(completion_certificate_folder_path):
                os.makedirs(completion_certificate_folder_path)
            new_filename = f'{id}.pdf'
            file.filename = new_filename
            file.save(f"{completion_certificate_folder_path}/" + file.filename)
            update_internship_certificate_status(id)
        return redirect(url_for('dashboard'))

    return render_template('upload_certificate.html',id = id)

@app.route('/report-form/<int:internship_id>', methods=['GET', 'POST'])
def report_form(internship_id):
    id = internship_id
    if request.method == 'POST':
        
        session['internship_id'] = id

        mobile = request.form['mobile']
        email = request.form['email']
        role = request.form['role']
        employer_email = request.form['employerEmail']
        supervisor_name = request.form['supervisorName']
        supervisor_email = request.form['supervisorEmail']
        supervisor_contact = request.form['supervisorContact']
        project_title = request.form['projectTitle']
        work_done = request.form['workDone']
        resources = request.form['resources']
        learnings = request.form['learnings']
        set_internship_report(id=id, std_mobile=mobile,std_email=email,roll_as_intern=role,emp_email=employer_email,supervisor_name=supervisor_name, supervisor_email=supervisor_email, supervisor_phone=supervisor_contact,project_title=project_title,project_desc=work_done, resources=resources, learnings=learnings)

        update_internship_report_status(id)
        
        return redirect(url_for('dashboard'))

    return render_template('reportInput.html',id = id)

@app.route('/feedback-form/<int:internship_id>', methods=['GET','POST'])
def feedback_form(internship_id):
    id = internship_id
    if request.method == 'POST':
        
        session['internship_id'] = id

        q1 = request.form['q1']
        q2 = request.form['q2']
        q3 = request.form['q3']
        q4 = request.form['q4']
        q5 = request.form['q5']
        q6 = request.form['q6']
        q7 = request.form['q7']
        q8 = request.form['q8']

        set_internship_feedback(id=id, question_1=q1, question_2=q2, question_3=q3, question_4=q4, question_5=q5,question_6=q6,question_7=q7, question_8=q8)

        update_internship_feedback_status(id)
        
        return redirect(url_for('dashboard'))
    return render_template('feedbackInput.html', id =id)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug = True)
    
