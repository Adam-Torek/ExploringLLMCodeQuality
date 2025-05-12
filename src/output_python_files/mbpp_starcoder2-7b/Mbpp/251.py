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
/python/python_fundamentals/for_loop_basic_1.py
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
for i in range(500001):
    if i % 2!= 0:
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
Create another function called toss_multiple_coins(n) that returns a list. Each element in the list should be a string of "Heads" or "Tails" randomly, based on the input parameter n.
"""

def toss_multiple_coins(n):
    list = []
    for i in range(n):
        list.append(toss_coin())
    return list

print(toss_multiple_coins(5))

"""
Create a function called toss_coin_to_win() that returns a string of "Heads" or "Tails", depending on the toss. If it's "Heads", return "Heads", otherwise return "Tails".
"""

def toss_coin_to_win():
    if toss_coin() == "Heads":
        return "Heads"
    else:
        return "Tails"

print(toss_coin_to_win())

"""
Create a function called toss_multiple_coins_to_win(n) that returns a string of "Heads" or "Tails", depending on the toss. If it's "Heads", return "Heads", otherwise return "Tails".
"""

def toss_multiple_coins_to_win(n):
    list = []
    for i in range(n):
        list.append(toss_coin