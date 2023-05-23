#!/usr/bin/python3
"""
A extend your Python script to export data in the JSON format,
Using what you did in the task #0.
Requirements:
Records all tasks that are owned by this employee
Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
File name must be: USER_ID.json
"""
import json
import re
import requests
import sys


API = "https://jsonplaceholder.typicode.com"
"""REST API url for prototyping"""

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            user_res = requests.get('{}/users/{}'.format(API, id)).json()
            todos_res = requests.get('{}/todos'.format(API)).json()
            user_name = user_res.get('username')
            todos = list(filter(lambda x: x.get('userId') == id, todos_res))
            with open("{}.json".format(id), 'w') as json_file:
                user_data = list(map(
                    lambda x: {
                        "task": x.get("title"),
                        "completed": x.get("completed"),
                        "username": user_name
                    },
                    todos
                ))
                user_data = {
                    "{}".format(id): user_data
                }
                json.dump(user_data, json_file)
