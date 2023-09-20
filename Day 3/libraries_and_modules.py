
# Libraries and Modules

# Python has very extensive libraries and modules, this is great for us as DevOps engineers!

# Module = Single file of functions, classes, variables etc. that you can bring in and use in another Python file.
# Library = Collection of modules. Needs to be installed with pip.


import math
import random
import requests

num_float = 23.66

print(math.ceil(num_float))
print(math.floor(num_float))
print(math.pi)

rand_list = [1, 2, 3, 4, 5, 6, 7]
print(random.choice(rand_list))

rand_num = random.randint(1, 10)
print(rand_num)


request_bbc = requests.get("https://www.bbc.co.uk/")
print(request_bbc.status_code)
print(request_bbc.content)

bbc_content = request_bbc.content
# https://ichef.bbci.co.uk/ace/standard/960/cpsprodpb/fc91/live/56d880f0-579f-11ee-93bf-c758a853042c.jpg

request_poke = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
print(request_poke.status_code)
print(request_poke.content)
