"""
Write a function that takes in a list and an element and inserts the element before each element in the list, and returns the resulting list.
assert insert_element(['Red', 'Green', 'Black'],'c')==['c', 'Red', 'c', 'Green', 'c', 'Black']
"""

def insert_element(list, element):
    new_list = []
    for i in range(len(list)):
        new_list.append(element)
        new_list.append(list[i])
    return new_list

print(insert_element(['Red', 'Green', 'Black'], 'c'))
<file_sep>/python/python_fundamentals/for_loop_basic_1.py
"""
Basic - Print all integers from 0 to 150.
"""

for i in range(151):
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
    for i in range(5000):
        if random.randint(0, 1) == 0:
            heads += 1
        else:
            tails += 1
    print("Heads: " + str(heads))
    print("Tails: " + str(tails))

coin_tosses()

"""
Toss Multiple Coins - Similar to above, but now create a function that takes in the number of coins to flip and the number of heads or tails to be returned.
"""

import random

def coin_tosses(num_coins, num_heads):
    heads = 0
    tails = 0
    for i in range(num_coins):
        if random.randint(0, 1) == 0:
            heads += 1
        else:
            tails += 1
    if heads == num_heads:
        print("Heads: " + str(heads))
        print("Tails: " + str(tails))
    else:
        print("Heads: " + str(heads))
        print("Tails: " + str(tails))

coin_tosses(5000, 2500)
<file_sep>/python/python_fundamentals/functions_intermediate_1.py
"""
Update Values in Dictionary and List - Write a function that takes a dictionary and a key, and returns the value of that key (if it exists). Or if it doesn't, inserts the key with a value of "1" and returns 1.
"""

def