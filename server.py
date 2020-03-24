from flask import Flask
from flask import render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/create', methods=['POST'])
def create():
    data = json.loads(request.data)
    username = data['username'] + "_name"
    password = data['password']
    return jsonify({
        "username": username
    })

if __name__ == '__main__':
    app.run(debug=True)
