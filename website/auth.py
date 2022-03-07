from flask import Flask, Blueprint, render_template, redirect, url_for, request, session, flash
from datetime import timedelta
from . import db
import sqlite3
import os
import jyserver.Flask as jsf

auth = Blueprint('auth', __name__)




@auth.route('/') # login page when you enter the site
def index():  

    return render_template('login.html')
    


@auth.route('/login', methods=['POST', 'GET']) # POST request to authenticate user
def login():
    print("LOGIN BUTTON IS PRESSED")
    print(url_for('auth.login'))

    if request.method == 'POST':        
        user = request.form['username']
        password = request.form['password']
        # print(user)
        # print(password)
       
        print("Username is :", user)

        ## CONNECT DATABASE     
        currentdirectory = os.path.dirname(os.path.abspath(__file__))
        # print("NOW WE ARE IN:" , currentdirectory)
        connect_directory = currentdirectory + "\pythonsqlite.db"
        print(connect_directory)
        connection = sqlite3.connect(connect_directory)
        cursor = connection.cursor()

        
        ## CHECK IF USERNAME EXIST
        query = "SELECT EXISTS (SELECT * FROM employee_details WHERE employee_name=?)"
        result = cursor.execute(query, (user,))
        row = result.fetchall()
        value_exist = row[0][0]
        # print(value_exist)

        if (value_exist == 1):

            ## CHECK IF PASSWORD IS SAME
            query1 = "SELECT employee_password FROM employee_details WHERE employee_name = ?"
            # query1 = "SELECT * FROM employee_details WHERE employee_email = ?"
            # user_email = "zjong.2019@scis.smu.edu.sg"
            # print(query1)
            result = cursor.execute(query1, (user,))
            row = result.fetchall()
            password_returned = row[0][0]
            # print(password_returned)

            if (password == password_returned):
                # flash('Login Successful!')
                session['user'] = user # storing information in the session
                
                return render_template('profile.html', user=user)
                # return redirect(url_for('auth.profile', user=user)) # routes to calendar of user upon successful authentication
            
            else:
                # flash("wrong user_id or password")
                # session["wrong"] = "wronger"
                return render_template('login.html',login_details="True")
        
        ## ASK JUSTIN WHATS THIS
        # elif 'user' in session:
        #     flash('Already Logged In!')
        #     return redirect(url_for('auth.profile'))

        ## If user_id doesn't exist, go back login.html
        else:    
            # flash("wrong user_id or password")
            return render_template('login.html', login_details="True")




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


@auth.route('/signup', methods=['POST', 'GET']) 
def signup():
    print("SIGNUP BUTTON IS PRESSED")
    if request.method == 'POST':        
        employee_id = request.form['employee_id']
        employee_name = request.form['employee_name']
        employee_position = request.form['employee_position']
        employee_email = request.form['employee_email']
        employee_phone = request.form['employee_phone']
        employee_password = request.form['employee_password']
        tuple_of_employee_details = (employee_id,employee_name,employee_position,employee_email,employee_phone,employee_password)

        
        print("employee_id is :", employee_id)
        print("employee_name is :", employee_name)
        print("employee_position is :", employee_position)
        print("employee_email is :", employee_email)
        print("employee_phone is :", employee_phone)
        print("employee_password is :", employee_password)
        
        ## IF GOT EMPTY FIELDS, TELL THEM TO FILL IN AGAIN
        empty_detected = 0
        for each in tuple_of_employee_details:
            if each == '':
                return render_template('signup.html', details_not_filled = True, employee_id = employee_id, employee_name=employee_name,employee_position=employee_position,employee_email=employee_email,employee_phone=employee_phone,employee_password=employee_password)

        
        

        ## CONNECT DATABASE     
        currentdirectory = os.path.dirname(os.path.abspath(__file__))
        # print("NOW WE ARE IN:" , currentdirectory)
        connect_directory = currentdirectory + "\pythonsqlite.db"
        print(connect_directory)
        connection = sqlite3.connect(connect_directory)
        cursor = connection.cursor()

        
        ## INSERT VALUES INTO DATABASE
        sql = """INSERT INTO employee_details(employee_id,employee_name,employee_position,employee_email,employee_phone,employee_password)
                VALUES(?,?,?,?,?,?)"""

        cursor.execute(sql, tuple_of_employee_details)
        connection.commit()

        print("insert successful")
        return render_template('login.html', signup_completed= True)

    return render_template('signup.html')


@auth.route('/calendar')
def calendar():
    print(url_for('auth.calendar'))
    print(url_for('static', filename="calendar_events_2_stuff/test.js"))
    # print(url_for('auth.calendar', filename="muahaaahah.js"))

    return render_template('calendar_events_2_test/calendar_events_2_test.html')

