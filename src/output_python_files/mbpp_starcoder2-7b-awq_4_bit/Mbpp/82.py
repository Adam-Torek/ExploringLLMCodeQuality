"""
Write a function to find the volume of a sphere.
assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)
"""

def volume_sphere(radius):
    return (4/3) * math.pi * (radius ** 3)

assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)
/python/python_fundamentals/for_loop_basic2.py
"""
Print integers from 0 to 100.
Print all the even numbers from 1 to 1000.
Print all the odd numbers from 1 to 1000.
Print all the multiples of 5 from 5 to 1,000,000.
Print integers 1 to 100, but if divisible by 5 print "Coding" instead.
If divisible by 10 print "Coding Dojo".
"""

for i in range(0, 101):
    print(i)

for i in range(1, 1001):
    if i % 2 == 0:
        print(i)

for i in range(1, 1001):
    if i % 2!= 0:
        print(i)

for i in range(5, 1000001):
    if i % 5 == 0:
        print(i)

for i in range(1, 1001):
    if i % 5 == 0:
        print("Coding")
    else:
        print(i)

for i in range(1, 1001):
    if i % 5 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)
/python/python_fundamentals/coin_tosses.py
"""
Create a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
"""

import random

def coin_tosses():
    heads = 0
    tails = 0
    for i in range(1, 5001):
        toss = random.randint(0, 1)
        if toss == 0:
            heads += 1
            print("Attempt #{}: Throwing a coin... It's a head!... Got {} head(s) so far and {} tail(s) so far".format(i, heads, tails))
        else:
            tails += 1
            print("Attempt #{}: Throwing a coin... It's a tail!... Got {} head(s) so far and {} tail(s) so far".format(i, heads, tails))

coin_tosses()
/python/python_fundamentals/coin_tosses2.py
"""
Create another function that simulates tossing a coin 5,000 times. Your function should print the number of heads and tails and the percentage of head/tails.
"""

import random

def coin_tosses():
    heads = 0
    tails = 0
    for i in range(1, 5001):
        toss = random.randint(0, 1)
        if toss == 0:
            heads += 1
            print("Attempt #{}: Throwing a coin... It's a head!... Got {} head(s) so far and {} tail(s) so far".format(i, heads, tails))
        else:
            tails += 1
            print("Attempt #{}: Throwing a coin... It's a tail!... Got {} head(s) so far and {} tail(s) so far".format(i, heads, tails))
    print("Ending the program, thank you!")
    print("Attempt #{}: Throwing a coin... It's a head!... Got {} head(s) so far and {} tail(s) so far".format(i, heads, tails))
    print("Ending the program, thank you!")
    print("Ending the program, thank you!")
    print("Ending the program, thank you!")
    print("Ending the program, thank you!")
    print("Ending the program, thank you!")
    print("Ending the program, thank you!")
    print("Ending