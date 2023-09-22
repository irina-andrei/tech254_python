# This will check that the json file is valid or not.

import json
import os
import sys


if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        # This will check if this is a file.
        file = open(sys.argv[1], "r")
        json.load(file)
        # using .load because we don't need to turn json into a dictionary like .loads would do, we just need to check the data.
        file.close()
        print("JSON is VALID!")
    else:
        print(sys.argv[1] + "not found")

else:
    print("Usage: python check_json.py <file>")
