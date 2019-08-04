#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 22:02:46 2019

@author: karlahirokawa
Foundations Homework 6: Functions

Creating a home inventory priority list, where the {task: priority} is stored
in a dictionary and the dictionary is modified based on user input and menu 
options stored in functions.

Modified from hw6_template
"""

# load data from ToDo.txt
infile = "/Users/grantraupp/Desktop/Coding/Foundations_2019/Todo.txt"

def open_file(filepath):
    '''Opens a file from a provided file path.
    Returns a list of tuples.'''
    lines = []
    with open(filepath, "r") as f:
        lines = f.readlines()
    return lines


def list_to_dict(list_items):
    '''Converts a list of tuples containing two elements into a dictionary. 
    Element 0 is the key, element 1 is the value.
    Returns a dictionary.'''
    new_dict = {}
    
    for line in list_items:
        key = line.split(",")[0].strip()
        value = line.split(",")[1].strip()
        new_dict[key] = value
    return new_dict


def view_items(input_dict):
    '''Displays the contents of a dictionary.'''
    print("Your current data is:")
    for key, value in input_dict.items():
        print(key, value)


def add_task(input_dict, new_key, new_value):
    '''Adds a new key:value pair to a dictionary.
    Returns updated dictionary.'''
    if new_key in input_dict:
        print("\nThis entry already exists in the file. \n")
    else:
        input_dict.update({new_key:new_value})
        print("\nYou have added: ", new_key, new_value, "\n")
        return input_dict


def remove_task(input_dict, task_name):
    '''Removes a key:value pair from a dictionary. First checks to make
    sure key is in the dictionary.
    Returns updated dictionary.'''
    if task_name in input_dict:
        del input_dict[task_name]
        print("\nYou have removed", task_name, "\n")
        return input_dict
    else:
        print("\nThis entry does not exist in the file. \n")


def save_todo(filepath, input_dict):
    '''Saves a dictionary to a provided file path. File is saved in write mode,
    so an existing file will be overwritten. File is formatted
    with one key:value pair per line.'''
    with open (filepath, "w") as f:
        for key, value in input_dict.items():
            f.writelines("{},{}\n".format(key,value))
    print("\nYour data has been saved to:\n", filepath)
        

# Main 
lines = open_file(infile)
task_dict = list_to_dict(lines)

###  menu options ###
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

    # Choice 1 -Show the current items in the table
    if (strChoice.strip() == '1'):
        view_items(task_dict)

    # Choice 2 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):

        # ask user for new task and priority
        new_key = input("Enter a new task name: ").title()
        new_value = input("Enter the new task's priority from low to high: ").lower()
        
        # call function to add a new task to dict
        add_task(task_dict, new_key, new_value)
        view_items(task_dict)
        
    # Choice 3 - Remove an existing item from dictionary
    elif(strChoice == '3'):
        remove_key = input("Enter the task name to remove: ").title()
        
        remove_task(task_dict, remove_key)
        view_items(task_dict)
        
    # Choice 4 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        save_todo(infile, task_dict)
        view_items(task_dict)
         
    # Choice 5- end the program
    elif (strChoice == '5'):
        save_todo(infile, task_dict)
        view_items(task_dict)
        print("\n\nExiting the program")
        break #and Exit the program

print("""
      Question: Will debugging in Sypder be demonstrated in office hours?
      The videos show Pycharm, but I've mostly decided to use Spyder. I've
      gone thru the Spyder documentation, but it would be nice to see it in
      action from someone who knows how to use it.
      """)
