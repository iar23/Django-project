import requests
import jsonURL = 'http://127.0.0.1:8000/api/'
# get data
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    jdata = json.dumps(data)
    r = requests.get(url=URL, data=jdata)
    data = r.json()
    print(data)
# Run 
get_data()