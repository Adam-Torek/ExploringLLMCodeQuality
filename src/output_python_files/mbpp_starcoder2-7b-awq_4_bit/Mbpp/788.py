"""
Write a function to create a new tuple from the given string and list.
assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
"""

def new_tuple(string, list):
    return tuple(string + list)

print(new_tuple(["WEB", "is"], "best"))/python/python_fundamentals/for_loop_basic2.py
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

for i in range(5, 1000001):
    if i % 5 == 0:
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
        print(i)/python/python_fundamentals/coin_tosses.py
"""
Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
"""

import random

def coin_tosses():
    heads = 0
    tails = 0
    for i in range(1, 5001):
        toss = random.randint(0, 1)
        if toss == 0:
            heads += 1
            print("Attempt #" + str(i) + ": Throwing a coin... It's a head!... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far")
        else:
            tails += 1
            print("Attempt #" + str(i) + ": Throwing a coin... It's a tail!... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far")

coin_tosses()/python/python_fundamentals/coin_tosses2.py
"""
Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
"""

import random

def coin_tosses():
    heads = 0
    tails = 0
    for i in range(1, 5001):
        toss = random.randint(0, 1)
        if toss == 0:
            heads += 1
            print("Attempt #" + str(i) + ": Throwing a coin... It's a head!... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far")
        else:
            tails += 1
            print("Attempt #" + str(i) + ": Throwing a coin... It's a tail!... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far")
    print("Ending the program, thank you!")

coin_tosses()/python/python_fundamentals/coin_tosses3.py
"""
Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
"""

import random

def coin_tosses():
    heads = 0
    tails = 0
    for i in range(1, 5001):
        toss = random.randint(0, 1)
        if toss == 0:
            heads +=