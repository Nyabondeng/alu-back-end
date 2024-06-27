#!/usr/bin/python3

"""
Module
export data in the JSON format
"""

import json
import requests


if __name__ == "__main__":
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users/"

    todos = requests.get(todos_url).json()
    users = requests.get(user_url).json()

    users_list = []
    for user in users:
        users_list.append((user.get('id'), user.get('username')))

    tasks = []
    for todo in todos:
        tasks.append((todo.get('userId'), todo.get('completed'),
                     todo.get('title')))

    output = dict()
    for users in users_list:
        employee = []
        for task in tasks:
            if users[0] == task[0]:
                employee.append({"task": task[2], "completed": task[1],
                                "username": users[1]})
        output[str(users[0])] = employee

    filename = "todo_all_employees.json"
    with open(filename, "w") as f:
        json.dump(output, f, sort_keys=True)
