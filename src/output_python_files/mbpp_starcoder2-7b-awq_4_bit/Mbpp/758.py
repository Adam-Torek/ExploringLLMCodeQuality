"""
Write a function to count lists within a list. The function should return a dictionary where every list is converted to a tuple and the value of such tuple is the number of its occurencies in the original list.
assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]] )=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
"""

def unique_sublists(lst):
    d = {}
    for i in lst:
        d[tuple(i)] = lst.count(i)
    return d

print(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]))
/Python/Python_100_Days_of_Code/Day_003_Guess_the_Number.py
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 10:44:29 2019

@author: 
"""

import random

def guess_the_number():
    """
    Guess the number game
    """
    print("Guess the number game")
    print("The number is between 1 and 100")
    print("You have 10 attempts")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have 1000 points")
    print("You have