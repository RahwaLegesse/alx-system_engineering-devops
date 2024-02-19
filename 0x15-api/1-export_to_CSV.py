#!/usr/bin/python3

"""
Python script that, using a REST API
"""
from requests import get
from sys import argv
import cs


if __name__ == "__main__":
    url = get('https://jsonplaceholder.typicode.com/todos/')
    info = url.json()
    completed = 0
    total = 0
    tasks = []
    res = get('https://jsonplaceholder.typicode.com/users')
    data = res.json()

    for j in data:
        if j.get('id') == int(argv[1]):
            emp = j.get('name'#!/usr/bin/python3

"""
Python script that exports
"""
from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    url = get('https://jsonplaceholder.typicode.com/todos/')
    info = url.json()

    ro = []
    res = get('https://jsonplaceholder.typicode.com/users')
    data = res.json()

    for j in data:
        if j['id'] == int(argv[1]):
            emp = j['username']

    with open(argv[1] + '.csv', 'w', newline='') as file:
        wt = csv.writer(file, quoting=csv.QUOTE_ALL)

        for j in info:

            ro = []
            if j['userId'] == int(argv[1]):
                ro.append(j['userId'])
                ro.append(emp)
                ro.append(j['completed'])
                ro.append(j['title'])

                wt.writerow(ro)

    for j in info:
        if j.get('userId') == int(argv[1]):
            total += 1

            if j.get('completed') is True:
                completed += 1
                tasks.append(j.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(emp, completed,
                                                          total))

    for j in tasks:
        print("\t {}".format(j))
