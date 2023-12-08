from flask import Blueprint, render_template, url_for, redirect, session,request, jsonify
from database import *
import datetime
import matplotlib.pyplot as plt
from io import BytesIO
import base64

report_bp = Blueprint('report',__name__)

def generate_pie_chart():
    labels = ['Label 1', 'Label 2', 'Label 3']
    values = [30, 50, 20]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

    # Save the plot to a BytesIO object
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)

    # Encode the image as base64
    image_base64 = base64.b64encode(image_stream.read()).decode('utf-8')

    plt.close()  # Close the plot to free up resources

    return image_base64

@report_bp.route('/report-nav')
def report_nav():
    return render_template('report-nav.html')

@report_bp.route('/last-three-years')
def last_three_years():
    internships = get_all_internships()
    chart_image = generate_pie_chart()


    return render_template('year_end_summary.html', chart_image=chart_image)