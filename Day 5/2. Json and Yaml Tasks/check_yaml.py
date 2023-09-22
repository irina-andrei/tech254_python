# This will check that the yaml file is valid or not.

import yaml
import os
import sys


if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        # This will check if this is a file.
        file = open(sys.argv[1], "r")
        yaml.safe_load(file)
        file.close()
        print("YAML is VALID!")
    else:
        print(sys.argv[1] + "not found")

else:
    print("Usage: python check_yaml.py <file>")


# In the terminal, you type:
# python check_yaml.py output.yaml
