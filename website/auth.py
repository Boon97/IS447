from flask import Flask, Blueprint, render_template, redirect, url_for, request, session, flash
from datetime import timedelta
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/') # login page when you enter the site
def index():
	return render_template('login.html')



@auth.route('/login', methods=['POST', 'GET']) # POST request to authenticate user
def login():
    if request.method == 'POST':
        user = request.form['username']
        session['user'] = user # storing information in the session
        flash('Login Successful!')
        return redirect(url_for('auth.profile', user=user)) # routes to calendar of user upon successful authentication
    elif 'user' in session:
        flash('Already Logged In!')
        return redirect(url_for('auth.profile'))
    else:    
        return render_template('login.html')



@auth.route('/user') # should be routed properly to user's profile
def user():
    if 'user' in session: # prevents people from logging in simply from modifying the url 
        user = session['user']
        return render_template('profile.html', user=user)
    else: # show this if not logged in
        flash('You are not logged in!')
        return redirect(url_for('auth.login'))



@auth.route('/logout')
def logout(): # removes sessions on logout
    flash('Successfully logged out!', 'info') # flash a message showing logout is successful
    session.pop('user', None)
    return redirect(url_for('auth.login'))


@auth.route('/profile')
def profile():
    return render_template('profile.html')


@auth.route('/signup') 
def signup():
    return render_template('signup.html')


@auth.route('/calendar')
def calendar():
    return render_template('calendar_events.html')

