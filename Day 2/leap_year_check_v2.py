# A Python program that will check whether a year is a leap year or not.


'''
leap year:
/ 4 and no reminder
except every year that is divisble by 100
unless the year is also evenly divisble by 400

2000 / 4 = 500 (leap)
2000 / 100 = 20 (not leap)
2000 / 400 = 5 (leap)
'''

# Some formatting shortcuts:
GREEN = '\033[92m'
BLUE = '\033[94m'
PINK = '\033[95m'
CYAN = '\033[96m'
RED = '\033[31m'
ENDC = '\033[0m'  # Removes all formatting applied.
EM = f"{RED}‼{ENDC}" # 'Exclamation Mark' shorthand


title = f'''
    {PINK}╔{'═'*23}╗
    ║{BLUE}**{CYAN} Leap Year Checker {BLUE}**{PINK}║
    ╚{'═'*23}╝{ENDC}
    '''

print(title)


year_to_check = int(input(f"Please enter the year to check: {CYAN}"))
# Getting the year from the user.
print(f"{ENDC}")

if year_to_check % 4 == 0:
    if year_to_check % 100 == 0:
        if year_to_check % 400 == 0:
            print(f"Year {PINK}{year_to_check}{ENDC} is a {CYAN}leap year{ENDC}.\n")
        else:
            print(f"{EM} Year {PINK}{year_to_check}{ENDC} is {RED}not a leap year{ENDC}.\n")
    else:
        print(f"Year {PINK}{year_to_check}{ENDC} is a {CYAN}leap year{ENDC}.\n")
else:
    print(f"{EM} Year {PINK}{year_to_check}{ENDC} is {RED}not a leap year{ENDC}.\n")
# If the year is divisible by 4, then it needs to be checked if it's also
# divisible by 100, in which case it has to also be divisible by 400 in order 
# to be a leap year.