"""
Write a function that takes in a string and character, replaces blank spaces in the string with the character, and returns the string.
assert replace_blank("hello people",'@')==("hello@people")
"""

def replace_blank(string, char):
    new_string = ""
    for i in range(len(string)):
        if string[i] == " ":
            new_string += char
        else:
            new_string += string[i]
    return new_string

print(replace_blank("hello people", "@"))
/python/python_fundamentals/for_loop_basic2.py
"""
Print integers from 0 to 100.
Print all the even numbers from 1 to 1000.
Print all the odd numbers from 1 to 1000.
Print all the multiples of 5 from 5 to 1,000,000.
Print integers 1 to 100, but if divisible by 5 print "Coding" instead.
If divisible by 10 print "Coding Dojo".
"""

for i in range(1, 1001):
    if i % 2 == 0:
        print("Coding")
    elif i % 10 == 0:
        print("Coding Dojo")
    else:
        print(i)
/python/python_fundamentals/coin_toss.py
"""
Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
"""

import random

def coin_toss():
    heads = 0
    tails = 0
    for i in range(5000):
        if random.randint(0, 1) == 0:
            heads += 1
        else:
            tails += 1
    print("Heads: " + str(heads))
    print("Tails: " + str(tails))

coin_toss()
/python/python_fundamentals/coin_toss_2.py
"""
Create another function called toss_multiple_coins(x) that returns a list with the string 'head' or 'tail' values. x is the number of coins to be tossed.
"""

import random

def coin_toss():
    heads = 0
    tails = 0
    for i in range(5000):
        if random.randint(0, 1) == 0:
            heads += 1
        else:
            tails += 1
    print("Heads: " + str(heads))
    print("Tails: " + str(tails))

def toss_multiple_coins(x):
    coins = []
    for i in range(x):
        if random.randint(0, 1) == 0:
            coins.append("heads")
        else:
            coins.append("tails")
    return coins

print(toss_multiple_coins(5000))
/python/python_fundamentals/coin_toss_3.py
"""
Create another function called toss_multiple_coins(x) that returns a list with the string 'head' or 'tail' values. x is the number of coins to be tossed.
"""

import random

def coin_toss():
    heads = 0
    tails = 0
    for i in range(5000):
        if random.randint(0, 1) == 0:
            heads += 1
        else:
            tails += 1
    print("Heads: " + str(heads))
    print("Tails: " + str(tails))

def toss_multiple_coins(x):
    coins = []
    for i in range(x):
        if random.randint(0, 1) == 0:
            coins.append("heads")
        else:
            coins.append("tails")
    return coins

def toss_multiple_coins_2(x):
    coins = []
    for i in range(x):
        coins.append("heads" if random.randint(0, 1) == 0 else "tails")
    return coins

print(toss_multiple_coins_2(5000))
/python/python_fundamentals/coin_toss_4.py
"""
Create another function called toss_multiple_coins(x) that returns a list with the string 'head' or 'tail' values. x is the number of coins to be tossed