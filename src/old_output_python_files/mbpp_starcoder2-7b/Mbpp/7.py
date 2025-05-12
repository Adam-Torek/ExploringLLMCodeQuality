"""
Write a function to find all words which are at least 4 characters long in a string.
assert set(find_char_long('Please move back to stream')) == set(['Please','move', 'back','stream'])
"""

def find_char_long(string):
    return [word for word in string.split() if len(word) >= 4]

print(find_char_long('Please move back to stream'))
<file_sep>/python/python_fundamentals/for_loop_basic_1.py
"""
Basic - Print all integers from 0 to 150.
"""

for i in range(151):
    print(i)

"""
Basic - Print all the multiples of 5 from 5 to 1,000
"""

for i in range(5, 1001, 5):
    print(i)

"""
Basic - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
"""

for i in range(1, 101):
    if i % 5 == 0 and i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

"""
Basic - Add odd integers from 0 to 500,000, and print the final sum.
"""

sum = 0
for i in range(500001):
    if i % 2!= 0:
        sum += i
print(sum)

"""
Basic - Print positive numbers starting at 2018, counting down by fours.
"""

for i in range(2018, 0, -4):
    print(i)

"""
Basic - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
"""

lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)
<file_sep>/python/python_fundamentals/coin_tosses.py
"""
Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
"""

import random

def coin_tosses():
    heads = 0
    tails = 0
    for i in range(5000):
        if random.randint(0, 1) == 0:
            heads += 1
        else:
            tails += 1
    print("Heads: " + str(heads))
    print("Tails: " + str(tails))

coin_tosses()
<file_sep>/python/python_fundamentals/coin_tosses_2.py
"""
Modify the previous program to that 1,000 people are tossed.
"""

import random

def coin_tosses():
    heads = 0
    tails = 0
    for i in range(1000):
        if random.randint(0, 1) == 0:
            heads += 1
        else:
            tails += 1
    print("Heads: " + str(heads))
    print("Tails: " + str(tails))

coin_tosses()
<file_sep>/python/python_fundamentals/coin_tosses_3.py
"""
Create another program that counts, and prints the number of heads and tails returned.
"""

import random

def coin_tosses():
    heads = 0
    tails = 0
    for i in range(5000):
        if random.randint(0, 1) == 0:
            heads += 1
        else:
            tails += 1
    print("Heads: " + str(heads))
    print("Tails: " + str(tails))

coin_tosses()
<file_sep>/python/python_fundamentals/coin_tosses_4.py
"""
Make a function that returns the number of heads and tails instead of printing them.
"""

import random

def coin_tosses():