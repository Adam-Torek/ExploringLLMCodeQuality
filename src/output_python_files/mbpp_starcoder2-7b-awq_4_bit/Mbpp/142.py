"""
Write a function to count number items that are identical in the same position of three given lists.
assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
"""

def count_samepair(list1, list2, list3):
    count = 0
    for i in range(len(list1)):
        if list1[i] == list2[i] == list3[i]:
            count += 1
    return count

print(count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9]))
/python/python_fundamentals/for_loop_basic2.py
"""
Print integers from 0 to 100. If divisible by 5 print "Coding" instead. If divisible by 10 print "Coding Dojo".
"""

for i in range(101):
    if i % 5 == 0 and i % 10!= 0:
        print("Coding")
    elif i % 10 == 0:
        print("Coding Dojo")
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
Write a function that simulates tossing a coin 5,000 times. Your function should print the number of heads and tails and the percentage of head/tails.
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
    print("Percentage of heads: " + str(heads/5000))
    print("Percentage of tails: " + str(tails/5000))

coin_tosses()
/python/python_fundamentals/coin_tosses3.py
"""
Write a function that simulates tossing a coin 5,000 times. Your function should return the percentage of heads.
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
    return heads/5000

print(coin_tosses())
/python/python_fundamentals/coin_tosses4.py
"""
Write a function that simulates tossing a coin 5,000 times. Your function should return the percentage of heads.
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
    return heads/5000

print(coin_tosses())

def coin_tosses2():
    heads = 0
    tails = 0
    for i in range(5000):
        if random.randint(0,1) == 0:
            heads += 1
        else:
            tails += 1
    return heads/5000

print(coin_tosses2())

def coin_tosses3():
    heads = 0
    tails = 0
    for i in range(5000):