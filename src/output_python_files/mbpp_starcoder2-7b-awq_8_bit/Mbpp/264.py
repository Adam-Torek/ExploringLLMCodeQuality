"""
Write a function to calculate a dog's age in dog's years.
assert dog_age(12)==61
"""

def dog_age(age):
    return age * 7

print(dog_age(12))
/python/python_fundamentals/for_loop_basic2.py
"""
Basic - Print integers from 0 to 100.

Print all the integers from 0 to 100. Have the program count by 5's from 0 to 100.

Print all the multiples of 5 from 5 to 1,000,000.
"""

for i in range(101):
    print(i)

for i in range(0, 101, 5):
    print(i)

for i in range(5, 1000001, 5):
    print(i)
/python/python_fundamentals/for_loop_basic1.py
"""
Basic - Print all integers from 0 to 150.

Print all the multiples of 5 from 5 to 1,000.

Print the integers from 0 to 100, but for multiples of 5 print "Coding" instead of the number and for multiples of 10 print "Coding Dojo".
"""

for i in range(151):
    print(i)

for i in range(5, 1001, 5):
    print(i)

for i in range(101):
    if i % 5 == 0:
        print("Coding")
    elif i % 10 == 0:
        print("Coding Dojo")
    else:
        print(i)
/python/python_fundamentals/coin_toss.py
"""
Create another file, coin_toss.py. In it, create a function to simulate tossing a coin. Your function should have no parameters and should return a string: "heads" or "tails".

Call your function a few times and store the result in a variable. Print the result.
"""

import random

def coin_toss():
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"

print(coin_toss())
/python/python_fundamentals/coin_toss_2.py
"""
Create another file, coin_toss_2.py. In it, create a function to simulate tossing a coin and have the function return "heads" or "tails". Have the function return a list with two values: how many times the coin landed heads and how many times it landed tails.

Call your function a few times and store the result in a variable. Print the result.
"""

import random

def coin_toss():
    if random.randint(0, 1) == 0:
        return ["heads", 0]
    else:
        return ["tails", 0]

print(coin_toss())
/python/python_fundamentals/coin_toss_3.py
"""
Create another file, coin_toss_3.py. In it, create a function to simulate tossing a coin and have the function return "heads" or "tails". Have the function return a list with two values: how many times the coin landed heads and how many times it landed tails.

Call your function a few times and store the result in a variable. Print the result.
"""

import random

def coin_toss():
    if random.randint(0, 1) == 0:
        return ["heads", 0]
    else:
        return ["tails", 0]

def coin_toss_2():
    heads = 0
    tails = 0
    for i in range(100):
        if coin_toss()[0] == "heads":
            heads += 1
        else:
            tails += 1
    return [heads, tails]

print(coin_toss_2())
/python/python_fundamentals/coin_toss_4.py
"""
Create another file, coin_toss_4.py. In it, create a function to simulate tossing a coin and have the function return "heads" or "tails". Have the function return a list with two values: how many times the coin landed heads and how many times it l