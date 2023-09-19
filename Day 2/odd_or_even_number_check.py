# A Python program that checks if a number is either odd or even.


number_to_check = int(input("Please enter your number: "))
# Getting the number from the user.

if number_to_check % 2 == 0:
    print(f"Number {number_to_check} is even.")
else:
    print(f"Number {number_to_check} is odd.")
# Checking whether the number divided by 2 has the remainder 0. 
# If so, then it's even. Otherwise it's odd.
#