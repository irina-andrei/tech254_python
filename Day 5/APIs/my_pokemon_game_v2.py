import requests
import json
import random as rd
import pokemon_ascii
import time

# Some formatting shortcuts:
RED = '\033[91m'
LIGHTRED = '\033[31m'
GREEN = '\033[32m'
LIGHTGREEN = '\033[92m'
YELLOW = '\033[33m'
LIGHTYELLOW = '\033[93m'
BLUE = '\033[34m'
LIGHTBLUE = '\033[94m'
PURPLE = '\033[35m'
PINK = '\033[95m'
CYAN = '\033[36m'
LIGHTCYAN = '\033[96m'
ENDC = '\033[0m'  # Removes all formatting applied.

colour_dict = {
    0: f'\033[31m', # red
    1: f'\033[32m', # green
    2: f'\033[94m', # blue 
    3: f'\033[95m', # pink
    4: f'\033[96m', # cyan
    5: f'\033[93m' # yellow
    }


ascii_dict = {
    1: pokemon_ascii.bulbasaur(),
    2: pokemon_ascii.ivysaur(),
    3: pokemon_ascii.venusaur(),
    4: pokemon_ascii.charmander(),
    5: pokemon_ascii.charmeleon(),
    6: pokemon_ascii.charizard(),
    7: pokemon_ascii.squirtle(),
    8: pokemon_ascii.wartortle(),
    9: pokemon_ascii.blastoise(),
    10: pokemon_ascii.caterpie(),
    11: pokemon_ascii.metapod(),
    12: pokemon_ascii.butterfree(),
    13: pokemon_ascii.weedle(),
    14: pokemon_ascii.kakuna(),
    15: pokemon_ascii.beedrill(),
    16: pokemon_ascii.pidgey(),
    17: pokemon_ascii.pidgeotto(),
    18: pokemon_ascii.pidgeot(),
    19: pokemon_ascii.rattata(),
    20: pokemon_ascii.raticate()
}

random_magic = [0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5]

title = f'''
    {LIGHTRED}╔{'═'*22}╗
    ║{LIGHTBLUE}**{LIGHTCYAN}  Pokemon Battle  {LIGHTBLUE}**{LIGHTRED}║
    ╚{'═'*22}╝{ENDC}
    '''
print(title)
# This will print out the title of the game.

print(f"Welcome to the game! {PINK}Let's get started...{ENDC}")
print(f"Here are the {BLUE}Pokemons{ENDC} available:\n")


# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']

pokemon_dict = {}
# This will contain the names of all the Pokemons available.

for index in range(len(pokemon_list)):
    print(f"{colour_dict[index % 6]}", end = '')
    pokemon_name = pokemon_list[index]['name'].capitalize()
    pokemon_dict[index + 1] = pokemon_name
    print(f"{index + 1}: {pokemon_name}")

secret = False

# Get the user's choice
choice_index = int(input(f"{ENDC}\nEnter the index of the Pokemon you want to play as: "))
if choice_index == 21:
    player_pokemon = "Pikachu"
    secret = True
else:
    player_pokemon = pokemon_dict[choice_index]
print(f"You chose {BLUE}{player_pokemon}!")

if secret:
    print(f"{pokemon_ascii.pikachu()}{ENDC}")
else:
    print(f"{ascii_dict[choice_index]}{ENDC}")

time.sleep(3)

# Get the pokemon's data from the API
if secret:
    url = f"https://pokeapi.co/api/v2/pokemon/pikachu/"
else:
    url = f"https://pokeapi.co/api/v2/pokemon/{choice_index}/"
response = requests.get(url)
pokemon_data = json.loads(response.text)

# Getting abilities
player_abilities = []
for index in range(len(pokemon_data['abilities'])):
    player_abilities.append(pokemon_data['abilities'][index]['ability']['name'])

# Formatting height and weight properly
height_formatted = int(pokemon_data['height']) / 10
weight_formatted = int(pokemon_data['weight']) / 10

player_XP = pokemon_data["base_experience"]
# Health Points
player_HP = pokemon_data["stats"][0]["base_stat"]
# Attack Points
player_attack = pokemon_data["stats"][1]["base_stat"]
# Defence points
player_defence = pokemon_data["stats"][2]["base_stat"]

print(f"\nYour Pokemon '{PURPLE}{player_pokemon}{ENDC}' Stats:\n")

print(f"""{LIGHTBLUE}Base Experience: {ENDC}{player_XP}
{PURPLE}HP: {ENDC}{player_HP}
{RED}Attack: {ENDC}{player_attack}
{GREEN}Defence: {ENDC}{player_defence}
{BLUE}Weight: {ENDC}{weight_formatted}kg
{CYAN}Height: {ENDC}{height_formatted}m
{YELLOW}Abilities: {ENDC}""")
for index in range(len(player_abilities)):
    print(f"\t{PINK}{index+1}{ENDC}: {player_abilities[index]}")

time.sleep(5)


print("\nNow the CPU will randomly get a Pokemon too.")

time.sleep(1)
print("Drumroll...")

drums = '''
                    /
                 __o____\____
                /._______o__.\.
                |'-=-=-=-=-='|
                |\  /\  /\  /|
                | \/  \/  \/ |
                \.-=-=-=-=-='/
                 '"""""""""""
        '''

print(f"{PURPLE}{drums}{ENDC}")

time.sleep(3)

CPU_random_index = choice_index
while CPU_random_index == choice_index:
    CPU_random_index = rd.randint(1, 20)
# This will make sure the Pokemon the CPU gets will not be the same as the player's.

CPU_pokemon = pokemon_dict[CPU_random_index]
print(f"CPU is playing as {GREEN}{CPU_pokemon}!{ENDC}")
print(f"{ascii_dict[CPU_random_index]}{ENDC}")

