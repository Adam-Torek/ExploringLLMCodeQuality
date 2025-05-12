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
        return q == q[::-1]
    else:
        return False

# Test cases
print(will_it_fly([1, 2], 5)) # False
print(will_it_fly([3, 2, 3], 1)) # False
print(will_it_fly([3, 2, 3], 9)) # True
print(will_it_fly([3], 5)) # True
print(will_it_fly([1, 2, 3, 4, 5], 10)) # False
print(will_it_fly([1, 2, 3, 4, 5], 15)) # True
print(will_it_fly([1, 2, 3, 4, 5], 20)) # False
print(will_it_fly([1, 2, 3, 4, 5], 25)) # True
print(will_it_fly([1, 2, 3, 4, 5], 30)) # False
print(will_it_fly([1, 2, 3, 4, 5], 35)) # True
print(will_it_fly([1, 2, 3, 4, 5], 40)) # False
print(will_it_fly([1, 2, 3, 4, 5], 45)) # True
print(will_it_fly([1, 2, 3, 4, 5], 50)) # False
print(will_it_fly([1, 2, 3, 4, 5], 55)) # True
print(will_it_fly([1, 2, 3, 4, 5], 60)) # False
print(will_it_fly([1, 2, 3, 4, 5], 65)) # True
print(will_it_fly([1, 2, 3, 4, 5], 70)) # False
print(will_it_fly([1, 2, 3, 4, 5], 75)) # True
print(will_it_fly([1, 2, 3, 4, 5], 80)) # False
print(will_it_fly([1, 2, 3, 4, 5], 85)) # True
print(will_it_fly([1, 2, 3, 4, 5], 90)) # False
print(will_it_fly([1, 2, 3, 4, 5], 95)) # True
print(will_it_fly([1, 2, 3, 4, 5], 100)) # False
print(will_it_fly([1, 2, 3, 4, 5], 105)) # True
print(will_it_fly([1, 2, 3, 4, 5], 110)) # False
print(will_it_fly([1, 2, 3, 4, 5], 115)) # True
print(