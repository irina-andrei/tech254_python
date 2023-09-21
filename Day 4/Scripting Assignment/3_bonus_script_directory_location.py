# A script that will create a directory.
# The user enters the name of the directory.
# The user can also specify where the directory will be made.


import os

print(f"This is the current directory (folder): {os.getcwd()}")
# Telling the user the current location.

user_choice = input("Please enter the name of the new directory: ")
choice = input("Do you want to create it in the current directory? Y/N: ").lower()

if choice == 'n':
    new_location = input("Please enter the new location desired: ")
    os.chdir(new_location)
    # This will change the directory to the one specified by the user.

os.mkdir(user_choice)
# This will create a directory named by the user in the current folder.

print(f"Directory '{user_choice}' created successfully.")
