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
        
        args_amount = len(command.split())
        needed_args = {
            "add": 2,
            "update": 3,
            "delete": 2,
            "mark": 3,
            "list": 2,
            "exit": 1
        }
        
        #check if the command is valid
        if needed_args.get(command.split()[0]) is None:
            print("Invalid command. Please try again.")
            continue

        #check if the command has the correct number of arguments
        if args_amount < needed_args.get(command.split()[0]):
            print(f"Too few arguments for command '{command.split()[0]}'. Please try again.")
            continue

        #choose which command to execute
        match command.split()[0]:
            case "add":
                add_task(command.split()[1])
            
            case "update":
                update_task(command.split()[1], command.split()[2])
            
            case "delete":
                delete_task(command.split()[1])

            case "mark":
                mark_task(command.split()[1], command.split()[2])
            
            case "list":
                list_tasks(command.split()[1])
            
            case "exit":
                print("Exiting the application. Goodbye!")
                return
            
            case _:
                print("Unknown command. Please try again.")

def add_task(task_name):
    # Logic to add a task
    pass

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

main()