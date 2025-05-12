"""
Write a python function to set all even bits of a given number.
assert even_bit_set_number(10) == 10
"""

def even_bit_set_number(num):
    return num | 0b10101010101010101010101010101010

print(even_bit_set_number(10))
/python/python_fundamentals/for_loop_basic1.py
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
/python/python_fundamentals/coin_toss.py
"""
Create a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
"""

import random

def coin_toss():
    heads = 0
    tails = 0
    for i in range(1, 5001):
        if random.randint(0, 1) == 0:
            heads += 1
        else:
            tails += 1
    print("Heads: " + str(heads))
    print("Tails: " + str(tails))

coin_toss()
/python/python_fundamentals/coin_toss_2.py
"""
Create another function that simulates tossing a coin 5,000 times. Your function should print the number of heads and tails and should return the percentage of head.
"""

import random

def coin_toss():
    heads = 0
    tails = 0
    for i in range(1, 5001):
        if random.randint(0, 1) == 0:
            heads += 1
        else:
            tails += 1
    print("Heads: " + str(heads))
    print("Tails: " + str(tails))
    return heads / (heads + tails)

print(coin_toss())
/python/python_fundamentals/coin_toss_3.py
"""
Create a function that simulates tossing a coin 5,000 times. Your function should return the percentage of head.
"""

import random

def coin_toss():
    heads = 0
    tails = 0
    for i in range(1, 5001):
        if random.randint(0, 1) == 0:
            heads += 1
        else:
            tails += 1
    return heads / (heads + tails)

print(coin_to