# A program that calculates a person's BMI.


weight = float(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in meters: "))
# casting these to float so we can use them in calculations.

BMI = round((weight / (height ** 2)), 2)
# Formula for BMI is BMI = (weight in kg) / ((height in metres)*(height in metres)).
# Instead of multiplying height by itself, we can do height to the power of 2.
# Rounding it to 2 decimals to be more user-friendly.

if BMI >= 30:
    status = "obese"
elif BMI >= 25:
    status = "overweight"
elif BMI >= 18.5:
    status = "normal"
else:
    status = "underweight"

print (f"""\n Based on your weight of {weight}kg and height of {height}m...
Your BMI is {BMI}. According on your BMI, you are {status}.\n""")