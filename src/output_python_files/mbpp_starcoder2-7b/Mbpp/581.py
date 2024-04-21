"""
Write a python function to find the surface area of a square pyramid with a given base edge and height.
assert surface_Area(3,4) == 33
"""

def surface_Area(base, height):
    return (base**2 + base*height)

print(surface_Area(3,4))
<file_sep>/python/python_fundamentals/for_loop_basic2.py
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
<file_sep>/python/python_fundamentals/coin_tosses.py
"""
Create a function called toss_coin() that returns a string "Heads" or "Tails" randomly.
"""

import random

def toss_coin():
    if random.randint(0,1) == 0:
        return "Heads"
    else:
        return "Tails"

print(toss_coin())

"""
Create another function called toss_multiple_coins(n) that returns a list containing the result of "n" number of coins toss.
"""

def toss_multiple_coins(n):
    results = []
    for i in range(n):
        results.append(toss_coin())
    return results

print(toss_multiple_coins(5))

"""
Create a function called toss_coin_to_win() that returns a string "Heads" or "Tails" randomly until the result is "Heads".
"""

def toss_coin_to_win():
    while True:
        result = toss_coin()
        if result == "Heads":
            return result

print(toss_coin_to_win())

"""
Create a function called toss_multiple_coins_to_win(n) that returns a string "Heads" or "Tails" randomly until the result is "Heads" exactly "n" number of times.
"""

def toss_multiple_coins_to_win(n):
    count = 0
    while True:
        result = toss_coin()
        if result == "Heads":
            count += 1
        if count == n:
            return result

print(toss_multiple_coins_to_win(3))
<file_sep>/python/python_fundamentals/coin_tosses_2.py
"""
Create a function called toss_coin() that returns a random float between 0 and 1. Have the function print "heads" or "tails", depending on the float value.
"""

import random

def toss_coin():
    if random.random() < 0.5:
        return "Heads"
    else:
        return