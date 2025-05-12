"""
Write a function to append the given list to the given tuples.
assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
"""

def add_lists(list1, tuple1):
    return tuple1 + tuple(list1)

print(add_lists([5, 6, 7], (9, 10)))
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
Create another function called toss_multiple_coins(x) that returns a list with the string 'head' or 'tail' values.
x is the number of coins to be tossed.
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

def toss_multiple_coins(x):
    list = []
    for i in range(1, x + 1):
        if random.randint(0, 1) == 0:
            list.append("head")
        else:
            list.append("tail")
    return list

coin_toss()
print(toss_multiple_coins(50))
/python/python_fundamentals/coin_toss_3.py
"""
Create another function called toss_multiple_coins(x) that returns a list with the string 'head' or 'tail' values.
x is the number of coins to be tossed.
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

def toss_multiple_coins(x):
    list = []
    for i in range(1, x + 1):
        if random.randint(0, 1) == 0:
            list.append("head")
        else:
            list.append("tail")
    return list

def toss_multiple_coins_2(x):