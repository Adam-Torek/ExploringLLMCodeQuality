"""
The input is defined as two lists of the same length. Write a function to count indices where the lists have the same values.
assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])==4
"""

def count_same_pair(list1, list2):
    count = 0
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            count += 1
    return count

print(count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9]))/python/python_fundamentals/for_loop_basic2.py
"""
Print integers from 0 to 100. 
But for multiples of five print "Coding" instead of the number and for multiples of fifteen print "Coding Dojo".
"""

for i in range(101):
    if i % 5 == 0 and i % 15!= 0:
        print("Coding")
    elif i % 15 == 0:
        print("Coding Dojo")
    else:
        print(i)/python/python_fundamentals/coin_toss.py
"""
Create a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
"""

import random

def coin_toss():
    head = 0
    tail = 0
    for i in range(5000):
        if random.randint(0,1) == 0:
            head += 1
        else:
            tail += 1
    print("Heads: " + str(head))
    print("Tails: " + str(tail))

coin_toss()/python/python_fundamentals/coin_toss_2.py
"""
Create another function that simulates tossing a coin 5,000 times. Your function should print the number of heads and tails and the percentage of head/tails.
"""

import random

def coin_toss():
    head = 0
    tail = 0
    for i in range(5000):
        if random.randint(0,1) == 0:
            head += 1
        else:
            tail += 1
    print("Heads: " + str(head))
    print("Tails: " + str(tail))
    print("Percentage of Heads: " + str(head/5000))
    print("Percentage of Tails: " + str(tail/5000))

coin_toss()/python/python_fundamentals/coin_toss_3.py
"""
Create another function that simulates tossing a coin 5,000 times. Your function should print the number of heads and tails and the percentage of head/tails.
"""

import random

def coin_toss():
    head = 0
    tail = 0
    for i in range(5000):
        if random.randint(0,1) == 0:
            head += 1
        else:
            tail += 1
    print("Heads: " + str(head))
    print("Tails: " + str(tail))
    print("Percentage of Heads: " + str(head/5000))
    print("Percentage of Tails: " + str(tail/5000))

coin_toss()

def coin_toss_2():
    head = 0
    tail = 0
    for i in range(5000):
        if random.randint(0,1) == 0:
            head += 1
        else:
            tail += 1
    print("Heads: " + str(head))
    print("Tails: " + str(tail))
    print("Percentage of Heads: " + str(head/5000))
    print("Percentage of Tails: " + str(tail/5000))

coin_toss_2()/python/python_fundamentals/coin_toss_4.py
"""
Create another function that simulates tossing a coin 5,000 times. Your function should print the number of heads and tails and the percentage of