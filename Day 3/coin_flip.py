# A Python program that flips a coin.

import random


coin_sides = ["Heads", "Tails"]
# The list with the 2 choices available.

print(f"Let's flip a coin! The result is...\n\t{random.choice(coin_sides)}")
# This will randomly print either 'Heads' or 'Tails'.