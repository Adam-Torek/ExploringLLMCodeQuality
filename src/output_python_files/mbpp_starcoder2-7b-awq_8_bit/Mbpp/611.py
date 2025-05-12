"""
Write a function which given a matrix represented as a list of lists returns the max of then'th column.
assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
"""

def max_of_nth(matrix, n):
    return max(matrix[i][n] for i in range(len(matrix)))

print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2))
/python/python_fundamentals/for_loop_basic2.py
"""
Basic - Print all integers from 0 to 150.

Print all the multiples of 5 from 5 to 1,000

Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

Print the sum of all integers from 0 to 5000.

Print all the multiples of 6 up to 60,000,000 (just the multiples)

Countdown by 4's starting at 2018, printing "Countdown - x".

Countdown by fours starting at 2018, printing "Countdown - x".

Flexible Countdown
Based on earlier exercise, given lowNum, highNum, mult, print multiples of mult from lowNum to highNum, using a for loop. For example, lowNum=2, highNum=9, mult=3 will print 3, 6, 9 on successive lines.
"""

for i in range(0, 151):
    print(i)

for i in range(5, 1001, 5):
    print(i)

for i in range(1, 1001):
    if i % 5 == 0:
        print("Coding")
    elif i % 10 == 0:
        print("Coding Dojo")
    else:
        print(i)

sum = 0
for i in range(0, 5001):
    sum += i
print(sum)

for i in range(5, 600000001, 6):
    print(i)

for i in range(2018, 0, -4):
    print("Countdown -", i)

for i in range(2018, 0, -1):
    if i % 4 == 0:
        print("Countdown -", i)

def flexible_countdown(lowNum, highNum, mult):
    for i in range(lowNum, highNum + 1):
        if i % mult == 0:
            print(i)

flexible_countdown(2, 9, 3)
/python/python_fundamentals/coin_tosses.py
"""
Toss a coin 5 times and print out the result of each toss.

Toss a coin 500 times and print out how many times the result is heads.

Toss a coin 500 times and print out how many times the result is heads.

Toss a coin 1000 times and print out how many times the result is heads.

Toss a coin 1000 times and print out how many times the result is heads.

Toss a coin 1000000 times and print out how many times the result is heads.

Toss a coin 1000000 times and print out how many times the result is heads.
"""

import random

def coin_tosses():
    heads = 0
    tails = 0
    for i in range(5):
        if random.randint(0, 1) == 0:
            heads += 1
        else:
            tails += 1
    print("Heads:", heads, "Tails:", tails)

coin_tosses()

def coin_tosses_500():
    heads = 0
    tails = 0
    for i in range(500):
        if random.randint(0, 1) == 0:
            heads += 1
        else:
            tails += 1
    print("Heads:", heads, "Tails:", tails)

coin_tosses_50