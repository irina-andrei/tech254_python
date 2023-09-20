# A program that lets the user calculate 2 values.

# Some formatting shortcuts:
BLUE = '\033[94m'
PINK = '\033[95m'
CYAN = '\033[96m'
ENDC = '\033[0m'  # Removes all formatting applied.


def getting_values():
    """ A function that gets the values from the user.
    Parameters: None
    Returns: 2 numbers """

    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2


def addition(nr1, nr2):
    """ A function that makes an addition.
    Parameters: nr1 and nr2
    Returns: the solution"""

    my_solution = nr1 + nr2

    return my_solution


def subtraction(nr1, nr2):
    """ A function that makes a subtraction.
    Parameters: nr1 and nr2
    Returns: the solution"""

    my_solution = nr1 - nr2
    
    return my_solution


def division(nr1, nr2):
    """ A function that makes a division.
    Parameters: nr1 and nr2
    Returns: the solution"""

    if nr2 == 0:
        print("You can't divide by 0.")
        return 0
    else:
        my_solution = nr1 / nr2

    return my_solution


def multiplication(nr1, nr2):
    """ A function that makes a multiplication.
    Parameters: nr1 and nr2
    Returns: the solution"""

    my_solution = nr1 * nr2

    return my_solution


title = f'''
    {PINK}╔{'═'*16}╗
    ║{BLUE}**{CYAN} Calculator {BLUE}**{PINK}║
    ╚{'═'*16}╝{ENDC}
    '''

print(title)


number1, number2 = getting_values()

operations = ['+', '-', '/', 'x']
# The only valid operations saved as a list.

while True:    
    operation = input("Enter the operation you want to perform (+ - / x): ")
    if operation == '*':
        operation = 'x'
    # As some users might enter '*' by mistake, we can easily fix that.

    if operation not in operations:
        print(f"'{operation}' is not a valid operator. Let's try again.")
        continue
    # It will keep looping until user enters a valid operator.

    solution = None
    error = False

    if operation == '+':
        solution = addition(number1, number2)
    elif operation == '-':
        solution = subtraction(number1, number2)
    elif operation == '/':
        solution = division(number1, number2)
        if number2 == 0:
            error = True
    elif operation == 'x':
        solution = multiplication(number1, number2)

    if solution == int(solution):
        solution = int(solution)
    else:
        solution = round(solution, 2)
    # A user-friendly format (i.e. a rounded float or 4 instead of 4.0).

    if number1 == int(number1):
        number1 = int(number1)
    if number2 == int(number2):
        number2 = int(number2)
    # Making sure there isn't an unnecessary ".0" at the end.

    if not error:
        print(f"{CYAN}{number1} {operation} {number2} = {solution}{ENDC}")
    else:
        print("Let's try again.")

    choice = input("Do you want to perform another operation? (Y/N) ").lower()

    if choice == 'n':
        print(f"{BLUE}Goodbye!{ENDC}")
        break

    choice = input("Do you want to change the numbers? (Y/N) ").lower()

    if choice == 'n':
        print(f"{BLUE}Okay, keeping the numbers...{ENDC}")
        continue
    else:
        print(f"{BLUE}Okay, let's change the numbers...{ENDC}")
        number1, number2 = getting_values()
