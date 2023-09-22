import json
import os


parsed_json = json.loads(open("example_json.json").read())

print(f"This is the current directory (folder): {os.getcwd()}")
# Telling the user the current location.

name_choice = "example_json.json"
# This will be the standard file that will be opened.

choice = input("Do you want to open 'example_json.json' in the current directory? Y/N: ").lower()

if choice == 'n':
    new_location = input("Please enter the new directory location desired: ")
    os.chdir(new_location)
    # This will change the directory to the one specified by the user.

    name_choice = input("Enter the name of the new json (remember to add '.json'): ")
    # This will get the new .json file name from the user.

print(f"\nOpening '{name_choice}'...\n")

parsed_json = json.loads(open("example_json.json").read())

for key, value in parsed_json.items():
    print(key, ": ", value)
    # This will print every item in the json file.