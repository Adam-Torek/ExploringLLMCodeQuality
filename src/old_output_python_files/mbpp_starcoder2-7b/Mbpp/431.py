"""
Write a function that takes two lists and returns true if they have at least one common element.
assert common_element([1,2,3,4,5], [5,6,7,8,9])==True
"""

def common_element(list1, list2):
    for i in list1:
        if i in list2:
            return True
    return False

print(common_element([1,2,3,4,5], [5,6,7,8,9]))
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
Tossing Coins - Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
"""

import random

def coin_tosses():
    heads = 0
    tails = 0
    for i in range(1, 5001):
        toss = random.randint(0, 1)
        if toss == 0:
            heads += 1
        else:
            tails += 1
    print("Heads: " + str(heads))
    print("Tails: " + str(tails))

coin_tosses()

"""
Creating a Coin Class - Create a class Coin that has two attributes: side and value. The side attribute should be either 'heads' or 'tails'. The value attribute should be either 1 or 0. The class should also have a method called toss that sets the side attribute to either 'heads' or 'tails' randomly.
"""

import random

class Coin:
    def __init__(self):
        self.side = ""
        self.value = 0

    def toss(self):
        toss = random.randint(0, 1)
        if toss == 0:
            self.side = "heads"
            self.value = 1
        else:
            self.side = "tails"
            self.value = 0

coin = Coin()
coin.toss()
print(coin.side)
print(coin.value)

"""
Flipping a Coin - Write a function called flip_coin() that returns a string 'heads' or 'tails'. Have the function print the string 'heads' or 'tails', and return the value.
"""

import random

def flip_coin():
    toss = random.randint(0, 1)
    if toss == 0:
        return "heads