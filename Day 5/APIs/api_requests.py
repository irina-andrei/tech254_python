# API Requests

import requests
import json

post_codes_req = requests.get("https://api.postcodes.io/postcodes/SE100FN")

print(post_codes_req)
# This will print '<Response [200]'>

print(post_codes_req.headers)
# This gives the headers

print(type(post_codes_req.content))
# Gives .json body as bytes


# Long way
post_codes_dict = json.loads(post_codes_req.content)
# Turn it into a Python dict
print(type(post_codes_req))
# Dictionary

# Short way
print(post_codes_req.json())
# In-Built method in the requests library to do this