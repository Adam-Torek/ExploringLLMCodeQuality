"""
Write a function to find the n most expensive items in a given dataset.
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
"""

def expensive_items(items, n):
    return sorted(items, key=lambda item: item['price'], reverse=True)[:n]

print expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)
/python/python_fundamentals/coin_toss.py
import random

def coin_toss():
    heads = 0
    tails = 0
    for i in range(1,5001):
        if random.randint(0,1) == 0:
            heads += 1
            print "Attempt #{}: Throwing a coin... It's a head!... Got {} head(s) so far and {} tail(s) so far".format(i, heads, tails)
        else:
            tails += 1
            print "Attempt #{}: Throwing a coin... It's a tail!... Got {} head(s) so far and {} tail(s) so far".format(i, heads, tails)

coin_toss()
/python/python_fundamentals/coin_toss_2.py
import random

def coin_toss():
    heads = 0
    tails = 0
    for i in range(1,5001):
        if random.randint(0,1) == 0:
            heads += 1
            print "Attempt #{}: Throwing a coin... It's a head!... Got {} head(s) so far and {} tail(s) so far".format(i, heads, tails)
        else:
            tails += 1
            print "Attempt #{}: Throwing a coin... It's a tail!... Got {} head(s) so far and {} tail(s) so far".format(i, heads, tails)
    print "Ending the program, thank you!"

coin_toss()
/python/python_fundamentals/coin_toss_3.py
import random

def coin_toss():
    heads = 0
    tails = 0
    for i in range(1,5001):
        if random.randint(0,1) == 0:
            heads += 1
            print "Attempt #{}: Throwing a coin... It's a head!... Got {} head(s) so far and {} tail(s) so far".format(i, heads, tails)
        else:
            tails += 1
            print "Attempt #{}: Throwing a coin... It's a tail!... Got {} head(s) so far and {} tail(s) so far".format(i, heads, tails)
    print "Ending the program, thank you!"
    if heads > tails:
        print "The winner is heads!"
    elif tails > heads:
        print "The winner is tails!"
    else:
        print "The winner is a tie!"

coin_toss()
/python/python_fundamentals/stars.py
def draw_stars(arr):
    for i in arr:
        if type(i) == int:
            print "*" * i
        else:
            print i[0].lower() * len(i)

draw_stars([4, "Tom", 1, "Michael", 5, 7, ""])
/python/python_fundamentals/stars_2.py
def draw_stars(arr):
    for i in arr:
        if type(i) == int:
            print "*" * i
        else:
            print i[0].lower() * len(i)

draw_stars([4, "Tom", 1, "Michael", 5, 7, ""])

def draw_stars_2(arr):
    for i in arr:
        if type(i) == int:
            print "*" * i
        else:
            print i[0].upper() * len(i)

draw_stars_2([4, "Tom", 1, "Michael", 5, 7, ""])
/python/python_fundamentals/stars_3.py
def draw_stars(arr):
    for i in arr: