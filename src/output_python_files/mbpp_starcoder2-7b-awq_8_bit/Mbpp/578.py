"""
Write a function to interleave 3 lists of the same length into a single flat list.
assert interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])==[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
"""

def interleave_lists(list1, list2, list3):
    return [list1[i] for i in range(len(list1))] + [list2[i] for i in range(len(list2))] + [list3[i] for i in range(len(list3))]

print(interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700]))
/python/python_fundamentals/for_loop_basic2.py
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
        print(i)
/python/python_fundamentals/coin_tosses.py
"""
Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
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
/python/python_fundamentals/coin_tosses2.py
"""
Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
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
/python/python_fundamentals/coin_tosses3.py
"""
Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
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