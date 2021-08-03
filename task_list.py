tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# PROVIDE MENU OPTIONS TO USER



# PRINT OUT ALL INCOMPLETE TASKS
def incomplete_tasks():
    for task in tasks:
        if task["completed"] == False:
            print(task)
# print("Here are the incomplete tasks...")
# incomplete_tasks()

# PRINT OUT ALL COMPLETE TASKS
def complete_tasks():
    for task in tasks:
        if task["completed"] == True:
            print(task)
# complete_tasks()

# PRINT OUT ALL TASK DESCRIPTIONS
def task_descriptions():
    for task in tasks:
        print(task["description"])
# task_descriptions()

# PRINT TASKS THAT TAKE AT LEAST 15 MINUTES
def long_tasks():
    for task in tasks:
        if task["time_taken"] >= 15:
            print(task)
print("Here are the tasks that take at least 15 minutes...")
# long_tasks()

# PRINT TASKS WITH A GIVEN DESCRIPTION
def task_search_result():
    description_search = input("Enter a Task Description to start search: ")
    task_in_list = False
    for task in tasks:
        if description_search == task["description"]:
            task_in_list = True
            description_search_result = task
    if task_in_list == True: 
        print(description_search_result)
    else:
        print(f"Sorry we don't have {description_search} on the list")
# task_search_result()

# MARK TASK AS COMPLETE WITH A GIVEN DESCRIPTION
def task_completer():
    update_request = input("What task have you completed?: ")
    update_request_valid = False
    update_selection = None
    for task in tasks:
        if update_request == task["description"]:
            update_request_valid = True
            update_selection = task
    if update_request_valid == True:
        update_selection["completed"] = True
# task_completer()

# ADD TASK TO LIST
def add_task():
    task_description = input("Enter the task description: ")
    task_length = input("Enter the time the task will take: ")
    task_addition = {"description": task_description, "completed": False, "time_taken": task_length}
    tasks.append(task_addition)
# add_task()