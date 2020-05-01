import requests


url = "http://127.0.0.1:5001/event"

def create_event(data):
    idx, st, duration, tags = data[idx], data[st], data[duration], data[tags]

    params = {'id':idx, 'start_time':st, 'duration':duration, 'tags':tags}

    r = requests.post(url=url, params=params)

    data = r.json()

    print(data)

def get_all_events():
    r = requests.get(url=url)
    print(r.json())
