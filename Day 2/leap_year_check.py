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

year_to_check = int(input("Please enter the year to check: "))
# Getting the year from the user.

if year_to_check % 4 == 0:
    if year_to_check % 100 == 0:
        if year_to_check % 400 == 0:
            print(f"Year {year_to_check} is a leap year.")
        else:
            print(f"Year {year_to_check} is NOT a leap year.")
    else:
        print(f"Year {year_to_check} is a leap year.")
else:
    print(f"Year {year_to_check} is NOT a leap year.")
# If the year is divisible by 4, then it needs to be checked if it's also
# divisible by 100, in which case it has to also be divisible by 400 in order 
# to be a leap year.