from flask import Flask, redirect, url_for, request, render_template, session
from database import Student,init_app, add_internship,get_student,  get_internships_organizations, update_password, authenticate_student, check_registration, get_all_internships, get_student_name, set_internship_status

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost/internship'

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
    session['internship_id'] = id
    return render_template('internship_view.html')

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

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        prn_number = request.form['prn_number']
        prn_id = Student.query.get(prn_number)
        if not check_registration(prn_number):
            if prn_id:
                session['prn']= prn_number
                session['student']= get_student(prn_number).name
                
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
        password = request.form.get('password')
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
            "internship":internship
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


        add_internship(prn= session.get('prn'), organization= organization_name, year = academic_year, roll_no= roll_no, duration= duration, start_date= start_date, end_date=end_date, work_time= work_time, days=days_string, std_class=student_class)
        
        return redirect(url_for('dashboard'))
    return render_template('request_internship.html',days = days)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug = True)
    
