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
    if len(q) > 1 and q == q[::-1]: #check if the list is balanced and palindromic
        if sum(q) <= w: #check if the sum of the elements is less than or equal to the maximum possible weight
            return True
    return False

#Test Cases
print(will_it_fly([1, 2], 5)) #False
print(will_it_fly([3, 2, 3], 1)) #False
print(will_it_fly([3, 2, 3], 9)) #True
print(will_it_fly([3], 5)) #True
print(will_it_fly([1, 1, 1, 1, 1], 5)) #True
print(will_it_fly([1, 1, 1, 1, 1], 1)) #False
print(will_it_fly([1, 1, 1, 1, 1], 10)) #True
print(will_it_fly([1, 1, 1, 1, 1], 11)) #False
print(will_it_fly([1, 1, 1, 1, 1], 12)) #True
print(will_it_fly([1, 1, 1, 1, 1], 13)) #False
print(will_it_fly([1, 1, 1, 1, 1], 14)) #True
print(will_it_fly([1, 1, 1, 1, 1], 15)) #False
print(will_it_fly([1, 1, 1, 1, 1], 16)) #True
print(will_it_fly([1, 1, 1, 1, 1], 17)) #False
print(will_it_fly([1, 1, 1, 1, 1], 18)) #True
print(will_it_fly([1, 1, 1, 1, 1], 19)) #False
print(will_it_fly([1, 1, 1, 1, 1], 20)) #True
print(will_it_fly([1, 1, 1, 1, 1], 21)) #False
print(will_it_fly([1, 1, 1, 1, 1], 22)) #True
print(will_it_fly([1, 1, 1, 1, 1], 23)) #False
print(will_it_fly([1, 1, 1, 1, 1], 24)) #True
print(will_it_fly([1, 1, 1, 1, 1], 25)) #False
print(will_it_fly([1, 1, 1, 1, 1], 26)) #True
print(will_it_fly([1, 1, 1, 1, 1], 27)) #False
print(will_it_fly([1, 1, 1, 1, 1], 28)) #True
print(