
# Functions to complete:

## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    uncompleted_tasks = []
    for task in list:
        if task["completed"] == False:
            uncompleted_tasks.append(task)
    return uncompleted_tasks

#print(get_uncompleted_tasks(tasks))

## Get a list of completed tasks
def get_completed_tasks(list):
    completed_tasks = []
    for task in list:
        if task["completed"] == True:
            completed_tasks.append(task)
    return completed_tasks

#print (get_completed_tasks(tasks))
    

## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    atleast_time_tasks = []
    for task in list:
        if task["time_taken"] >= time:
            atleast_time_tasks.append(task)
    return atleast_time_tasks

#print (get_tasks_taking_at_least(tasks, 10))

## Find a task with a given description
def get_task_with_description(list, description):
    for task in list:
        if task["description"] == description:
            return task

#print(get_task_with_description(tasks, "Wash Dishes"))

# Extention (Function): 

## Get a list of tasks by status
# def get_tasks_by_status(list, status):
#     list_tasks = []
#     for task in list:
#         if task["completed"] == status:
#             list_tasks.append(task["description"])
#     if status == True:
#         print("The completed tasks are: " + (', '.join(list_tasks)))
#     else:
#         print("The uncompleted tasks are: " + (', '.join(list_tasks)))
        
#get_tasks_by_status(tasks, True)

def mark_task_complete(task):
    task["completed"] = True

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task



