import sqlite3
from sqlite3 import Error
import datetime;
time_now = datetime.datetime.now()


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_employee(conn, employee):
    sql = ''' INSERT INTO employee_details(employee_id,employee_name,employee_position,employee_email,employee_phone,employee_password)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, employee)
    conn.commit()
    # return cur.lastrowid

def create_leave_application(conn, leave_application):
    
    sql = ''' INSERT INTO leave_application(application_id,applicant_id,leave_start_date,leave_end_date,leave_am_pm_both,leave_reason, leave_application_timestamp, leave_number_of_days,leave_approved)
            VALUES(?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, leave_application)
    conn.commit()

def create_leave_approval(conn, leave_approval):
    
    sql = ''' INSERT INTO leave_approval(application_id,leave_approver_id,leave_approved,leave_approval_timestamp,reason_if_rej)
            VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, leave_approval)
    conn.commit()

# def create_task(conn, task):
#     """
#     Create a new task
#     :param conn:
#     :param task:
#     :return:
#     """

#     sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
#               VALUES(?,?,?,?,?,?) '''
#     cur = conn.cursor()
#     cur.execute(sql, task)
#     conn.commit()
#     return cur.lastrowid


def main():
    database = r".\website\pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a employee_details
        employee1 = ('1353654','Ong Zheng Jie', 'Junior', 'zjong.2019@scis.smu.edu.sg', 88138399,'password123');
        employee2 = ('1353655','Chee Jay Sian', 'Senior', 'jayjay@boiboi.com', 91919235,'password456');
        employee_list = (employee1,employee2)
        for employee in employee_list:
            create_employee(conn,employee)



        # create leave applications
        leave_application_1 = ('1','1353654','123321','1353654','123321','1353654','123321','1353654','123321');
        leave_application_2 = ('2','1353655','123321','1353654','123321','1353654','123321','1353654','123321');
        leave_application_list = (leave_application_1,leave_application_2)
        # print("leave_application_1: ", leave_application_1)
        for each in leave_application_list:
            # print(each)
            create_leave_application(conn,each)


        # create leave approvals
        leave_approval_1 = ('1','1353654','123321',time_now,'123321');
        leave_approval_2 = ('1','1353654','123321',time_now,'123321');
        leave_approval_list = (leave_approval_1,leave_approval_2)
        # print("leave_application_1: ", leave_application_1)
        for each in leave_approval_list:
            # print(each)
            create_leave_approval(conn,each)


        # # tasks
        # task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
        # task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')

        # # create tasks
        # create_task(conn, task_1)
        # create_task(conn, task_2)


if __name__ == '__main__':
    main()


