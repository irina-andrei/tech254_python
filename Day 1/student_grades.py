# A Python program that stores student grades.


# Some formatting shortcuts:
RED = '\033[31m'
GREEN = '\033[92m'
BLUE = '\033[94m'
PINK = '\033[95m'
CYAN = '\033[96m'
UNDERL = '\033[4m' # 'Underline'
ENDC = '\033[0m' # Removes all formatting applied.
EM = f"{RED}‼{ENDC}" # 'Exclamation Mark' shorthand

my_students = {
    "Lee Pace": {"Geography": 7.2,
                "Maths": 5.4,
                "Spanish": 8.3},

    "Tim Roth": {"Geography": 4.2,
                "Maths": 7,
                "Spanish": 6.1},

    "Maggie Smith": {"Geography": 9,
                "Maths": 9.3,
                "Spanish": 8.7}
                }
# A dictionary that will hold the grades for each student and each subject.

while True:
    menu = input(f'''
        {PINK}╔{'═'*45}╗
        ║{ENDC} Please select one of the following options: {PINK}║
        ║ *{CYAN} 1 {ENDC}- Show grades for 1 student {PINK}{' '*12}║
        ║ *{CYAN} 2 {ENDC}- Display all student grades {PINK}{' '*11}║
        ║ *{CYAN} 3 {ENDC}- Change a grade {PINK}{' '*23}║
        ║ *{RED} 4 {ENDC}- {UNDERL}Exit{ENDC}{PINK}{' '*34}║
        ╚{'═'*45}╝
        {ENDC}  Your selection: {CYAN}''')
    # The menu will keep appearing after every command run until user exits.

    if menu == '1':
        # This will show grades for 1 student.
        print(f"{ENDC}Retrieving grades...")
        student_name = input("Please enter name of student (it's case-sensitive!):")
        if student_name not in my_students:
            print(f"{EM}Student not found.")
        else:
            print(f"The grades of {CYAN}'{student_name}'{ENDC}:\n {my_students[student_name]}")

    elif menu == '2':
        # This will display all student grades.
        print(f"{ENDC}Retrieving grades...")
        for student_name in my_students.keys():
            print(f"The grades of {CYAN}'{student_name}'{ENDC}:\n {my_students[student_name]}")
        
    elif menu == '3':
        # This will change a student's grade.
        print(f"{ENDC}Changing grade user...")
        student_name = input("Please enter name of student (it's case-sensitive!):")
        if student_name not in my_students:
            print(f"{EM}Student not found.")
        else:
            pass
        print("Student grade changed.")

    elif menu == '4':
        # This will exit the programme.
        print(f"{CYAN}Goodbye!{ENDC}")
        break

    else:
        print(f"\n{EM} You have made a wrong choice, please try again.")
        # This will print if the user enters anything that isn't 1, 2, 3 or 4.