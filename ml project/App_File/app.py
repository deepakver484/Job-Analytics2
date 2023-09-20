# Importing necessary modules and functions from Flask and pandas
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import sys

# Adding a custom directory to the system path
sys.path.insert(0, 'C:/Users/DEEPAK VERMA/Desktop/ml project/backend')

# Importing functions from the 'data_dao' module
from data_dao import skill_job, skill_details, job_details, job_job

# Reading data from CSV files into DataFrames
df = pd.read_csv('final_all_data.csv')
df1 = pd.read_csv('users.csv')

# List of skills for searching
skills = ['python', 'c', 'r', 'java', 'hadoop', 'scala', 'flask', 'pandas', 'spark',
          'numpy', 'php', 'sql', 'mysql', 'dbms', 'mongdb', 'nltk', 'keras', 'pytorch', 'tensorflow',
          'linux', 'ruby', 'django', 'react', 'excel', 'reactjs', 'ai', 'ui', 'tableau', 'cad', 'php']

# Initialize the Flask app
app = Flask(__name__)

# Route for the login page
@app.route('/') 
def login():
    place = {'emailpl' : 'Email' , 'passwordpl' : 'Password'}
    return render_template('login.html', data=place, color='black')

# Route to handle form submission for login
@app.route('/signin', methods=['POST']) 
def signin():
    object = request.form.to_dict()
    email = df1['email'].to_list()
    password = df1['password'].to_list()
    if object['email'] in email and object['password'] in password:
        return redirect('/home')
    else:
        if object['email'] not in email:
            place = {'emailpl': 'No data Found !!!', 'passwordpl': 'Password'}
            return render_template('login.html', data=place)
        elif object['password'] not in password:
            place = {'emailpl': 'Email', 'passwordpl': 'Wrong Password !!!'}
            return render_template('login.html', data=place)

# Route to handle form submission for signup
@app.route('/signup', methods=['POST']) 
def signup():
    object = request.form.to_dict()
    email = df1['email'].to_list()
    if object['email'] in email:
        place = {'emailpl': 'User Already Exist', 'passwordpl': 'Password'}
        return render_template('login.html', data=place)
    else:
        df1 = df1.append(object, ignore_index=True)
        df1.to_csv('users.csv')
        return redirect('/home')

# Route for the home page
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        object = request.form.to_dict()
        if object["skill"].lower() not in skills:
            data = {'placeholder': "Search Relevant Skill"}
        else:
            data = skill_job(object['skill'], df)
            if 'placeholder' not in data.keys():
                data['placeholder'] = object['skill']
        details = []
        return render_template('index.html', data=data, details=details)
    else:
        data = {"placeholder": "Search your skills here"}
        details = []
        return render_template('index.html', data=data, details=details)

# Route to display skill details
@app.route('/skilldetails', methods=['POST'])
def skilldetails():
    object = request.form.to_dict()
    data = skill_job(object['skill'], df)
    if 'placeholder' not in data.keys():
        data['placeholder'] = object['skill']
    details = skill_details(object['skill'], df)
    return render_template('index.html', data=data, details=details)

# Route for the job search page
@app.route('/job', methods=['GET', 'POST'])
def job():
    if request.method == 'POST':
        object = request.form.to_dict()
        data = job_job(object['job'], df)
        if 'placeholder' not in data.keys():
            data['placeholder'] = object['job']
        details = []
        return render_template('job.html', data=data, details=details)
    else:
        data = {"placeholder": "Search your Job Title here"}
        details = []
        return render_template('job.html', data=data, details=details)

# Route to display job details
@app.route('/jobdetails', methods=['POST'])
def jobdetails():
    object = request.form.to_dict()
    data = job_job(object['job'], df)
    if 'placeholder' not in data.keys():
        data['placeholder'] = object['job']
    details = job_details(object['job'], df)
    return render_template('job.html', data=data, details=details)

# Route for the dashboard page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Entry point to run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
