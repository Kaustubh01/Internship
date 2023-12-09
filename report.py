from flask import Blueprint, render_template, url_for, redirect, session,request, jsonify
from database import *
import datetime
import matplotlib.pyplot as plt
from io import BytesIO
import base64

report_bp = Blueprint('report',__name__)


def create_bar_yertical_graph():
    categories = ['Category A', 'Category B', 'Category C']
    values = [10, 20, 15]

    # Create the bar graph using Matplotlib with bars along the y-axis
    fig, ax = plt.subplots()
    bars = ax.barh(categories, values)

    # Remove the border around the graph by setting spines to 'none'
    for spine in ['top', 'right', 'bottom', 'left']:
        ax.spines[spine].set_visible(False)

    # Customize other aspects of the plot if needed
    ax.set_xlabel('Values')
    ax.set_ylabel('Categories')
    ax.set_title('Bar Graph with Bars on Y-Axis')

    # Save the plot to a BytesIO object
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    # Encode the image as base64
    img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')

    return img_base64

def create_bar_graph():
    categories = ['Category A', 'Category B', 'Category C']
    values = [10, 20, 15]

    # Create the bar graph using Matplotlib with bars along the y-axis
    fig, ax = plt.subplots()
    bars = ax.bar(categories, values)

    # Remove the border around the graph by setting spines to 'none'
    for spine in ['top', 'right', 'bottom', 'left']:
        ax.spines[spine].set_visible(False)

    # Customize other aspects of the plot if needed
    ax.set_xlabel('Values')
    ax.set_ylabel('Categories')
    ax.set_title('Bar Graph with Bars on Y-Axis')

    # Save the plot to a BytesIO object
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    # Encode the image as base64
    img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')

    return img_base64


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
    vertical_bar_graph = create_bar_yertical_graph()
    bar_graph = create_bar_graph()
    chart_image = generate_pie_chart()


    return render_template('year_end_summary.html', chart_image=chart_image, bar_graph=bar_graph,vertical_bar_graph = vertical_bar_graph)