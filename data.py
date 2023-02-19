import sqlite3


DATABASE="login.db"

def config() -> None:

    conn=sqlite3.connect('login.db')
    c=conn.cursor()

    c.execute(""" CREATE TABLE creds(
        f_name text,
        l_name text,
        email text,
        password text,
        pass_rep text
        )""")
    print("database created successfully")
    conn.commit()
    conn.close()


def signup_submit(info:list) -> None:
    """
        submits data from sign up page into database.
        Arguments:
            f_name : 0,
            l_name : 1,
            email : 2,
            password : 3,
            pass_rep : 4
    """

    conn=sqlite3.connect(DATABASE)
    c=conn.cursor()

    c.execute('INSERT INTO Account VALUES (:first_name,:middle_name,:last_name,:email,:dob, :gender, :username, :password)',{
        'f_name':info[0],
        'l_name':info[1],
        'email':info[2],
        'password':info[3],
        'pass_rep':info[4]
    })
    print('data submitted successfully')

    conn.commit()
    conn.close()

def retrieve_all() -> list:
    """
        retrieves all data in form of a list.
        [('Fname', 'Lname', 'Email', 'Password', 'Repeat_password', oid)]
    """
    conn= sqlite3.connect(DATABASE)

    c= conn.cursor()

    c.execute("SELECT *, oid FROM Account")

    records= c.fetchall()#[(),()]

    return records

    conn.close()

try:# Creates tables for new host machine.
    config()
except sqlite3.OperationalError:
    pass