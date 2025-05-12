"""
Write a python function that takes in an integer n and returns the sum of the squares of the first n odd natural numbers.
assert square_Sum(2) == 10
"""

def square_Sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**2
    return sum

print(square_Sum(2))
/python/python_fundamentals/for_loop_basic2.py
"""
Write a function that counts from 1 to 2000.  As it loops through each number, have your program print "Even" if the current number is even.  Otherwise, print "Odd".
"""

def count_to_2000():
    for i in range(1, 2001):
        if i % 2 == 0:
            print("Even")
        else:
            print("Odd")

count_to_2000()
/python/python_fundamentals/coin_toss.py
"""
Create another file, coin_toss.py.  In this file, create a function that simulates tossing a coin 5,000 times.  Your function should print how many times the head/tail appears.
"""

import random

def coin_toss():
    heads = 0
    tails = 0
    for i in range(1, 5001):
        if random.randint(0, 1) == 0:
            heads += 1
            print("Attempt #{}: Throwing a coin... It's a head!... Got {} head(s) so far and {} tail(s) so far".format(i, heads, tails))
        else:
            tails += 1
            print("Attempt #{}: Throwing a coin... It's a tail!... Got {} head(s) so far and {} tail(s) so far".format(i, heads, tails))

coin_toss()
/python/python_fundamentals/coin_toss_2.py
"""
Create another file, coin_toss_2.py.  In this file, create another function that simulates tossing a coin 5,000 times.  Your function should print how many times the head/tail appears.  Your function should also print what the result would be if the value toss() returned either a 1 or 0.  You should call your function and see that it works.
"""

import random

def coin_toss():
    heads = 0
    tails = 0
    for i in range(1, 5001):
        if random.randint(0, 1) == 0:
            heads += 1
            print("Attempt #{}: Throwing a coin... It's a head!... Got {} head(s) so far and {} tail(s) so far".format(i, heads, tails))
        else:
            tails += 1
            print("Attempt #{}: Throwing a coin... It's a tail!... Got {} head(s) so far and {} tail(s) so far".format(i, heads, tails))
    if heads > tails:
        print("Heads")
    else:
        print("Tails")

coin_toss()
/python/python_fundamentals/coin_toss_3.py
"""
Create another file, coin_toss_3.py.  In this file, create another function that simulates tossing a coin 5,000 times.  Your function should print how many times the head/tail appears.  Your function should also print what the result would be if the value toss() returned either a 1 or 0.  You should call your function and see that it works.
"""

import random

def coin_toss():
    heads = 0
    tails = 0
    for i in range(1, 5001):
        if random.randint(0, 1) == 0:
            heads += 1
            print("Attempt #{}: Throwing a coin... It's a head!... Got {} head(s) so far and {} tail(s) so far".format(i, heads, tails))
        else:
            tails += 1
            print("Attempt #{}: Throwing a coin... It's a tail!... Got {} head(s) so far and {} tail(s) so far".format(i, heads, tails))
    if heads > tails:
        print("Heads")
    else:
        print("