"""
Write a function that takes in a list and an integer n and splits a list for every nth element, returning a list of the resulting lists.
assert list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n'],3)==[['a', 'd', 'g', 'j','m'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
"""

def list_split(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

print(list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n'],3))
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
Tossing Coins
Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
Sample output should be like the following:
Starting the program...
Attempt #1: Throwing a coin... It's a head!... Got 1 head(s) so far and 0 tail(s) so far
Attempt #2: Throwing a coin... It's a head!... Got 2 head(s) so far and 0 tail(s) so far
Attempt #3: Throwing a coin... It's a tail!... Got 2 head(s) so far and 1 tail(s) so far
Attempt #4: Throwing a coin... It's a head!... Got 3 head(s) so far and 1 tail(s) so far
Attempt #5: Throwing a coin... It's a head!... Got 4 head(s) so far and 1 tail(s) so far
...
Attempt #5000: Throwing a coin... It's a head!... Got 2412 head(s) so far and 2588 tail(s) so far
Ending the program, thank you!
"""

import random

def coin_tosses():
    heads = 0
    tails = 0
    for i in range(1, 5001):
        print("Attempt #{}: Throwing a coin...".format(