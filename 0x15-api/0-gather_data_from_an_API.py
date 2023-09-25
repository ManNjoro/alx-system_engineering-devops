#!/usr/bin/python3
import requests
import sys

res = requests.get('https://jsonplaceholder.typicode.com/todos').json()
users = requests.get('https://jsonplaceholder.typicode.com/users/').json()
id = int(sys.argv[1])
completed = 0
name = ""
tasks = 0
title = ""
for i in res:
    if i.get('userId') == id and i.get('completed') is True:
        completed += 1
        title += f"{i['title']}\n\t"
    if i.get('userId') == id:
        tasks += 1
for i in users:
    if i.get('id') == id:
        name = i.get('name')
print("Employee {} is done with tasks ({}/{}):\n\t{}".format(
    name, completed, tasks, title), end="")
