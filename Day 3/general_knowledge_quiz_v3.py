# A General Knowledge quiz that allows users to test their knowledge
# and get a score as a percentage at the end.
# Each question is worth 10 points, with 15 questions in total (Max score: 150)


# Some formatting shortcuts:
RED = '\033[31m'
GREEN = '\033[92m'
BLUE = '\033[94m'
PINK = '\033[95m'
CYAN = '\033[96m'
ENDC = '\033[0m'  # Removes all formatting applied.
EM = f"{RED}‼{ENDC}"  # 'Exclamation Mark' shorthand


def print_score(current_score, questions):
    """ A function that prints out the current score as a percentage.
    Parameters: current score, number of questions
    Returns: None"""

    current_score = round(current_score / questions * 10)
    if current_score == 0:
        current_score = "  0"
    elif current_score < 100:
        current_score = " " + str(current_score)
    # This will make sure the score is displayed on the screen without moving the borders of the score panel.

    score_panel = f'''
    {CYAN}╔{'═'*23}╗
    ║{PINK}**{BLUE}  Your score: {GREEN}{current_score}% {PINK}**{CYAN}║
    ╚{'═'*23}╝{ENDC}
    '''
    print(score_panel)


title = f'''
    {PINK}╔{'═'*22}╗
    ║{BLUE}**{CYAN}  Knowledge Quiz  {BLUE}**{PINK}║
    ╚{'═'*22}╝{ENDC}
    '''
print(title)
# This will print out the title of the game.

print(f'''Welcome to the {PINK}General Knowledge Quiz{ENDC}. 
    Let's test your {GREEN}knowledge{EM}''')
player_name = input(f"\nFirst, enter your name: {CYAN}").capitalize()
# Getting the player's name and starting the game. 

print(f"{ENDC}\nGreat stuff, {BLUE}{player_name}{ENDC}. Now let's get started...")

quiz_questions = [
    f'''1. {PINK}What city is known as 'The Eternal City'? {ENDC}
    A: Rome
    B: Paris
    C: London
    D: New York''',
    f'''2. {PINK}Who has won the most total Academy Awards?{ENDC}
    A: Steven Spielberg
    B: Martin Scorsese
    C: Walt Disney
    D: Tom Hanks''',
    f'''3. {PINK}What company was originally called "Cadabra"?{ENDC}
    A: Amazon
    B: Netflix
    C: Twitter
    D: eBay''',
    f'''4. {PINK}What game studio makes the Red Dead Redemption series?{ENDC}
    A: Microsoft Studios
    B: Blizzard
    C: EA Games
    D: Rockstar Games''',
    f'''5. {PINK}What country has won the most World Cups?{ENDC}
    A: Brazil
    B: Spain
    C: France
    D: Germany''',
    f'''6. {PINK}The Parthenon Marbles are controversially located in what museum?{ENDC}
    A: The Louvre
    B: Athens History Museum
    C: The British Museum
    D: National History Museum''',
    f'''7. {PINK}Where did sushi originate?{ENDC}
    A: Thailand
    B: China
    C: South Korea
    D: Japan''',
    f'''8. {PINK}Kratos is the main character of what video game series?{ENDC}
    A: Red Dead Redemption 2
    B: God of War
    C: The Last of Us
    D: The Witcher 3''',
    f'''9. {PINK}How many dots appear on a pair of dice?{ENDC}
    A: 21
    B: 18
    C: 42
    D: 26''',
    f'''10. {PINK}Queen guitarist Brian May is also an expert in what scientific field?{ENDC}
    A: Astrophysics
    B: Biology
    C: Chemistry
    D: Maths''',
    f'''11. {PINK}What Netflix show had the most streaming views in 2021?{ENDC}
    A: Grace and Frankie
    B: Tiger King
    C: Ozark
    D: Squid Game''',
    f'''12. {PINK}What software company is headquartered in Redmond, Washington?{ENDC}
    A: Twitter
    B: Microsoft
    C: Amazon
    D: eBay''',
    f'''13. {PINK}What country drinks the most coffee per capita?{ENDC}
    A: USA
    B: Italy
    C: Finland
    D: France''',
    f'''14. {PINK}Simone Biles is famous for her skill in what sport?{ENDC}
    A: Gymnastics
    B: Football
    C: Sumo wrestling
    D: Archery''',
    f'''15. {PINK}Which of the following sauces is NOT traditionally vegan?{ENDC}
    A: Hoisin
    B: Worcestershire
    C: Mustard
    D: Wasabi'''
]
# The list with all 15 questions. 

