from flask import Flask, Blueprint, render_template, redirect, url_for, request, session, flash, jsonify
from datetime import timedelta
from . import db
import sqlite3
import os
import jyserver.Flask as jsf
import json

auth = Blueprint('auth', __name__)




@auth.route('/') # login page when you enter the site
def index():  

    return render_template('login.html')
    


@auth.route('/login', methods=['POST', 'GET']) # POST request to authenticate user
def login():
    # print(url_for('auth.login'))

    if request.method == 'POST' and request.form['submit_button'] =="Login":
        # print("LOGIN BUTTON IS PRESSED")

        # print(request.form['submit_button'])
        user = request.form['employee_name']
        password = request.form['employee_password']
        # print(user)
        # print(password)
    
        # print("Employee ID is :", user)

        ## CONNECT DATABASE     
        currentdirectory = os.path.dirname(os.path.abspath(__file__))
        # print("NOW WE ARE IN:" , currentdirectory)
        connect_directory = currentdirectory + "\pythonsqlite.db"
        # print(connect_directory)
        connection = sqlite3.connect(connect_directory)
        cursor = connection.cursor()

        
        ## CHECK IF Employee ID EXIST
        query = "SELECT EXISTS (SELECT * FROM employee_details WHERE employee_name =?)"
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
                
                query_employee = "SELECT * FROM employee_details WHERE employee_name = ?"
                # print(query1)
                result = cursor.execute(query_employee, (user,))
                row = result.fetchall()
                # print(row[0])
                session['user_information'] = row[0] # storing information in the session
                # print("session VARIABLE:", session['user_information'])
                user_information = session['user_information']
                # print(type(user_information))
                user_information = json.dumps(row[0])
                # print(type(user_information))
                
                user_information = json.loads(user_information)
                # print(user_information)
                # print(type(user_information))
                

                # return render_template('profile.html')
                return redirect(url_for('auth.calendar'))
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

    elif request.method == 'POST' and request.form['submit_button'] =="Signup":
        return render_template('signup.html')


@auth.route('/signup', methods=['POST', 'GET']) 
def signup():
    # print("SIGNUP BUTTON IS PRESSED")
    if request.method == 'POST':        
        
        # employee_id = request.form['employee_id']
        employee_name = request.form['employee_name']
        employee_position = request.form['employee_position']
        # employee_email = request.form['employee_email']
        # employee_phone = request.form['employee_phone']
        employee_password = request.form['employee_password']
        tuple_of_employee_details = (employee_name,employee_position,employee_password)


        
        # # print("employee_id is :", employee_id)
        # print("employee_name is :", employee_name)
        # print("employee_position is :", employee_position)
        # # print("employee_email is :", employee_email)
        # # print("employee_phone is :", employee_phone)
        # print("employee_password is :", employee_password)
        
        
        
       
        
        

        ## CONNECT DATABASE     
        currentdirectory = os.path.dirname(os.path.abspath(__file__))
        # print("NOW WE ARE IN:" , currentdirectory)
        connect_directory = currentdirectory + "\pythonsqlite.db"
        # print(connect_directory)
        connection = sqlite3.connect(connect_directory)
        cursor = connection.cursor()

        ## Check if employee_name is unique in DB
        query = "SELECT EXISTS (SELECT * FROM employee_details WHERE employee_name =?)"
        result = cursor.execute(query, (employee_name,))
        row = result.fetchall()
        value_exist = row[0][0]
        # print("employee_name exists:", value_exist)

        if value_exist ==1:
            return render_template('signup.html',employee_name_exists="True")


        ## IF GOT EMPTY FIELDS, TELL THEM TO FILL IN AGAIN
        for each in tuple_of_employee_details:
            if each == '':
                return render_template('signup.html', details_not_filled = True, employee_name=employee_name,employee_position=employee_position,employee_password=employee_password)


        ## INSERT VALUES INTO DATABASE
        sql = """INSERT INTO employee_details(employee_name,employee_position,employee_password)
                VALUES(?,?,?)"""

        cursor.execute(sql, tuple_of_employee_details)
        connection.commit()

        # print("insert successful")
        return render_template('login.html', signup_completed= True)

    return render_template('signup.html')


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
    
    user_information = session['user_information']

    return render_template('profile.html', user_information=user_information)





@auth.route('/calendar')
def calendar():
    # print(url_for('auth.calendar'))
    # print(url_for('static', filename="calendar_events_2_stuff/test.js"))
    # print(url_for('auth.calendar', filename="muahaaahah.js"))


    ## Retrieve list of values for leave approved
    currentdirectory = os.path.dirname(os.path.abspath(__file__))
    connect_directory = currentdirectory + "\pythonsqlite.db"
    connection = sqlite3.connect(connect_directory)
    cursor = connection.cursor()

    
    ## OBTAIN LEAVE APPLICATIONS
    query = "SELECT * FROM leave_application"
    # query = "SELECT json_group_object(employee_name, json_object('employee_position',employee_position,'employee_password',employee_password)) AS json_result FROM (SELECT * FROM employee_details)"
    result = cursor.execute(query)
    rows = result.fetchall()
    leave_applications = rows
   
    ## OBTAIN Employee Details

    query = "SELECT employee_name, employee_position FROM employee_details"
    result = cursor.execute(query)
    rows = result.fetchall()
    employee_details = rows
    print(employee_details)
    

    return render_template('calendar.html', leave_applications = leave_applications, employee_details = employee_details)

