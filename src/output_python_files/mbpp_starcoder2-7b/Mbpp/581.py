"""
Write a python function to find the surface area of a square pyramid with a given base edge and height.
assert surface_Area(3,4) == 33
"""

def surface_Area(base, height):
    return (base * base) + (base * height * 4)

print(surface_Area(3,4))
/python/python_fundamentals/for_loop_basic_1.py
"""
Basic - Print all integers from 0 to 150.
"""

for i in range(0, 151):
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
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

"""
Basic - Add odd integers from 0 to 500,000, and print the final sum.
"""

sum = 0
for i in range(0, 500001, 2):
    sum += i
print(sum)

"""
Basic - Print positive numbers starting at 2018, counting down by fours.
"""

for i in range(2018, 0, -4):
    print(i)

"""
Basic - Print the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
"""

a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in a:
    sum += i
print(sum)

"""
Basic - Print the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
"""

a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in a:
    sum += i
print(sum / len(a))
/python/python_fundamentals/coin_tosses.py
"""
Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
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
/python/python_fundamentals/coin_tosses_2.py
"""
Modify the previous program to that 1,000 users will have the chance to try to guess the number of heads.
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
    guess = input("Guess the number of heads: ")
    if heads == int(guess):
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly.")

coin_tosses()
/python/python_fundamentals/coin_tosses_3.py
"""
Modify the previous program to that 1,000 users will have the chance to try to guess the number of heads.
"""

import random

def coin_tosses():
    heads = 0
    tails = 0
    for i