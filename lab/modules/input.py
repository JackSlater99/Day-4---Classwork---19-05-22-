
def ask_description():
    description = input("Enter task description to search for: ")
    return description

def ask_duration():
    duration = int(input("Enter task duration: "))
    return duration

def new_task():
    description = input("Enter description: ")
    time_taken = int(input("Enter time taken: "))
    return description, time_taken

def menu_key():
    key = input("Select an option 1, 2, 3, 4, 5, 6, 7, display (m)enu or (q)uit: ")
    return key
