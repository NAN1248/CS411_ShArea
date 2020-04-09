from flask import Flask
from flask import render_template, request, jsonify
import json
import sql_interface as sql_int
import sys

PREFIX = "localhost:5000"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', prefix = PREFIX)

@app.route('/create.html')
def create_html():
    return render_template('create.html', prefix = PREFIX)

@app.route('/login.html')
def login_html():
    return render_template('login.html', prefix = PREFIX)

@app.route('/search.html')
def search_html():
    return render_template('search.html', prefix = PREFIX)

@app.route('/settings.html')
def settings_html():
    return render_template('settings.html', prefix = PREFIX)

@app.route('/events.html')
def events_html():
    return render_template('events.html', prefix = PREFIX)

@app.route('/events')
def events():
    return render_template('events.html', prefix = PREFIX)

@app.route('/create', methods=['POST'])
def create():
    data = json.loads(request.data)
    username = data['username'] + "_name"
    password = data['password']
    return jsonify({
        "username": username
    })

# create user with username and password
@app.route('/create_user', methods=['POST'])
def create_user():
    data = json.loads(request.data)
    email = data['email']
    password = data['password']
    value = sql_int.create_user(email, password)
    return jsonify({
        "value": value
    })

# login
@app.route('/login', methods=['POST'])
def login():
    data = json.loads(request.data)
    email = data['email']
    password = data['password']
    
    value = sql_int.login(email, password)

    return jsonify({
        "value": value
    })
    
# get contact info
@app.route('/contact')
def contact():
    data = json.loads(request.data)
    email = data['email']  
    contact_info = sql_int.contact_info(email)

    return jsonify({
        "contacts": contact_info
    })

# add contact info
# delete contact info
# edit contact info
@app.route('/edit_contact', methods=['POST'])
def edit_contact():
    data = json.loads(request.data)
    email = data['email']
    edit = data['edit'] # either "add", "edit", "delete"
    oldval = data['oldval'] # if add, ""
    newval = data['newval'] # if delete, ""

    if edit == "add":
        value = sql_int.add_contact_info(email, newval)
    elif edit == "delete":
        value = sql_int.delete_contact_info(email, oldval)
    elif edit == "edit":
        value = sql_int.update_contact_info(email, oldval, newval)
    
    return jsonify({
        "value": value
    })


if __name__ == '__main__':
    # add code to startup the sql and nosql databases 
    if sys.platform == "linux":
        PREFIX = "http://127.0.0.1:5000"
    app.run(debug=True)

