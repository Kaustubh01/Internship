from flask import Flask, redirect, url_for, request, render_template, session
from database import Student,init_app, add_student, add_internship,get_student,  get_internships_organizations, update_password, authenticate_student, check_registration

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
    return render_template('index.html')

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
    internships = get_internships_organizations(session.get('prn'))
    student_name = session.get('student')
    first_name = student_name.split()[1].lower().capitalize()
    return render_template('dashboard.html', student_name = first_name,internships = internships)

@app.route('/request_internship')
def request_internship():
    return render_template('request_internship.html')

@app.route('/add_new_internship', methods=['POST'])
def add_new_internship():
    student_prn = session.get('prn')
    new_organization = request.form.get('organization')
    new_employer = request.form.get('employer-name')
    add_internship(student_prn, new_organization, new_employer)
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug = True)
    
