"""
Write a function to create a new tuple from the given string and list.
assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
"""

def new_tuple(string, list):
    return tuple(string + list)

print(new_tuple(["WEB", "is"], "best"))/python/python_fundamentals/for_loop_basic2.py
"""
Print integers from 0 to 100. 
But for multiples of five print "Coding" instead of the number. 
For multiples of both print "Coding Dojo".
"""

for i in range(101):
    if i % 5 == 0 and i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)/python/python_fundamentals/coin_tosses.py
"""
Write a function that simulates tossing a coin 5,000 times. 
Your function should print how many times the head/tail appears.
"""

import random

def coin_tosses():
    heads = 0
    tails = 0
    for i in range(5000):
        if random.randint(0,1) == 0:
            heads += 1
        else:
            tails += 1
    print("Heads: " + str(heads))
    print("Tails: " + str(tails))

coin_tosses()/python/python_fundamentals/coin_tosses2.py
"""
Write a function that simulates tossing a coin 5,000 times. 
Your function should print how many times the head/tail appears.
"""

import random

def coin_tosses():
    heads = 0
    tails = 0
    for i in range(5000):
        if random.randint(0,1) == 0:
            heads += 1
        else:
            tails += 1
    print("Heads: " + str(heads))
    print("Tails: " + str(tails))

coin_tosses()

def coin_tosses2():
    heads = 0
    tails = 0
    for i in range(5000):
        if random.randint(0,1) == 0:
            heads += 1
        else:
            tails += 1
    print("Heads: " + str(heads))
    print("Tails: " + str(tails))

coin_tosses2()/python/python_fundamentals/coin_tosses3.py
"""
Write a function that simulates tossing a coin 5,000 times. 
Your function should print how many times the head/tail appears.
"""

import random

def coin_tosses():
    heads = 0
    tails = 0
    for i in range(5000):
        if random.randint(0,1) == 0:
            heads += 1
        else:
            tails += 1
    print("Heads: " + str(heads))
    print("Tails: " + str(tails))

coin_tosses()

def coin_tosses2():
    heads = 0
    tails = 0
    for i in range(5000):
        if random.randint(0,1) == 0:
            heads += 1
        else:
            tails += 1
    print("Heads: " + str(heads))
    print("Tails: " + str(tails))

coin_tosses2()

def coin_tosses3():
    heads = 0
    tails = 0
    for i in range(5000):
        if random.randint(0,1) == 0:
            heads += 1
        else:
            tails += 1
    print("Heads: " + str(heads))
    print("Tails: " + str(tails))

coin_tosses3()/python/python_fundamentals/coin_tosses4.py
"""
Write a function that simulates tossing a coin 5,000 times. 
Your function should print how many times the head/tail appears.
"""

import random

def coin_tosses():
    heads = 0
    tails = 0
    for i in range(5000):
        if random.randint(0,1) ==