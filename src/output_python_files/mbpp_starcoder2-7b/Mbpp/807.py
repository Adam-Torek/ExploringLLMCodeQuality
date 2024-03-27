"""
Write a python function to find the first odd number in a given list of numbers.
assert first_odd([1,3,5]) == 1
"""

def first_odd(numbers):
    for number in numbers:
        if number % 2!= 0:
            return number

assert first_odd([1,3,5]) == 1
assert first_odd([2,4,6]) == None
assert first_odd([2,4,6,8]) == None
assert first_odd([1,2,3,4,5]) == 1
assert first_odd([1,2,3,4,5,6]) == 3
assert first_odd([1,2,3,4,5,6,7]) == 3
assert first_odd([1,2,3,4,5,6,7,8]) == 1
assert first_odd([1,2,3,4,5,6,7,8,9]) == 3
assert first_odd([1,2,3,4,5,6,7,8,9,10]) == 1
assert first_odd([1,2,3,4,5,6,7,8,9,10,11]) == 3
assert first_odd([1,2,3,4,5,6,7,8,9,10,11,12]) == 1
assert first_odd([1,2,3,4,5,6,7,8,9,10,11,12,13]) == 3
assert first_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14]) == 1
assert first_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) == 3
assert first_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]) == 1
assert first_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]) == 3
assert first_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]) == 1
assert first_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]) == 3
assert first_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) == 1
assert first_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]) == 3
assert first_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]) == 1
assert first_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]) == 3
assert first_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]) == 1
assert first_odd([1,2,3,4,5,6,7,8,9,10,11,12,1