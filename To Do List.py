"""Simple To Do List Program"""
import json


# Loading the file
def load_file():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

    except FileNotFoundError:
        tasks = []

    return tasks


# Display Tasks
def show_tasks(tasks):
    if not tasks:
        print("No Tasks Yet.")

    else:
        for i, task in enumerate(tasks, 1):
            print(f'{i}. {task}')


# Delete A Task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter Task Number To Delete: "))
        removed_task = tasks.pop(task_num - 1)
        print(f"Removed Task: {removed_task}")

    except (IndexError, ValueError):
        print("Invalid Input.")


# Add A New Task
def add_task(tasks):
    task = input("Enter A New Task: ")
    tasks.append(task)
    print("Task Added.")


# Save Tasks
def save_tasks(tasks):
        with open ("task.json", "w") as file:
            json.dump(tasks, file)



# SIMPLE USER INTERFACE

task_list = load_file()

while True:

    print(f"___To Do List___")
    print('1. Show Tasks.')
    print('2. Add Tasks')
    print('3. Delete Tasks.')
    print('4. Exit.')

    choice = input("Choose an Option: ")

    match choice:
        case "1" :
            show_tasks(task_list)

        case "2" :
            add_task(task_list)

        case "3" :
            delete_task(task_list)

        case "4" :
            save_tasks(task_list)
            print("Good Bye.")
            break

        case _ :
            print("Invalid Input.")

