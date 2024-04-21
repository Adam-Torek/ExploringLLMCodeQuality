"""
Write a function to find the intersection of two arrays.
assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
"""

def intersection_array(arr1, arr2):
    result = []
    for i in arr1:
        if i in arr2:
            result.append(i)
    return result

print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9]))
<file_sep>/python/python_fundamentals/for_loop_basic2.py
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
<file_sep>/python/python_fundamentals/coin_tosses.py
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
Create another function called toss_multiple_coins(n) that returns a list containing the result of "n" number of coins tossing experiments where each coin toss will have a result of either "Heads" or "Tails".
"""

def toss_multiple_coins(n):
    result = []
    for i in range(n):
        result.append(toss_coin())
    return result

print(toss_multiple_coins(5))

"""
Create a function called toss_coin_multiple_times(n) that calls the toss_coin function multiple times and returns a dictionary containing the number of heads and tails.
"""

def toss_coin_multiple_times(n):
    heads = 0
    tails = 0
    for i in range(n):
        if toss_coin() == "Heads":
            heads += 1
        else:
            tails += 1
    return {"heads": heads, "tails": tails}

print(toss_coin_multiple_times(50))
<file_sep>/python/python_fundamentals/coin_tosses_2.py
"""
Create a function called toss_coin() that returns a string "Heads" or "Tails" randomly.
"""

import random

def toss_coin():
    if random.