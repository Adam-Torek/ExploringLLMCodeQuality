"""
Write a function which takes two tuples of the same length and performs the element wise modulo.
assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)
"""

def tuple_modulo(tup1, tup2):
    return tuple(map(lambda x, y: x % y, tup1, tup2))

print(tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)))
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

for i in range(5, 1000001):
    if i % 5 == 0:
        print(i)

for i in range(1, 101):
    if i % 5 == 0:
        print("Coding")
    else:
        print(i)

for i in range(1, 101):
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
        if random.randint(0, 1) == 0:
            heads += 1
        else:
            tails += 1
    print("Heads: " + str(heads))
    print("Tails: " + str(tails))

coin_toss()
/python/python_fundamentals/coin_toss_2.py
"""
Create another function that simulates tossing a coin 5,000 times. Your function should print the percentage of head/tails.
"""

import random

def coin_toss():
    heads = 0
    tails = 0
    for i in range(1, 5001):
        if random.randint(0, 1) == 0:
            heads += 1
        else:
            tails += 1
    print("Heads: " + str(heads))
    print("Tails: " + str(tails))
    print("Percentage of Heads: " + str(heads / 5000))
    print("Percentage of Tails: " + str(tails / 5000))

coin_toss()
/python/python_fundamentals/coin_toss_3.py
"""
Create another function that simulates tossing a coin 5,000 times. Your function should return the percentage of head/tails.
"""

import random

def coin_toss():
    heads = 0
    tails = 0
    for i in range(1, 5001):
        if random.randint(0, 1) == 0:
            heads += 1
        else:
            tails += 1
    return heads / 5000, tails / 5000

print(coin_toss())
/python/python_fundamentals/coin_toss_4.py
"""
Create a function that simulates tossing a coin 5,000 times. Your function should return the percentage of head/tails.
"""

import random

def coin_toss():
    heads = 0
    tails = 0
    for i in range(1,