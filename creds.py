import sqlite3


# Creating a data table
def cred():
    conn=sqlite3.connect('student.db')
    c=conn.cursor()

    c.execute(""" CREATE TABLE Students(
        f_name text,
        l_name text,
        RollNo integer PRIMARY KEY,
        Gender text,
        Email text,
        address text,
        Nationality text,
        DOB date,
        POB text,
        Phone_num int
        )""")
    print("database created successfully")
    conn.commit()
    conn.close()
