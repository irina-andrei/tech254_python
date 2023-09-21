# A script that put a new, blank file in a directory.


import os


print(f"This is the current directory (folder): {os.getcwd()}")
# Telling the user the current location.

choice = input("Do you want to create the new file in the current directory? Y/N: ").lower()

if choice == 'n':
    new_location = input("Please enter the new location desired: ")
    os.chdir(new_location)
    # This will change the directory to the one specified by the user.

name_choice = input("Enter the name of the new file (remember to add .txt or other extension): ")
f = open(name_choice, "w")

print(f"File '{name_choice}' created successfully.")
