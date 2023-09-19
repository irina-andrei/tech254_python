# A Python program that stores usernames and passwords and allows users to change their passwords.


# Some formatting shortcuts:
RED = '\033[31m'
GREEN = '\033[92m'
BLUE = '\033[94m'
PINK = '\033[95m'
CYAN = '\033[96m'
UNDERL = '\033[4m' # 'Underline'
ENDC = '\033[0m' # Removes all formatting applied.
EM = f"{RED}‼{ENDC}" # 'Exclamation Mark' shorthand

my_users = {
    "admin": "adm1n",
    "coco": "C0C0",
    "timmy": "timtim",
    "roger": "rogerroger",
    "max": "Maximus",
    "sydney": "happydays"}
# A dictionary that will hold usernames and passwords.

while True:
    menu = input(f'''
        {PINK}╔{'═'*45}╗
        ║{ENDC} Please select one of the following options: {PINK}║
        ║ *{CYAN} 1 {ENDC}- Retrieve password via username {PINK}{' '*7}║
        ║ *{CYAN} 2 {ENDC}- Change password {PINK}{' '*22}║
        ║ *{CYAN} 3 {ENDC}- Add new user {PINK}{' '*25}║
        ║ *{RED} 4 {ENDC}- {UNDERL}Exit{ENDC}{PINK}{' '*34}║
        ╚{'═'*45}╝
        {ENDC}  Your selection: {CYAN}''')
    # The menu will keep appearing after every command run until user exits.

    if menu == '1':
        # This will retrieve the password via username.
        print(f"{ENDC}Retrieving password...")
        username = input("Please enter the username:").lower()
        if username not in my_users:
            print(f"{EM}User not found.")
        else:
            print(f"The password for {username} is {my_users[username]}.")

    elif menu == '2':
        # This will change the password for a user.
        print(f"{ENDC}Changing password...")
        username = input("Please enter the username:").lower()
        if username not in my_users:
            print(f"{EM}User not found.")
        else:
            password = input("Please enter password: ")
            if password == my_users[username]:
                new_password = input(f"{GREEN}Login successful.{ENDC} Please enter new password: ")
                my_users[username] = new_password
                print(f"The password for {username} has been changed to {new_password}.")
            else:
                print(f"{EM}Wrong password.")

    elif menu == '3':
        # This will add a new username and password to dictionary.
        print(f"{ENDC}Adding new user...")
        new_username = input("Please enter new username:").lower()
        new_password = input("Please enter new password:")
        my_users[new_username] = new_password
        print(f"{GREEN}User added successfully!{ENDC}")

    elif menu == '4':
        # This will exit the programme.
        print(f"{CYAN}Goodbye!{ENDC}")
        break

    else:
        print(f"\n{EM} You have made a wrong choice, please try again.")
        # This will print if the user enters anything that isn't 1, 2, 3 or 4.