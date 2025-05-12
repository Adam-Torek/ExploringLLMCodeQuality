def will_it_fly(q,w):
    '''
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.

    Example:
    will_it_fly([1, 2], 5) ➞ False 
    # 1+2 is less than the maximum possible weight, but it's unbalanced.

    will_it_fly([3, 2, 3], 1) ➞ False
    # it's balanced, but 3+2+3 is more than the maximum possible weight.

    will_it_fly([3, 2, 3], 9) ➞ True
    # 3+2+3 is less than the maximum possible weight, and it's balanced.

    will_it_fly([3], 5) ➞ True
    # 3 is less than the maximum possible weight, and it's balanced.
    '''
    if sum(q) <= w:
        if q == q[::-1]:
            return True
    return False

# Test cases
print(will_it_fly([1, 2], 5)) # False
print(will_it_fly([3, 2, 3], 1)) # False
print(will_it_fly([3, 2, 3], 9)) # True
print(will_it_fly([3], 5)) # True
print(will_it_fly([1, 2, 3, 4, 5], 10)) # True
print(will_it_fly([1, 2, 3, 4, 5], 9)) # False
print(will_it_fly([1, 2, 3, 4, 5], 11)) # False
print(will_it_fly([1, 2, 3, 4, 5], 12)) # True
print(will_it_fly([1, 2, 3, 4, 5], 13)) # False
print(will_it_fly([1, 2, 3, 4, 5], 14)) # False
print(will_it_fly([1, 2, 3, 4, 5], 15)) # False
print(will_it_fly([1, 2, 3, 4, 5], 16)) # False
print(will_it_fly([1, 2, 3, 4, 5], 17)) # False
print(will_it_fly([1, 2, 3, 4, 5], 18)) # False
print(will_it_fly([1, 2, 3, 4, 5], 19)) # False
print(will_it_fly([1, 2, 3, 4, 5], 20)) # False
print(will_it_fly([1, 2, 3, 4, 5], 21)) # False
print(will_it_fly([1, 2, 3, 4, 5], 22)) # False
print(will_it_fly([1, 2, 3, 4, 5], 23)) # False
print(will_it_fly([1, 2, 3, 4, 5], 24)) # False
print(will_it_fly([1, 2, 3, 4, 5], 25)) # False
print(will_it_fly([1, 2, 3, 4, 5], 26)) # False
print(will_it_fly([1, 2, 3, 4, 5], 27)) # False
print(will_it_fly([1, 2, 3, 4, 5], 28)) # False
print(will_it_fly([1, 2, 3, 4, 5], 29)) # False
print(will_it_fly([1, 2, 3, 4, 5], 30)) # False
print(will_it_fly