# A program that asks for a number from the user and prints out a response.

while True:
    number_to_check = input("Please enter the number to check: ")
    # Getting the number from the user.
    if not number_to_check.isdigit():
        print("You need to enter a valid number. Let's try again...")
    else:
        break
# The while loop will keep running as long as the user doesn't enter a valid number.

number_to_check = int(number_to_check)

if number_to_check % 3 == 0 and number_to_check % 5 == 0:
    print("FizzBuzz")
elif number_to_check % 3 == 0:
    print("Fizz")
elif number_to_check % 5 == 0:
    print("Buzz")
else:
    print(f"The number {number_to_check} is not a multiple of either 3 or 5.")
# For multiples of 3, the program prints "Fizz".
# For multiples of 5, the program prints "Buzz".
# For multiples of 3 and 5, the program prints "FizzBuzz".