#!/usr/bin/python3
"""a given employee ID"""

import requests
import sys

if __name__ == "__main__":

    userID = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(userID))
    name = user.json().get('name')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    total = 0
    completedtask = 0

    for task in todos.json():
        if task.get('userId') == int(userID):
            total += 1
            if task.get('completed'):
                completedtask += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completedtask, total))
    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('userId') == int(userID) and task.get('completed')]))
