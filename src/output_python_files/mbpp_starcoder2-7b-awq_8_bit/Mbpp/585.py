"""
Write a function to find the n most expensive items in a given dataset.
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
"""

def expensive_items(items, n):
    return sorted(items, key=lambda x: x['price'], reverse=True)[:n]

print expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)
/python/python_fundamentals/coin_toss.py
import random

def coin_toss():
    heads = 0
    tails = 0
    for i in range(1,5001):
        if random.randint(0,1) == 0:
            heads += 1
        else:
            tails += 1
    print "Attempt #" + str(i) + ": " + "heads: " + str(heads) + " tails: " + str(tails) + " " + "difference: " + str(abs(heads-tails))

coin_toss()
/python/python_fundamentals/coin_toss_2.py
import random

def coin_toss():
    heads = 0
    tails = 0
    for i in range(1,5001):
        if random.randint(0,1) == 0:
            heads += 1
        else:
            tails += 1
    print "Attempt #" + str(i) + ": " + "heads: " + str(heads) + " tails: " + str(tails) + " " + "difference: " + str(abs(heads-tails))

coin_toss()

def coin_toss_2():
    heads = 0
    tails = 0
    for i in range(1,5001):
        if random.randint(0,1) == 0:
            heads += 1
        else:
            tails += 1
    print "Attempt #" + str(i) + ": " + "heads: " + str(heads) + " tails: " + str(tails) + " " + "difference: " + str(abs(heads-tails))

coin_toss_2()
/python/python_fundamentals/coin_toss_3.py
import random

def coin_toss():
    heads = 0
    tails = 0
    for i in range(1,5001):
        if random.randint(0,1) == 0:
            heads += 1
        else:
            tails += 1
    print "Attempt #" + str(i) + ": " + "heads: " + str(heads) + " tails: " + str(tails) + " " + "difference: " + str(abs(heads-tails))

coin_toss()

def coin_toss_2():
    heads = 0
    tails = 0
    for i in range(1,5001):
        if random.randint(0,1) == 0:
            heads += 1
        else:
            tails += 1
    print "Attempt #" + str(i) + ": " + "heads: " + str(heads) + " tails: " + str(tails) + " " + "difference: " + str(abs(heads-tails))

coin_toss_2()

def coin_toss_3():
    heads = 0
    tails = 0
    for i in range(1,5001):
        if random.randint(0,1) == 0:
            heads += 1
        else:
            tails += 1
    print "Attempt #" + str(i) + ": " + "heads: " + str(heads) + " tails: " + str(tails) + " " + "difference: " + str(abs(heads-tails))

coin_toss_3()
/python/python_fundamentals/coin_toss_4.py
import random

def coin_toss():
    heads = 0
    tails = 0
    for i in range(1,5001):
        if random.randint(0,1