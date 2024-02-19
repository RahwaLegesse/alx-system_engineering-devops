#!/usr/bin/python3

"""
Python script.
"""

from requests import get
import json

if __name__ == "__main__":
    url= get('https://jsonplaceholder.typicode.com/todos/')
    info = url.json()

    rw = []
    resp = get('https://jsonplaceholder.typicode.com/users')
    data = resp.json()

    new = {}

    for i in data:

        rw = []
        for j in info:

            new2 = {}

            if i['id'] == j['userId']:

                new2['username'] = i['username']
                new2['task'] = j['title']
                new2['completed'] = j['completed']
                rw.append(new2)

        new[i['id']] = rw

    with open("todo_all_employees.json",  "w") as x:

        json_obj = json.dumps(new)
        x.write(json_obj)
