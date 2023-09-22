# Post request to postcodes API

import requests
import json


json_body = json.dumps({"postcodes": ["PR3 0SG", "M45 6GN", "EX16 5BL", "SE10 0FN"]})
headers = {"Content-Type": "application/json"}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)

print(post_multi_req.json())
