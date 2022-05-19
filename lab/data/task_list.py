

tasks_empty_data = []

tasks_data_set = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

def determine_user_list():
    user_list_option = input("Do you want to load a previously created list, Please type (Y)es or (N)o: ")
    if user_list_option == "Y":
        tasks = tasks_data_set
    elif user_list_option == "N":
        tasks = tasks_empty_data
    return tasks