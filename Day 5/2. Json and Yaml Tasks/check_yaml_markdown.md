# check_yaml.py Script

### This Python script will check if the yaml file entered is valid or not.

The script imports the following libraries:
- yaml
- os
- sys

The script will first check there is more than one argument entered in the terminal:

```python
if len(sys.argv) > 1
```

If there is more than one argument, the script will continue the checks.
```python
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")
        yaml.safe_load(file)
        file.close()
```
If the script is able to open the file and load it without any errors, it means the .yaml file is valid. Otherwise, it's invalid. 
<br>

To run this script in the terminal, you will have to type:
`python check_yaml.py <file_name>`