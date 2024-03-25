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
    if q == []:
        return False
    if q == q[::-1]:
        if sum(q) <= w:
            return True
        else:
            return False
    else:
        return False


print(will_it_fly([1, 2], 5))
print(will_it_fly([3, 2, 3], 1))
print(will_it_fly([3, 2, 3], 9))
print(will_it_fly([3], 5))
print(will_it_fly([1, 2, 3], 5))
print(will_it_fly([1, 2, 3], 1))
print(will_it_fly([1, 2, 3], 9))
print(will_it_fly([1, 2, 3], 10))
print(will_it_fly([1, 2, 3], 11))
print(will_it_fly([1, 2, 3], 12))
print(will_it_fly([1, 2, 3], 13))
print(will_it_fly([1, 2, 3], 14))
print(will_it_fly([1, 2, 3], 15))
print(will_it_fly([1, 2, 3], 16))
print(will_it_fly([1, 2, 3], 17))
print(will_it_fly([1, 2, 3], 18))
print(will_it_fly([1, 2, 3], 19))
print(will_it_fly([1, 2, 3], 20))
print(will_it_fly([1, 2, 3], 21))
print(will_it_fly([1, 2, 3], 22))
print(will_it_fly([1, 2, 3], 23))
print(will_it_fly([1, 2, 3], 24))
print(will_it_fly([1, 2, 3], 25))
print(will_it_fly([1, 2, 3], 26))
print(will_it_fly([1, 2, 3], 27))
print(will_it_fly([1, 2, 3], 28))
print(will_it_fly([1, 2, 3], 29))
print(will_it_fly([1, 2, 3], 30))
print(will_it_fly([1, 2, 3], 31))
print(will_it_fly([1, 2, 3], 32))
print(will_it_fly([1, 2, 3], 33))
print(will_it_fly([1, 2, 3], 34))
print(will_it_fly([1, 2, 3], 35))
print(will_it_fly([1, 2, 3], 36))
print(will_it