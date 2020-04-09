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

    return "failure"

# returns "success" or "failure"
def login(email, password):
    print("login attempt: ", email, password)
    # interface with SQL here
    print("created: ", email, password)
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

    return ["a", "b"]

# returns "success" or "failure"
def add_contact_info(email, value):
    print("add contact: ", email, value)
    # interface with SQL here
    # NEED TYPE
    connection = create_connection()
    cursor = connection.cursor()
    sql = ''' INSERT INTO ContactMethod(email, password, Event_id)
              VALUES(?,?,?) '''
    values = (email, value)
    cursor.execute(sql, values)
    connection.commit()
    connection.close()
    return "failure"

# returns "success" or "failure"
def delete_contact_info(email, value):
    print("delete ", email, value)
    # interface with SQL here
    # NEED TYPE (Maybe)
    connection = create_connection()
    cursor = connection.cursor()
    sql = 'DELETE FROM ContactMethod WHERE id = ? AND info = value'
    values = (email, value)
    cursor.execute(sql, values)
    connection.commit()
    connection.close()

    return "failure"

# returns "success" or "failure"
def update_contact_info(email, oldval, newval):
    print("update attempt: ", email, oldval, newval)

    # interface with SQL here
    connection = create_connection()
    cursor = connection.cursor()
    sql = ''' UPDATE ContactMethod
              SET info = ?
              WHERE id = ? AND info = ?'''
    values = (newval, email, oldval)
    cursor.execute(sql, values)
    connection.commit()
    connection.close()
    return "failure"

def create_connection():

    connection = None
    try:
        connection = sqlite3.connect('sql_database.db')
    except Error as error:
        print(error)
    return connection
