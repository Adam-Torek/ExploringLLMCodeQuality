"""
Write a function to check whether the entered number is greater than the elements of the given array.
assert check_greater([1, 2, 3, 4, 5], 4) == False
"""


def check_greater(arr, num):
    for i in arr:
        if i > num:
            return True
    return False


print(check_greater([1, 2, 3, 4, 5], 4))
print(check_greater([1, 2, 3, 4, 5], 6))
print(check_greater([1, 2, 3, 4, 5], 0))
print(check_greater([1, 2, 3, 4, 5], 1))
print(check_greater([1, 2, 3, 4, 5], 5))
print(check_greater([1, 2, 3, 4, 5], 6))
print(check_greater([1, 2, 3, 4, 5], 10))
print(check_greater([1, 2, 3, 4, 5], 100))
print(check_greater([1, 2, 3, 4, 5], 1000))
print(check_greater([1, 2, 3, 4, 5], 10000))
print(check_greater([1, 2, 3, 4, 5], 100000))
print(check_greater([1, 2, 3, 4, 5], 1000000))
print(check_greater([1, 2, 3, 4, 5], 10000000))
print(check_greater([1, 2, 3, 4, 5], 100000000))
print(check_greater([1, 2, 3, 4, 5], 1000000000))
print(check_greater([1, 2, 3, 4, 5], 10000000000))
print(check_greater([1, 2, 3, 4, 5], 100000000000))
print(check_greater([1, 2, 3, 4, 5], 1000000000000))
print(check_greater([1, 2, 3, 4, 5], 10000000000000))
print(check_greater([1, 2, 3, 4, 5], 100000000000000))
print(check_greater([1, 2, 3, 4, 5], 1000000000000000))
print(check_greater([1, 2, 3, 4, 5], 10000000000000000))
print(check_greater([1, 2, 3, 4, 5], 100000000000000000))
print(check_greater([1, 2, 3, 4, 5], 1000000000000000000))
print(check_greater([1, 2, 3, 4, 5], 10000000000000000000))
print(check_greater([1, 2, 3, 4, 5], 100000000000000000000))
print(check_greater([1, 2, 3, 4, 5], 1000000000000000000000))
print(check_greater([1, 2, 3, 4, 5], 1000000