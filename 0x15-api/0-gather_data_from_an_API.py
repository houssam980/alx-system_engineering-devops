#!/usr/bin/python3
"""given employee ID"""


import requests
import sys



if __name__ == "__main__":
    userID = sys.argv[1]
    usr = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userID))

    name = usr.json().get('name')
    all = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = 0
    completefTask = 0

    for task in all.json():
        if task.get('userId') == int(userID):
            tasks += 1
            if task.get('completed'):
                completefTask += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completefTask, tasks))

    print('\n'.join(["\t " + task.get('title') for task in all.json()
          if task.get('userId') == int(userID) and task.get('completed')]))
