#!/usr/bin/python3

"""
Python script
"""

from requests import get
from sys import argv
import json

if __name__ == "__main__":
    url = get('https://jsonplaceholder.typicode.com/todos/')
    info = url.json()

    rw = []
    resp = get('https://jsonplaceholder.typicode.com/users')
    data = resp.json()

    for j in data:
        if j['id'] == int(argv[1]):
            name = j['username']
            idd = j['id']

    rw = []

    for j in info:

        new_dict = {}

        if j['userId'] == int(argv[1]):
            new_dict['username'] = name
            new_dict['task'] = j['title']
            new_dict['completed'] = j['completed']
            rw.append(new_dict)

    final = {}
    final[idd] = rw
    json_obj = json.dumps(final)

    with open(argv[1] + ".json",  "w") as x:
        x.write(json_obj)
