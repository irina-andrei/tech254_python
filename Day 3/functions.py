# Functions

# DRY - Don't Repeat Yourself
# Allow us to embed/reference code, making it reusable.

# Making a Function

def print_something(print_string):
    print(print_string)


def greeting(name):
    print(f"Hello, my name is {name}")


print_something("we can pass anything in here")
greeting("Luke")


# The Return statement - holds a value

def addition(int1, int2):
    return int1 + int2


print(addition(12, 3))

# Multiple Arguments


def multi_args(arg2, *multi_arguments):
    for arg in multi_arguments:
        print(arg)
    print(arg2)
    print(type(multi_arguments))


multi_args(1, 2, 3, 4, 5)


"""
def holiday_days(days_worked):
    happy_days = days_worked * 21 / 365
    happy_days = round(happy_days)
    return happy_days


print(f"Wafa worked 250 days, so she can take {holiday_days(250)} day(s)")
print(f"Luke worked 12 days, so he can take {holiday_days(12)} day(s)")
print(f"Irina worked 79 days, so she can take {holiday_days(79)} day(s)")
"""

# Type Hints - can research this

""" ==== Functions Good Practices ====
1. Add useful comments to explain your function
2. Clear function names and argument names
3. Keep your functions small and compact
4. Avoid duplication
5. Correct indentation and formatting/syntax
6. Organised properly
7. Do not use them unnecessarily
8. Functions at the start of your code 
9. Consider using Type Hints
"""