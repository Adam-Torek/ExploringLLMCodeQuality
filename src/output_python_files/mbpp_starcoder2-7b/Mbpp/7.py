"""
Write a function to find all words which are at least 4 characters long in a string.
assert set(find_char_long('Please move back to stream')) == set(['Please','move', 'back','stream'])
"""

def find_char_long(string):
    return [word for word in string.split() if len(word) >= 4]

print(find_char_long('Please move back to stream'))
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
Toss Coin - Create a function called tossCoin() that returns a string "Heads" or "Tails" randomly.
"""

import random

def tossCoin():
    if random.randint(0, 1) == 0:
        return "Heads"
    else:
        return "Tails"

print(tossCoin())

"""
Toss Multiple Coins - Create another function called tossMultipleCoins(num) that returns a list of strings of "head" or "tail" that is the length of the input parameter num.
"""

def tossMultipleCoins(num):
    return [tossCoin() for i in range(num)]

print(tossMultipleCoins(5))

"""
Call tossMultipleCoins with 500 and save the results to a variable called coins.
"""

coins = tossMultipleCoins(500)

"""
Create another function called getCount(lst) that takes in a list of strings and returns a dictionary with the key "heads" and the value being the number of heads in the list, and key "tails" and the value being the number of tails.
"""

def getCount(lst):
    return {
        "heads": lst.count("Heads"),
        "tails": lst.count("Tails")
    }

print(getCount(coins))

"""
Create another function called tossMultipleCoins(num) that returns a list of strings of "head" or "tail" that is the length of the input parameter num. Then, create another function called getCount(lst) that takes in a list of strings and returns a dictionary with the key "heads" and the value being the number of heads in the list, and key "tails" and the value being the number of tails.
"""