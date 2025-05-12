"""
Write a function to sort each sublist of strings in a given list of lists.
assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
"""

def sort_sublists(lst):
    for i in range(len(lst)):
        lst[i].sort()
    return lst

print(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]))
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
Creating a Coin Class - Create a class Coin that has two instance attributes: heads and tails. Create an instance method called toss that flips the coin once and changes heads or tails accordingly. Create another instance method called flip that flips the coin once and changes heads or tails accordingly.
"""

import random

class Coin:
    def __init__(self):
        self.heads = 0
        self.tails = 0

    def toss(self):
        toss = random.randint(0, 1)
        if toss == 0:
            self.heads += 1
        else:
            self.tails += 1

    def flip(self):
        toss = random.randint(0, 1)
        if toss == 0:
            self.heads += 1
        else:
            self.tails += 1

coin = Coin()
coin.toss()
coin.toss()
coin.toss()
coin.flip()
coin.flip()
coin.flip()
print(coin.heads)
print(coin.tails)

"""
Flipping the Coin - Write a function called flip_coin() that returns the string