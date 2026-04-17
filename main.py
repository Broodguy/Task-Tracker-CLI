from datetime import date, datetime
import json
import shlex

print("Welcome to the Task Tracker CLI!")

print("\n\nCommands: ")
print("\tadd *task name* - Add a new task")
print("\tupdate *task id* *new task name* - Update an existing task")
print("\tdelete *task id* - Delete a task")
print("\tmark *task id* *new state* - Mark a task as busy or done")
print("\tlist *state* - List tasks by state (busy, done, nothing = all)")
print("\texit - Exit the application")

def main():
    while True:
        command = input("\ntask-cli ")
        
        split_command = shlex.split(command)
        args_amount = len(split_command)
        needed_args = {
            "add": 2,
            "update": 3,
            "delete": 2,
            "mark": 3,
            "list": 2,
            "exit": 1
        }
        
        #check if the command is valid
        if needed_args.get(split_command[0]) is None:
            print("Invalid command. Please try again.")
            continue

        #check if the command has the correct number of arguments
        if args_amount < needed_args.get(split_command[0]):
            print(f"Too few arguments for command '{split_command[0]}'. Please try again.")
            continue

        #choose which command to execute
        match split_command[0]:
            case "add":
                add_task(split_command[1])
            
            case "update":
                update_task(split_command[1], split_command[2])
            
            case "delete":
                delete_task(split_command[1])

            case "mark":
                mark_task(split_command[1], split_command[2])
            
            case "list":
                list_tasks(split_command[1])
            
            case "exit":
                print("Exiting the application. Goodbye!")
                return
            
            case _:
                print("Unknown command. Please try again.")


def add_task(task_name):
 
    tasks = []
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        pass

    new_task = {
        "id": get_id(),
        "name": task_name,
        "state": "busy",
        "created_at": datetime.now().today().isoformat(),
        "updated_at": datetime.now().today().isoformat()
    }
    
    tasks.append(new_task)
    
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

def update_task(task_id, new_task_name):
    # Logic to update a task
    pass

def delete_task(task_id):
    # Logic to delete a task
    pass

def mark_task(task_id, new_state):
    # Logic to mark a task
    pass

def list_tasks(state=None):
    # Logic to list tasks
    pass


def get_id():
    return 0

main()