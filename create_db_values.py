import sqlite3
from sqlite3 import Error


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
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO employee_details(employee_id,employee_name,employee_position,employee_email,employee_phone,employee_password)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, employee)
    conn.commit()
    # return cur.lastrowid


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
    database = r"C:\sqlite\db\pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        employee1 = ('1353654','Ong Zheng Jie', 'BOSS', 'zjong.2019@scis.smu.edu.sg', 88138399,'password123');
        employee2 = ('1353655','Chee Jay Sian', 'BOSS', 'jayjay@boiboi.com', 91919235,'password456');
        create_employee(conn, employee1)
        create_employee(conn, employee2)

        # # tasks
        # task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
        # task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')

        # # create tasks
        # create_task(conn, task_1)
        # create_task(conn, task_2)


if __name__ == '__main__':
    main()


