"""
Write a function to multiply all the numbers in a list and divide with the length of the list.
assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
"""

def multiply_num(list):
    return reduce(lambda x, y: x * y, list) / len(list)

print multiply_num((8, 2, 3, -1, 7))
/python/python_fundamentals/coin_toss.py
"""
Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
"""

import random

def coin_toss():
    head = 0
    tail = 0
    for i in range(5000):
        if random.randint(0, 1) == 0:
            head += 1
        else:
            tail += 1
    print "Heads: " + str(head)
    print "Tails: " + str(tail)

coin_toss()
/python/python_fundamentals/coin_toss_2.py
"""
Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
"""

import random

def coin_toss():
    head = 0
    tail = 0
    for i in range(5000):
        if random.randint(0, 1) == 0:
            head += 1
        else:
            tail += 1
    print "Heads: " + str(head)
    print "Tails: " + str(tail)

coin_toss()

def coin_toss_2():
    head = 0
    tail = 0
    for i in range(5000):
        if random.randint(0, 1) == 0:
            head += 1
        else:
            tail += 1
    print "Heads: " + str(head)
    print "Tails: " + str(tail)

coin_toss_2()
/python/python_fundamentals/coin_toss_3.py
"""
Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
"""

import random

def coin_toss():
    head = 0
    tail = 0
    for i in range(5000):
        if random.randint(0, 1) == 0:
            head += 1
        else:
            tail += 1
    print "Heads: " + str(head)
    print "Tails: " + str(tail)

coin_toss()

def coin_toss_2():
    head = 0
    tail = 0
    for i in range(5000):
        if random.randint(0, 1) == 0:
            head += 1
        else:
            tail += 1
    print "Heads: " + str(head)
    print "Tails: " + str(tail)

coin_toss_2()

def coin_toss_3():
    head = 0
    tail = 0
    for i in range(5000):
        if random.randint(0, 1) == 0:
            head += 1
        else:
            tail += 1
    print "Heads: " + str(head)
    print "Tails: " + str(tail)

coin_toss_3()
/python/python_fundamentals/coin_toss_4.py
"""
Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
"""

import random

def coin_toss():
    head = 0
    tail = 0
    for i in range(5000):
        if random.randint(0, 1) == 0:
            head += 1
        else:
            tail += 1
    print "Heads: " + str(head)
    print "Tails: " + str(tail)

coin_toss()

def coin_toss_2():
    head = 0
    tail = 0
    for i in range(5000):
        if random.randint(0, 1) == 0: