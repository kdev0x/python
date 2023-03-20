                                           #requarments
# Project: To-Do List Application
# The goal of this project is to create a simple application that helps the user manage their to-do list. The application should have the following features:
# 1. Task input: The user should be able to enter the tasks they need to complete.done
# 2. Task display: The user should be able to view a list of all the tasks they have entered.done
# 3. Task completion: The user should be able to mark a task as complete.
# 4. Task deletion: The user should be able to delete a task from the list.
# 5. Task prioritization: The user should be able to assign a priority level (high, medium, low) to each task, and the tasks should be displayed in order of priority.
# 6. Saving and loading data: The application should save the data entered by the user to a file, so that it can be loaded later.
# To fulfill these requirements, you will need to use the following Python concepts and features:
# * Variables and data types (e.g. integers, strings, lists)
# * Input and output (e.g. using the input function and printing results)
# * Control structures (e.g. if statements, loops)
# * Functions and modules
# * File input/output (e.g. using the open and write functions)
# * Data structures (e.g. lists, dictionaries)
#code :
import os
import pickle

loaded_data=[]
taskes_high_priority = []
task_medium_prioriy = []
task_low_priority = []
all_task = []
while True:
    options = input("what do you want to do enter as a task or veiw youre taskes or mark a task as complete if you want to stop the app press q :")
    if options == "q":
         print("Thank you for using the app i hope you had a great time")
         break
    if options == "enter a new task":
          priority = input ("Is the task high priority or medium priority or low priority    :")
          if priority == "high":
               high_priority_task = input ("what is the task that you want to add")
               taskes_high_priority.append(high_priority_task)
               all_task.append(high_priority_task)
          if priority == "medium":
                medium_priority_task = input ("what is the task that you want to add")
                task_medium_prioriy.append(medium_priority_task)
                all_task.append(medium_priority_task)
          if priority == "low":
                low_priority_task = input ("what is the task that you want to add")
                low_priority_task.append(low_priority_task)
                all_task.append(low_priority_task)  
          elif priority == "q":
             print("Thank you for using the app i hope you had a great time")
             break             
          

    if options == "veiw taskes":
      veiw_task_priortey = input ("what taskes do you want to veiw all taskes or high priorty taskes or medium priorty taskes or low priorty task")
      if veiw_task_priortey == "all taskes":
           print(all_task)
      elif veiw_task_priortey == "high priorty taskes":
           print (high_priority_task)
      elif veiw_task_priortey == "medium priorty taskes":
           print(medium_priority_task)
      elif veiw_task_priortey == "low priorty taskes":
           print(low_priority_task)
      else:
           raise ValueError ("sorry we dont have", veiw_task_priortey,"please enter a neiw value")
    elif options == "mark a task as complete":
        complete_task_number = 0
        complete_task_number = int(input("witch task do you want to mark as complete    :"))
        complete_task_number = complete_task_number - 1
        del all_task[complete_task_number]
    else:
         raise ValueError ("sorry we dont have this option avalible please add a other one")
data_file = "data.txt"
if os.path.exists(data_file):
    with open(data_file, "rb") as file:
        loaded_data = pickle.load(file)
# Save tasks to the file:

