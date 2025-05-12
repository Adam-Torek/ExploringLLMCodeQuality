"""
Write a python function to find the first odd number in a given list of numbers.
assert first_odd([1,3,5]) == 1
"""

def first_odd(numbers):
    for num in numbers:
        if num % 2!= 0:
            return num

assert first_odd([1,3,5]) == 1
assert first_odd([2,4,6]) == None
assert first_odd([2,4,6,8]) == 2
assert first_odd([2,4,6,8,10]) == 2
assert first_odd([2,4,6,8,10,12]) == 12
assert first_odd([2,4,6,8,10,12,14]) == 12
assert first_odd([2,4,6,8,10,12,14,16]) == 12
assert first_odd([2,4,6,8,10,12,14,16,18]) == 12
assert first_odd([2,4,6,8,10,12,14,16,18,20]) == 12
assert first_odd([2,4,6,8,10,12,14,16,18,20,22]) == 22
assert first_odd([2,4,6,8,10,12,14,16,18,20,22,24]) == 22
assert first_odd([2,4,6,8,10,12,14,16,18,20,22,24,26]) == 22
assert first_odd([2,4,6,8,10,12,14,16,18,20,22,24,26,28]) == 22
assert first_odd([2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]) == 22
assert first_odd([2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]) == 22
assert first_odd([2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34]) == 34
assert first_odd([2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]) == 34
assert first_odd([2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38]) == 34
assert first_odd([2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40]) == 34
assert first_odd([2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42]) == 42
assert first_odd([2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44]) == 42
assert first_odd([2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46]) == 42
assert