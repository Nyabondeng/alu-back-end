#!/usr/bin/python3

"""
Module
export data in the JSON format
"""

import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users/"

    todos = requests.get(todos_url).json()
    users = requests.get(user_url).json()

    for user in users:
        if user.get('id') == int(argv[1]):
            user_name = user.get('username')
            break

    tasks = []
    for todo in todos:
        if todo.get('userId') == int(argv[1]):
            tasks.append((todo.get('completed'), todo.get('title')))

    filename = "{}.json".format(argv[1])

    json_list = []
    for task in tasks:
        json_list.append({"task": task[1], "completed": task[0],
                         "username": user_name})

    json_file = {str(argv[1]): json_list}
    with open(filename, 'w') as f:
        json.dump(json_file, f)
