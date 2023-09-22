import json


# Json is used to stare and transport data through systems.
# Easy to understand.

parsed_json = json.loads(open("example_json.json").read())
value = parsed_json["name"]
print(value)
print(type(parsed_json))

# Parsing is something(more) understandable. So le'ts make json more understandable for Python.
