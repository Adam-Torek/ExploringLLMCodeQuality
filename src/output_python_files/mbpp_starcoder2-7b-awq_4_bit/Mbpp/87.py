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
Print all the even numbers from 1 to 1000.
Print all the odd numbers from 1 to 1000.
Print all the multiples of 5 from 5 to 1,000,000.
Print integers 1 to 100, but if divisible by 5 print "Coding" instead.
If divisible by 10 print "Coding Dojo".
"""

for i in range(0, 101):
    print(i)

for i in range(1, 1001):
    if i % 2 == 0:
        print(i)

for i in range(1, 1001):
    if i % 2!= 0:
        print(i)

for i in range(5, 1000001, 5):
    print(i)

for i in range(1, 1001):
    if i % 5 == 0:
        print("Coding")
    else:
        print(i)

for i in range(1, 1001):
    if i % 5 == 0:
        print("Coding Dojo")
    else:
        print(i)
/python/python_fundamentals/coin_toss.py
"""
Create a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
"""

import random

def coin_toss():
    heads = 0
    tails = 0
    for i in range(1, 5001):
        toss = random.randint(0, 1)
        if toss == 0:
            heads += 1
            print("Attempt #{}: Throwing a coin... It's a head!... Got {} head(s) so far and {} tail(s) so far".format(i, heads, tails))
        else:
            tails += 1
            print("Attempt #{}: Throwing a coin... It's a tail!... Got {} head(s) so far and {} tail(s) so far".format(i, heads, tails))

coin_toss()
/python/python_fundamentals/coin_toss_2.py
"""
Create another function that simulates tossing a coin 5,000 times. Your function should print the number of heads and tails and the percentage of head/tails.
"""

import random

def coin_toss():
    heads = 0
    tails = 0
    for i in range(1, 5001):
        toss = random.randint(0, 1)
        if toss == 0:
            heads += 1
            print("Attempt #{}: Throwing a coin... It's a head!... Got {} head(s) so far and {} tail(s) so far".format(i, heads, tails))
        else:
            tails += 1
            print("Attempt #{}: Throwing a coin... It's a tail!... Got {} head(s) so far and {} tail(s) so far".format(i, heads, tails))
    print("Ending the program. Thank you!")
    print("Heads: {}".format(heads))
    print("Tails: {}".format(tails))
    print("Percentage of Heads: {}".format(heads/5000