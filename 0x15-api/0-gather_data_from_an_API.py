#!/usr/bin/python3

"""
Python script that, using a REST API
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    url = get('https://jsonplaceholder.typicode.com/todos/')
    info = url.json()
    completed = 0
    total = 0
    tasks = []
    response = get('https://jsonplaceholder.typicode.com/users')
    data = response.json()

    for j in data:
        if j.get('id') == int(argv[1]):
            emp = j.get('name')

    for j in info:
        if j.get('userId') == int(argv[1]):
            total += 1

            if j.get('completed') is True:
                completed += 1
                tasks.append(j.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(emp, completed,
                                                          total))

    for i in tasks:
        print("\t {}".format(i))
