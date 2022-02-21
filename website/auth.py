<<<<<<< HEAD
from flask import Blueprint, render_template, redirect, url_for, request
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/') # login page when you enter the site
def index():
	return render_template('login.html')

@auth.route('/login', methods=['POST', 'GET']) # POST request to authenticate user
def login():
    if request.method == 'POST':
        user = request.form['username']
        return redirect(url_for('auth.calendar', usr=user)) # routes to calendar of user upon successful authentication
    else: 
        return render_template('login.html')

@auth.route('/<usr>') # should be routed properly to user's profile
def user(usr):
    return render_template('profile.html')

@auth.route('/profile')
def profile():
    return render_template('profile.html')

@auth.route('/signup') 
def signup():
    return render_template('signup.html')

@auth.route('/calendar')
def calendar():
    return render_template('calendar_events.html')

=======
from flask import Blueprint, render_template, redirect, url_for, request
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/') # login page when you enter the site
def index():
	return render_template('login.html')

@auth.route('/login', methods=['POST', 'GET']) # POST request to authenticate user
def login():
    if request.method == 'POST':
        user = request.form['username']
        return redirect(url_for('auth.calendar', usr=user)) # routes to calendar of user upon successful authentication
    else: 
        return render_template('login.html')

@auth.route('/<usr>') # should be routed properly to user's profile
def user(usr):
    return render_template('profile.html')

@auth.route('/profile')
def profile():
    return render_template('profile.html')

@auth.route('/signup') 
def signup():
    return render_template('signup.html')

@auth.route('/calendar')
def calendar():
    return render_template('calendar_events.html')

>>>>>>> c1daa13c026cdd946bd8e6e9a09f8e91c83910e4
