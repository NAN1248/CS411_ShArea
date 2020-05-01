import requests


url = "http://127.0.0.1:5001/event"

def create_event(data):
    try:
        idx, st, duration, tags = data['id'], data['start_time'], data['duration'], data['tags']
    except KeyError:
        return "failure"

    params = {'id':idx, 'start_time':st, 'duration':duration, 'tags':tags}

    r = requests.post(url=url, params=params)
    return "success"

    #data = r.json()

    #print(data)

def get_all_events():
    r = requests.get(url=url)
    #print(r)
    return r.json()
