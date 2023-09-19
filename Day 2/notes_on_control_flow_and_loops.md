# Control Flow and Loops

### *Control Flow*
 Control **the flow of your code** (make decisions and ignore certain code dependent on factors).

- Check if conditions are true before you run a piece of code. 
- Can think of each control flow statement as a boolean.

```python
if age >= 18:
    print("You are old enough to watch this movie")
elif age < 18:
    print("Sorry, you are not old enough to watch this movie")
```
elif -> Less processing power and runs only if the *'if condition'* is not met.


```python
film_rating = "U"

if film_rating.lower() == "u":
    print("All age groups can watch this movie")
elif film_rating.lower() == "pg":
    print("Parental guidance is advised for this movie")
elif film_rating.lower() == "12" or film_rating.lower() == "12a":
    print("People aged 12 or over can watch this film unsupervised. Younger people must be supervised.")
elif film_rating.lower() == "15":
    print("People aged 15 or over can watch this movie")
elif film_rating.lower() == "18":
    print("People aged 18 can watch this movie")
else:
    print("This is not a valid rating, please use 'u', 'pg', '12' or '12a', '15', '18'")
```
else -> a way to round off control flow block.

<br>

### *For Loops*
Python uses *'for'* only, no *'for each'* loops.

```python
list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {
    1: {"name": "Bronson",
        "money": "£0.05"},
    2: {"name": "Masha",
        "money": "£3.66"},
    3: {"name": "Roscoe",
        "money": "£1.14"}
}
```

```python
for num in list_data:
    print(num * 2)
```
-> This will print **2, 4, 6, 8, 10**

<br>

### *Nested For Loops*
```python
for data in embedded_lists:
    print(data)
    for num in data:
        print(num)
```
This will print:   
**[1, 2, 3]   
1   
2   
3   
[4, 5, 6]   
4   
5   
6**

<br>

### *Looping through dictionaries*
```python
for item in dict_data.values():
    for embed_value in item.values():
        print(embed_value)
```
This will print:   
**Bronson   
£0.05   
Masha  
£3.66  
Roscoe  
£1.14**

<br>

### *Getting values for individual keys*
```python
for items in dict_data.values():
    print(items["money"])
```
This will print:   
**£0.05  
£3.66  
£1.14**

<br>

### *Loops and if statements*
```python
for num in list_data:
    if num == 3:
        print("I found 3!")
    elif num > 3:
        print("Gone too far!")
    else:
        print("Too soon!")
```
*This will print:*   
**Too soon!  
Too soon!  
I found 3!  
Gone too far!  
Gone too far!**

<br>

### *While loops*
- For loops are all to do with iterating through a collection.
-  While loops are more like *a monitor* -> **while** something is **True**, then ***act***.

```python
x = 0
while x < 10:
    print(f"It's working --> {x}")
    if x == 4:
        break
    x += 1
```
This will print:  
**It's working --> 0  
It's working --> 1  
It's working --> 2  
It's working --> 3  
It's working --> 4**

<br>

### *Verifying User Input*
```python
user_prompt = True
while user_prompt:
    age = input("What is your age? ")
    if age.isdigit() and int(age) < 118:
        user_prompt = False
    else:
        print("Please provide your answer in digits, below 118")
print(f"Your age is {age}")
```
- The while loop will run as long as the user hasn't entered a valid age. 
- After exiting the loop, program will print out the user's age.