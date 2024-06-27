#!/usr/bin/python3

"""
Module
"""

import csv
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

    filename = "{}.csv".format(argv[1])
    with open(filename, 'w') as file:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(file, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow({"USER_ID": argv[1], "USERNAME": user_name,
                             "TASK_COMPLETED_STATUS": task[0],
                             "TASK_TITLE": task[1]})
