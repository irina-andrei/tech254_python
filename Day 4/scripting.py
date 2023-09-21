# Scripting

# There are seven modules that we can consider "core" in Python.
import sys
import os
import subprocess
import math
import random
# or 'from random import randrange'
import json
from datetime import datetime
# import datetime; or 'from datetime import dt'

''' sys '''
print(sys.version)
# Used for checking versions or hardware


''' os '''
print(f"This is the current folder: {os.getcwd()}")

# os.chdir("C:/Users/irina/PycharmProjects/Sparta/")
# This will change the directory to the one specified.

print(os.getcwd())

# os.mkdir("test_dir")
# This will make a directory in the current folder.


''' subprocess '''

subprocess.run(["python", "hello_world.py"])
# This will run a script from another location.


'''math'''

pi = math.pi
pi_string = str(pi)
print(f"The value of pi is {pi_string}")


''' random '''

rand_num = random.randrange(1, 10)
print(rand_num)


''' datetime '''

whatisthedate = datetime.now()
print(whatisthedate)
# normally, datetime.datetime.now()


''' json '''

x = {
    "name": "John",
    "age": 30,
    "city": "London"
}

print(type(x))

y = json.dumps(x)
# Converts the x dictionary to json format, which will be <class 'str'>
print(type(y))
print(y)