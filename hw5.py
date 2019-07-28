#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 21:45:38 2019

@author: karlahirokawa

Foundations Homework 5: Lists and Dictionaries

Creating a home inventory priority list, where the {task: priority} is stored in
a dictionary and the dictionary is modified based on user input and if/elif/else
menu options.

Modified from hw5_template
"""

#Todo.txt file location
infile = "/Users/grantraupp/Desktop/Coding/Foundations_2019/Todo.txt"

# read in ToDo.txt here using readlines. Reads in as a list.
with open(infile, 'r') as todo_file:
    lines = todo_file.readlines()
    #print(lines)
  

# create empty dictionary to store data as we loop 
task_dict = {}
    
for line in lines:
    task = line.split(",")[0] #split the line and pull out task by index
    if "\n" in task:
        task = task.strip("\n") #removes any carriage returns
    priority =  line.split(",")[1] #split the line and pull out prority by index
    if "\n" in priority:
        priority = priority.strip("\n") #removes any carriage returns
    
    task_dict[task] = priority # add new key:value pairs to dictionary 

#print(task_dict)


while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()#adding a new line

    # Choice 1 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # loop through the dictionary here and print items
        for key, value in task_dict.items():
            print(key,value)
        input("Press enter to return to menu.")
        
    # Choice 2 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        # add a new key, value pair to the dictionary
        new_task = input("Enter new task: ")
        new_task = new_task.title() #Make new_task title case to match homework formatting. 
        new_priority = input("Enter new task's priority: ")
        new_priority = new_priority.lower() #Make new_priority lower case to match homework formatting.
        
        #Prevent user from adding task if the task already exists in the Table.
        if new_task in task_dict: 
            input("This task already exists in file. Press enter to return to menu.")
        else: #Add a new task:priority
            task_dict[new_task] = new_priority
            print("You have added", new_task, new_priority, "to the file.")
            print("Your current data is:")
            for key, value in task_dict.items():
                print(key, value)
            input("Press enter to return to menu.")
    
    # Choice 3 - Remove a new item from the list/Table
    elif(strChoice == '3'):
        remove_key = input("Enter the task name to remove: ")
        remove_key = remove_key.title() #Use title case to match homework formatting
        # locate key and delete it using del function
        if remove_key in task_dict: #Make sure task to delete exists in Table
            del task_dict[remove_key]
            print("You have deleted", remove_key, "from the list.")
            print("Your current data is:")
            for key, value in task_dict.items():
                print(key, value)
            input("Press enter to return to menu.")
        else: #Message to print if task to delete is not in Table
            input("This task is not in the file. Press enter to return to menu.")
   
    # Choice 4 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        # loop through key, value and write to file
        todo_output = [] #formatting for txt file
        for pair in task_dict.items():
            todo_format = "{task},{priority}\n".format(task=pair[0], priority=pair[1])
            todo_output.append(todo_format)
        with open (infile, "w") as f: #open and write to txt file
            f.writelines(todo_output)
        
        print("The following data has been saved to 'ToDo.txt':")
        for key, value in task_dict.items():
            print(key, value)
    
    # Choice 5 - save data and end the program
    elif (strChoice == '5'):
        # loop through key, value and write to file
        todo_output = [] #formatting for txt file
        for pair in task_dict.items():
            todo_format = "{task},{priority}\n".format(task=pair[0], priority=pair[1])
            todo_output.append(todo_format)
        with open (infile, "w") as f: #open and write to txt file
            f.writelines(todo_output)
        
        print("Your file 'ToDo.txt' contains the following tasks:")
        for key, value in task_dict.items():
            print(key, value)
        print("Exiting program.")
        break #and Exit the program
            
#Questions
print("Questions: None this week.")
                