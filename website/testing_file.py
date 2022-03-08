import datetime;
time_now = datetime.datetime.now()
import os
import sqlite3
import json


currentdirectory = os.path.dirname(os.path.abspath(__file__))
connect_directory = currentdirectory + "\pythonsqlite.db"
connection = sqlite3.connect(connect_directory)
cursor = connection.cursor()


## OBTAIN LEAVE APPLICATIONS
# query = "SELECT * FROM leave_application"
query = "SELECT * from employee_details"
result = cursor.execute(query)
rows = result.fetchall()
leave_applications = rows
# print(leave_applications)
# print(value_exist)
# leave_applications = json.dumps(leave_applications)
# leave_applications = jsonify(leave_applications)
# leave_applications = {'firstname':'Harry','lastname':'Potter'}
# print(leave_applications)
# print(type(leave_applications))
print(leave_applications)

dct = dict(leave_applications)
print(dct)