time.sleep(3)

# Get the pokemon's data from the API
url = f"https://pokeapi.co/api/v2/pokemon/{CPU_random_index}/"
response = requests.get(url)
pokemon_data = json.loads(response.text)

# Getting abilities
CPU_abilities = []
for index in range(len(pokemon_data['abilities'])):
    CPU_abilities.append(pokemon_data['abilities'][index]['ability']['name'])

# Formatting height and weight properly
height_formatted = int(pokemon_data['height']) / 10
weight_formatted = int(pokemon_data['weight']) / 10

CPU_XP = pokemon_data["base_experience"]
# Health Points
CPU_HP = pokemon_data["stats"][0]["base_stat"]
# Attack Points
CPU_attack = pokemon_data["stats"][1]["base_stat"]
# Defence points
CPU_defence = pokemon_data["stats"][2]["base_stat"]

print(f"\nThe CPU's Pokemon '{PURPLE}{CPU_pokemon}{ENDC}' Stats:")

print(f"""{LIGHTBLUE}Base Experience: {ENDC}{CPU_XP}
{PURPLE}HP: {ENDC}{CPU_HP}
{RED}Attack: {ENDC}{CPU_attack}
{GREEN}Defence: {ENDC}{CPU_defence}
{BLUE}Weight: {ENDC}{weight_formatted}kg
{CYAN}Height: {ENDC}{height_formatted}m
{YELLOW}Abilities: {ENDC}""")
for index in range(len(CPU_abilities)):
    print(f"\t{PINK}{index+1}{ENDC}: {CPU_abilities[index]}")

time.sleep(5)

print(f"\n\n{CYAN}Let's start the game!\n")

round = 0

while True:
    round += 1
    title = f'''
        {PINK}╔{'═' * 15}╗
        ║{LIGHTBLUE}**{LIGHTCYAN}  ROUND {round}  {LIGHTBLUE}**{PINK}║
        ╚{'═' * 15}╝{ENDC}
        '''
    print(title)
    if round % 2 != 0:
        if secret:
            print(f"{pokemon_ascii.pikachu()}{ENDC}")
        else:
            print(f"{ascii_dict[choice_index]}{ENDC}")
        print("It's your turn. Here are your available abilities:")
        for index in range(len(player_abilities)):
            print(f"\t{PINK}{index + 1}{ENDC}: {player_abilities[index]}")
        ability_choice = int(input("Enter the ability index you want to use: "))
        print(f"You chose {CYAN}{player_abilities[ability_choice-1]}{ENDC}. Let's see what happens...")

        time.sleep(1)

        drums = '''
                            /
                         __o____\____
                        /._______o__.\.
                        |'-=-=-=-=-='|
                        |\  /\  /\  /|
                        | \/  \/  \/ |
                        \.-=-=-=-=-='/
                         '"""""""""""
                '''

        print(f"{PURPLE}{drums}{ENDC}")

        time.sleep(3)

        magic = rd.choice(random_magic)
        hit_strength = (player_attack + (player_XP / 100 * ability_choice)) * magic

        print(f"The CPU had {GREEN}{int(CPU_HP)} Health Points{ENDC}.")

        if CPU_defence <= hit_strength:
            CPU_HP = CPU_HP - (hit_strength - CPU_defence)
            print(f"\nWith {player_abilities[ability_choice - 1]}, you inflicted {RED}{int(hit_strength - CPU_defence)}{ENDC} points of damage!")
            time.sleep(3)
        else:
            print(f"\nYour hit was not strong enough... {LIGHTRED}No damage inflicted{LIGHTRED}.")
            time.sleep(3)
        if CPU_HP <= 0:
            title = f'''
                    {PINK}╔{'═' * 17}╗
                    ║{LIGHTBLUE}**{LIGHTCYAN}  YOU WON!!  {LIGHTBLUE}**{PINK}║
                    ╚{'═' * 17}╝{ENDC}
                    '''
            print(title)
            break
    else:
        print("It's CPU's turn.")
        print(f"{ascii_dict[CPU_random_index]}{ENDC}")

        print("Here are the abilities CPU can choose:")
        for index in range(len(CPU_abilities)):
            print(f"\t{PINK}{index + 1}{ENDC}: {CPU_abilities[index]}")
        time.sleep(3)

        drums = '''
                                    /
                                 __o____\____
                                /._______o__.\.
                                |'-=-=-=-=-='|
                                |\  /\  /\  /|
                                | \/  \/  \/ |
                                \.-=-=-=-=-='/
                                 '"""""""""""
                        '''

        print(f"{PURPLE}{drums}{ENDC}")

        time.sleep(5)

        magic = rd.choice(random_magic)
        CPU_ability_choice = rd.randint(1, len(CPU_abilities))
        hit_strength = (CPU_attack + (CPU_XP / 100 * CPU_ability_choice)) * magic
        print(f"You had {GREEN}{int(player_HP)} Health Points{ENDC}.")
        if player_defence <= hit_strength:
            player_HP = player_HP - (hit_strength - player_defence)
            print(f"CPU inflicted {RED}{int(hit_strength - player_defence)}{ENDC} points of damage with {CYAN}{CPU_abilities[CPU_ability_choice - 1]}{ENDC}!")
        else:
            print(f"The CPU hit was not strong enough... {GREEN}No damage inflicted{ENDC}.")

        time.sleep(3)

        if player_HP <= 0:
            title = f'''
                    {BLUE}╔{'═' * 18}╗
                    ║{CYAN}**{RED}  YOU LOST!!  {CYAN}**{BLUE}║
                    ╚{'═' * 18}╝{ENDC}
                    '''
            print(title)
            break

    if round == 9:
        break
