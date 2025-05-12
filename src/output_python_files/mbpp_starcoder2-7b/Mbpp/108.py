"""
Write a function to merge three lists into a single sorted list.
assert merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48])==[4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233]
"""

def merge_sorted_list(list1, list2, list3):
    return sorted(list1 + list2 + list3)

print(merge_sorted_list([25, 24, 15, 4, 5, 29, 110],[19, 20, 11, 56, 25, 233, 154],[24, 26, 54, 48]))
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
Toss Multiple Coins - Create another function called tossMultipleCoins(num) that returns a list of strings of "head" or "tails" that is the length of the input num.
"""

def tossMultipleCoins(num):
    return [tossCoin() for i in range(num)]

print(tossMultipleCoins(5))

"""
Call tossMultipleCoins(x) and store the value in a variable called coins.
"""

coins = tossMultipleCoins(5)
print(coins)

"""
If you actually got more heads than tails, print "You got more heads!" If you got the same number of heads and tails, print "You got the same number of heads and tails!" If you got more tails than heads, print "You got