quiz_answers = [
    "A",
    "C",
    "A",
    "D",
    "A",
    "C",
    "B",
    "B",
    "C",
    "A",
    "D",
    "B",
    "C",
    "A",
    "B"
]
# The answers to all 15 questions, in order.

score = 0

# This loop will go through each question one by one:
for index in range(len(quiz_questions)):
    if index == 0:
        print("Are you feeling lucky? Let's see the first question.\n")
    # This will only print at the beginning of the game.
    elif index == 8:
        print(f"{BLUE}First 8 questions over{ENDC}, let's see how you've done so far...")
        print_score(score, index)
        if score < 30:
            print(f"Yikes, {RED}{player_name}{ENDC}... Not doing too well. But you still have time to improve.\n")
        elif score < 60:
            print(f"Okay, not bad {CYAN}{player_name}{ENDC}, but could be better... Let's keep going.\n")
        elif score < 80:
            print(f"Almost perfect {BLUE}{player_name}{ENDC}, keep at it.\n")
        else:
            print(f"Perfect answers so far! Amazing!! Great job {GREEN}{player_name}{ENDC}.\n")
    # Halfway through the game, this will print the score so far and give a message to the player.

    while True:
        print(quiz_questions[index])
        answer = input(f"Your answer {CYAN}(A, B, C or D){ENDC}: ").upper()

        if answer not in ["A", "B", "C", "D"]:
            print(f"\n{EM}Sorry, that wasn't a valid answer: only A, B, C or D accepted. {RED}Let's try again{ENDC}.\n")
            continue

        if answer == quiz_answers[index]:
            print(f"\n{GREEN}Correct!{ENDC} 10 points for you, {GREEN}{player_name}{ENDC}.\n")
            score += 10
        else:
            print(f"\n{RED}Sorry{ENDC}, wrong answer {RED}{player_name}{ENDC}. :( ")
            print(f"Correct answer was {BLUE}{quiz_answers[index]}{ENDC}.\n")
        
        break
    # The while loop makes sure the player has entered a valid answer.
    # It will keep looping until the player enters A, B, C or D.


print(f"That was the {GREEN}last question{ENDC}. The final tally is in...\n")
print_score(score, 15)
# The final score of the game is printed.

if score < 50:
    print(f"Yikes, {RED}{player_name}{ENDC}... I'm sure {CYAN}you'll do better next time{ENDC}.\n")
elif score < 90:
    print(f"Okay, not bad {CYAN}{player_name}{ENDC}, but {BLUE}I have faith you can do better{ENDC}.\n")
elif score < 120:
    print(f"Overall good performance {BLUE}{player_name}{ENDC}, {CYAN}I am impressed{ENDC}.\n")
elif score < 150:
    print(f"Almost perfect score {BLUE}{player_name}{ENDC}! {CYAN}You're truly impressive{ENDC}.\n")
else:
    print(f"Perfect score! {CYAN}INCREDIBLE!{ENDC} Great job {GREEN}{player_name}, {PINK}a round of applause{ENDC}.\n")
# The player will get a personalised message based on their score.


# Question Sources:
# https://www.mentimeter.com/blog/audience-energizers/55-free-trivia-and-fun-quiz-question-templates
