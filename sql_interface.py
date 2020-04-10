import sqlite3
from sqlite3 import Error

# will create the user return "success" or "failure"
def create_user(email, password):
    # interface with SQL here
    print("created: ", email, password)
    connection = create_connection()
    cursor = connection.cursor()
    # Change when putting in Events
    sql = ''' INSERT INTO User(email, password, Event_id)
              VALUES(?,?,?) '''

    user = (email, password, " ")
    cursor.execute(sql, user)
    connection.commit()
    connection.close()

    # return "failure"
    return "success"

# returns "success" or "failure"
def login(email, password):
    print("login attempt: ", email, password)
    # interface with SQL here
    connection = create_connection()
    cursor = connection.cursor()
    # Change when putting in Events
    sql = "SELECT * FROM User WHERE email = ? AND password=?"
    user = (email, password)
    cursor.execute(sql, user)
    result = cursor.fetchone()
    connection.close()
    if result == None:
        return "failure"
    else:
        return "success"


# returns contact info in a list
def contact_info(email):
    print("contacts ", email)
    # interface with SQL here
    sql = "SELECT * FROM ContactMethod WHERE User_username = ?"
    connection = create_connection()
    connection.row_factory = lambda cursor, row: row[2]
    cursor = connection.cursor()
    result = cursor.execute(sql, (email,)).fetchall()
    connection.close()
    return result

# returns "success" or "failure"
def add_contact_info(email, value):
    #print("add contact: ", email, info)
    # interface with SQL here
    # NEED TYPE
    connection = create_connection()
    cursor = connection.cursor()

    if cursor.execute("SELECT * FROM User WHERE email = ?", (email,)).fetchall() == None:
        return "failure"

    sql = ''' INSERT INTO ContactMethod(User_username, type, info)
              VALUES(?,?,?) '''
    values = (email, "Account Type", value)
    cursor.execute(sql, values)
    connection.commit()
    connection.close()
    return "success"

    # return "failure"

# returns "success" or "failure"
def delete_contact_info(email, info):
    print("delete ", email, info)
    # interface with SQL here
    # NEED TYPE (Maybe)
    connection = create_connection()
    cursor = connection.cursor()
    sql = 'DELETE FROM ContactMethod WHERE User_username = ? AND info = ?'
    values = (email, info)
    cursor.execute(sql, values)
    connection.commit()
    connection.close()
    return "success"
    # return "failure"

# returns "success" or "failure"
def update_contact_info(email, oldval, newval):
    print("update attempt: ", email, oldval, newval)

    # interface with SQL here
    connection = create_connection()
    cursor = connection.cursor()
    sql = ''' UPDATE ContactMethod
              SET info = ?
              WHERE User_username = ? AND info = ?'''
    values = (newval, email, oldval)
    cursor.execute(sql, values)
    connection.commit()
    connection.close()
    return "success"
    # return "failure"

def create_connection():

    connection = None
    try:
        connection = sqlite3.connect('sql_database.db')
        # connection = sqlite3.connect('sql_database2.db')
    except Error as error:
        print(error)
    return connection
