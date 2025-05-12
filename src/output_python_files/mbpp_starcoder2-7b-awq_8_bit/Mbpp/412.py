"""
Write a python function to remove odd numbers from a given list.
assert remove_odd([1,2,3]) == [2]
"""

def remove_odd(numbers):
    return [number for number in numbers if number % 2 == 0]

assert remove_odd([1,2,3]) == [2]
assert remove_odd([1,2,3,4]) == [2,4]
assert remove_odd([1,2,3,4,5]) == [2,4]
assert remove_odd([1,2,3,4,5,6]) == [2,4,6]
assert remove_odd([1,2,3,4,5,6,7]) == [2,4,6]
assert remove_odd([1,2,3,4,5,6,7,8]) == [2,4,6,8]
assert remove_odd([1,2,3,4,5,6,7,8,9]) == [2,4,6,8]
assert remove_odd([1,2,3,4,5,6,7,8,9,10]) == [2,4,6,8,10]
assert remove_odd([1,2,3,4,5,6,7,8,9,10,11]) == [2,4,6,8,10]
assert remove_odd([1,2,3,4,5,6,7,8,9,10,11,12]) == [2,4,6,8,10,12]
assert remove_odd([1,2,3,4,5,6,7,8,9,10,11,12,13]) == [2,4,6,8,10,12]
assert remove_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14]) == [2,4,6,8,10,12,14]
assert remove_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) == [2,4,6,8,10,12,14]
assert remove_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]) == [2,4,6,8,10,12,14,16]
assert remove_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]) == [2,4,6,8,10,12,14,16]
assert remove_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]) == [2,4,6,8,10,12,14,16,18]
assert remove_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]) == [2,4,6,8,10,12,14,16,18]
assert remove_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) == [2,4,6,8,10,12,14,16,18,20]
assert remove_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]) == [2,4,6,8,10,12,14,16,18,20]
assert remove_odd([1,2,3,4,5,6,