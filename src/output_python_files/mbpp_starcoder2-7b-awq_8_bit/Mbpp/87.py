"""
Write a function to merge three dictionaries into a single dictionary.
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
"""

def merge_dictionaries_three(dict1, dict2, dict3):
    dict1.update(dict2)
    dict1.update(dict3)
    return dict1

print(merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" }))
/python/python_fundamentals/for_loop_basic2.py
"""
Print integers from 0 to 100. 
Print all the odd integers from 1 to 100. 
Print all the multiples of 5 from 5 to 1,000,000. 
Print integers 1 to 100. 
If divisible by 5, print "Coding" instead. 
If divisible by 10, print "Coding Dojo". 
"""

for i in range(101):
    print(i)

for i in range(1, 101, 2):
    print(i)

for i in range(5, 1000001, 5):
    print(i)

for i in range(1, 101):
    if i % 5 == 0:
        print("Coding")
    elif i % 10 == 0:
        print("Coding Dojo")
    else:
        print(i)
/python/python_fundamentals/coin_tosses.py
"""
Create a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
Sample output should be like the following:
Starting the program...
Attempt #1: Throwing a coin... It's a head!... Got 1 head(s) so far and 0 tail(s) so far
Attempt #2: Throwing a coin... It's a head!... Got 2 head(s) so far and 0 tail(s) so far
Attempt #3: Throwing a coin... It's a tail!... Got 2 head(s) so far and 1 tail(s) so far
Attempt #4: Throwing a coin... It's a head!... Got 3 head(s) so far and 1 tail(s) so far
Attempt #5: Throwing a coin... It's a head!... Got 4 head(s) so far and 1 tail(s) so far
Attempt #6: Throwing a coin... It's a tail!... Got 4 head(s) so far and 2 tail(s) so far
Attempt #7: Throwing a coin... It's a head!... Got 5 head(s) so far and 2 tail(s) so far
Attempt #8: Throwing a coin... It's a tail!... Got 5 head(s) so far and 3 tail(s) so far
Attempt #9: Throwing a coin... It's a head!... Got 6 head(s) so far and 3 tail(s) so far
Attempt #10: Throwing a coin... It's a head!... Got 7 head(s) so far and 3 tail(s) so far
...
Attempt #5000: Throwing a coin... It's a head!... Got 2499 head(s) so far and 2501 tail(s) so far
Ending the program, thank you!
"""

import random

def coin_tosses():
    heads = 0
    tails = 0
    for i in range(1, 5001):
        print("Attempt #{}: Throwing a coin...".format(i))
        if random.randint(0, 1) == 0:
            print("It's a head!")
            heads += 1
        else:
            print("It's a tail!")
            tails += 1
        print("Got {}