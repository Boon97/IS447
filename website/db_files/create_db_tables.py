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
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r".\website\pythonsqlite.db"

    sql_create_employee_details_table = """ CREATE TABLE IF NOT EXISTS employee_details (                                        
                                        employee_name text NOT NULL PRIMARY KEY,
                                        employee_position text NOT NULL,                                        
                                        employee_password text NOT NULL
                                    ); """

    sql_create_leave_application_table = """CREATE TABLE IF NOT EXISTS leave_application (
                                    application_id integer PRIMARY KEY,
                                    applicant_name text NOT NULL,                                
                                    leave_start_date text NOT NULL,
                                    leave_end_date text NOT NULL,
                                    leave_am_pm_both text,
                                    leave_reason text NOT NULL,
                                    leave_application_timestamp text NOT NULL,
                                    leave_number_of_days integer NOT NULL,
                                    leave_approved text NOT NULL,
                                    FOREIGN KEY (applicant_name) REFERENCES employee_details (employee_name)
                                );"""

    sql_create_leave_approval_table = """ CREATE TABLE IF NOT EXISTS leave_approval (
                                        application_id text NOT NULL,
                                        leave_approver_name text NOT NULL,
                                        leave_approved text NOT NULL,
                                        leave_approval_timestamp text,
                                        reason_if_rej text,
                                        FOREIGN KEY (application_id) REFERENCES employee_details (leave_application),
                                        FOREIGN KEY (leave_approver_name) REFERENCES employee_details (employee_name)
                                    ); """

    sql_create_admin_table = """ CREATE TABLE IF NOT EXISTS admin (
        employee_name text NOT NULL,
        FOREIGN KEY (employee_name) REFERENCES employee_details (employee_name)
        ); """
                                

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create table
        create_table(conn, sql_create_employee_details_table)

        # create  table
        create_table(conn, sql_create_leave_application_table)

        # create  table
        create_table(conn, sql_create_leave_approval_table)

        # create table 
        create_table(conn,sql_create_admin_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()