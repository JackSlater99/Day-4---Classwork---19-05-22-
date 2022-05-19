#import pdb

from modules.task_list import *
from modules.output import *
from data.task_list import *
from modules.input import *

tasks = determine_user_list()

while (True):
    #pdb.set_trace()
    print_menu()
    option = menu_key()
    if (option.lower() == 'q'):
        break
    if option == '1':
        print_list(tasks)
    elif option == '2':
        print_list(get_uncompleted_tasks(tasks))
    elif option == '3':
        print_list(get_completed_tasks(tasks))
    elif option == '4':
        description = ask_description()
        task = get_task_with_description(tasks, description)
        if task is not None:
            mark_task_complete(task)
            print("Task marked complete")
        else:
            print("Task not found")
    elif option == '5':
        time = ask_duration()
        print_list(get_tasks_taking_at_least(tasks, time))
    elif option == '6':
        description = ask_description()
        print(get_task_with_description(tasks, description))
    elif option == '7':
        description = input("Enter description: ")
        time_taken = int(input("Enter time taken: "))
        task = create_task(description, time_taken)
        tasks.append(task)
    else:
        print("Invalid Input - choose another option")



#1, 2, 3, 4, 5, 6, 7, Q