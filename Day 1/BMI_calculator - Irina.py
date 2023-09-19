# A program that calculates a person's BMI.

GREEN = '\033[92m'
BLUE = '\033[94m'
PINK = '\033[95m'
CYAN = '\033[96m'
RED = '\033[31m'
ENDC = '\033[0m'  # Removes all formatting applied.


title = f'''
    {PINK}╔{'═'*25}╗
    ║{RED}♦♦{CYAN} BMI Calculator {RED}♦♦{PINK}║
    ╚{'═'*25}╝{ENDC}
    '''

print(title)

weight = float(input(f"Please enter your weight in kg: {CYAN}"))
height = float(input(f"{ENDC}Please enter your height in meters: {CYAN}"))
# casting these to float so we can use them in calculations.

BMI = round((weight / (height ** 2)), 2)
# Formula for BMI is BMI = (weight in kg) / ((height in metres)*(height in metres)).
# Instead of multiplying height by itself, we can do height to the power of 2.
# Rounding it to 2 decimals to be more user-friendly.

if BMI >= 30:
    status = f"{RED}obese"
elif BMI >= 25:
    status = f"{PINK}overweight"
elif BMI >= 18.5:
    status = f"{GREEN}normal"
else:
    status = f"{PINK}underweight"

print (f"""{ENDC}\n Based on your weight of {CYAN}{weight}kg{ENDC} and height of {CYAN}{height}m{ENDC}...
Your BMI is {BLUE}{BMI}{ENDC}. According on your BMI, you are {status}{ENDC}.""")