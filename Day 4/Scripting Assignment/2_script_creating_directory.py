# A script that will create a directory.
# The user enters the name of the directory.

import os


user_choice = input("Please enter the name of the new directory (folder): ")
os.mkdir(user_choice)
# This will create a directory named by the user in the current folder.

print(f"Directory '{user_choice}' created successfully.")
