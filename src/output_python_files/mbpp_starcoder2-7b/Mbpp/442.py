"""
Write a function to find the ration of positive numbers in an array of integers.
assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.54
"""

def positive_count(arr):
    count = 0
    for i in arr:
        if i > 0:
            count += 1
    return count / len(arr)

print(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]))
/python/python_fundamentals/for_loop_basic2.py
"""
Basic - Print all integers from 0 to 150.
"""

for i in range(0, 151):
    print(i)

"""
Multiples of Five - Print all the multiples of 5 from 5 to 1,000
"""

for i in range(5, 1001, 5):
    print(i)

"""
Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
"""

for i in range(1, 101):
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
for i in range(0, 500001, 2):
    sum += i
print(sum)

"""
Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
"""

for i in range(2018, 0, -4):
    print(i)

"""
Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
"""

lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)
/python/python_fundamentals/coin_tosses.py
"""
Create a function called toss_coin() that returns a string "Heads" or "Tails" randomly.
"""

import random

def toss_coin():
    if random.randint(0, 1) == 0:
        return "Heads"
    else:
        return "Tails"

print(toss_coin())

"""
Create another function called toss_multiple_coins(n) that returns a list.
Where n is the number of coins to be tossed.
"""

def toss_multiple_coins(n):
    coins = []
    for i in range(n):
        coins.append(toss_coin())
    return coins

print(toss_multiple_coins(5))

"""
Create a function called toss_coin_to_win() that returns a string - "Heads" or "Tails"
Have the function print the number of tosses it took to toss a head.
"""

def toss_coin_to_win():
    count = 0
    while True:
        count += 1
        if toss_coin() == "Heads":
            return count

print(toss_coin_to_win())
/python/python_fundamentals/coin_tosses_2.py
"""
Create a function called toss_coin() that returns a string "Heads" or "Tails" randomly.
"""

import random

def toss_coin():
    if random.randint(0, 1) == 0:
        return