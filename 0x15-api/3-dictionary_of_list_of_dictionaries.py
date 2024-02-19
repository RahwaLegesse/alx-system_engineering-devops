#!/usr/bin/python3

"""
Python script SON format.
"""

from requests import get
import json

if __name__ == "__main__":
    url = get('https://jsonplaceholder.typicode.com/todos/')
    info = url.json()

    rw = []
    url2 = get('https://jsonplaceholder.typicode.com/users')
    data = url2.json()

    new_1 = {}

    for k in data:

        rw = []
        for j in info:

            new_2 = {}

            if k['id'] == j['userId']:

                new_2['username'] = k['username']
                new_2['task'] = j['title']
                new_2['completed'] = j['completed']
                rw.append(new_2)

        new_1[j['id']] = rw

    with open("todo_all_employees.json",  "w") as y:

        json_obj = json.dumps(new_1)
        y.write(json_obj)
