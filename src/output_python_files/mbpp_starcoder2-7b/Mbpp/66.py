"""
Write a python function to count the number of positive numbers in a list.
assert pos_count([1,-2,3,-4]) == 2
"""

def pos_count(list):
    count = 0
    for i in list:
        if i > 0:
            count += 1
    return count

print(pos_count([1,-2,3,-4]))
/python/python_fundamentals/for_loop_basic2.py
"""
Basic - Print all integers from 0 to 150.
"""

for i in range(0,151):
    print(i)

"""
Multiples of Five - Print all the multiples of 5 from 5 to 1,000
"""

for i in range(5,1001,5):
    print(i)

"""
Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
"""

for i in range(1,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

"""
Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
"""

sum = 0
for i in range(0,500001,2):
    sum += i
print(sum)

"""
Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
"""

for i in range(2018,0,-4):
    print(i)

"""
Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
"""

lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum,highNum+1):
    if i % mult == 0:
        print(i)
/python/python_fundamentals/coin_tosses.py
"""
Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
"""

import random

def coin_tosses():
    heads = 0
    tails = 0
    for i in range(1,5001):
        toss = random.randint(0,1)
        if toss == 0:
            heads += 1
        else:
            tails += 1
    print("Heads: " + str(heads))
    print("Tails: " + str(tails))

coin_tosses()
/python/python_fundamentals/coin_tosses2.py
"""
Write a function that simulates tossing a coin 5,000 times. Your function should print the number of heads and tails. Return the percentage of head/tails as a two-tuple. In other words, return the percentage of heads and the percentage of tails. If the side that is chosen is head, have the function return "head". If the side that is chosen is tail, have the function return "tail".
"""

import random

def coin_tosses():
    heads = 0
    tails = 0
    for i in range(1,5001):
        toss = random.randint(0,1)
        if toss == 0:
            heads += 1
        else:
            tails += 1
    print("Heads: " + str(heads))
    print("Tails: " + str(tails))
    return (heads/5000, tails/5000)

print(coin_tosses())
/python/python_fundamentals/coin_tosses3.py
"""
Write a function that simulates tossing a pair of dice 5,000 times. Your function should print each instance of the dice roll (ex. "You rolled a 4 and a 6").
"""

import random

def dice_roll():
    for i