# yaml_to_json.py Script

### This Python script will convert a .yaml file to .json.

The script imports the following libraries:
- yaml
- json
- os
- sys

<br>

First, the script makes sure the file does exist:
```python
if os.path.exists(sys.argv[1]):
    source_file = open(sys.argv[1], "r")
    source_content = yaml.safe_load(source_file)
    source_file.close()
```
If it doesn't, it will exit the script.

<br>

Processing the conversion:
```python
output = json.dumps(source_content, indent=4)
```

Afterwards, if the target file already exists, it will exit the program. Otherwise, it will write the output to the selected file and exit the script:

```python
if len(sys.argv) < 3:
    print(output)
elif os.path.exists(sys.argv[2]):
    print("ERROR: " + sys.argv[2] + " already exists")
    exit(1)
else:
    target_file = open(sys.argv[2], "w")
    target_file.write(output)
    target_file.close()
```

<br>

To run this script in the terminal, you will have to type:

`python yaml_to_json.py <source_file.yaml> [target_file.json]`