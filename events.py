from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'

app.url_map.strict_slashes = False # Disable redirecting on POST method from /event to /event/

mongo = PyMongo(app)

class Event(Resource):
     def get(self, _id):
        myevent = mongo.db.events
        e = myevent.find_one({'id' : _id})
        if e:
            output = {'id' : e['id'], 'start_time' : e['start_time'], 'duration':e['duration'], 'tags':e['tags']}
        else:
            output = "No such event"
        return jsonify({'id' : e['id'], 'start_time' : e['start_time'], 'duration':e['duration'], 'tags':e['tags']})




class EventList(Resource):
    
    def get(self):
        events = mongo.db.events
        output = []
        for e in events.find():
            output.append ({'id' : e['id'], 'start_time' : e['start_time'], 'duration':e['duration'], 'tags':e['tags']})
        return jsonify({'result' : output})

    

    def post(self):
        events = mongo.db.events
        _id = request.json['id']
        _start_time = request.json['start_time']
        _duration = request.json['duration']
        _tags = request.json['tags']

        output = {'id' : _id, 'start_time' : _start_time, 'duration':_duration, 'tags':_tags}
        event_id = events.insert(output)

        return jsonify({'id' : _id, 'start_time' : _start_time, 'duration':_duration, 'tags':_tags})

    def delete(self):
        events = mongo.db.events
        _id = request.json['id']
        e = events.find_one({'id' : _id})
        if e:
            events.remove({'id' : _id})
            return jsonify({'result' : "Delete successfully"})
        else:
            return jsonify({'result' : "Nothing to delete"})


api.add_resource(EventList, '/event')
api.add_resource(Event, '/event/<string:_id>')

if __name__ == '__main__':
    app.run(debug=True)
