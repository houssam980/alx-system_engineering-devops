#!/usr/bin/python3
"""Exports data in the JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    userID = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(userID))
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    taskLists = []
    todoUsers = {}


    for task in todos:
        if task.get('userId') == int(userID):
            taskDict = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": user.json().get('username')}
            taskLists.append(taskDict)
    todoUsers[userID] = taskLists

    filename = userID + '.json'
    with open(filename, mode='w') as f:
        json.dump(todoUsers, f)
