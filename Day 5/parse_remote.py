import urllib.request
import json


with urllib.request.urlopen("http://jsonplaceholder.typicode.com/todos/1") as url:
    data = json.load(url)
    print(data)
