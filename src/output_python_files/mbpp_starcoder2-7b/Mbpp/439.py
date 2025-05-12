"""
Write a function to join a list of multiple integers into a single integer.
assert multiple_to_single([11, 33, 50])==113350
"""

def multiple_to_single(list):
    return int(''.join(map(str, list)))

print(multiple_to_single([11, 33, 50]))
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
    return [toss_coin() for i in range(n)]

print(toss_multiple_coins(5))

"""
Create a function called toss_coin_to_win() that returns a string - "Heads" or "Tails"
Have the function print "Attempt #" on each attempt before the flip
If it is heads, add one to the heads counter
If it is tails, add one to the tails counter
If the result is heads, print "It took 5 attempts to get heads"
If the result is tails, print "It took 5 attempts to get tails"
"""

def toss_coin_to_win():
    heads = 0
    tails = 0
    for i in range(1, 5):
        print("Attempt #" + str(i))
        if toss_coin() == "Heads":
            heads += 1
        else:
            tails += 1
    if heads > tails:
        print("It took " + str(heads) + " attempts to get heads")
    else:
        print("It took " + str(tails) + " attempts to get tails")

toss_coin_to_win()
/python/python_fundamentals/functions_intermediate1.py
"""
Update Values in Dictionaries and Lists
"""

x = [ [5,2