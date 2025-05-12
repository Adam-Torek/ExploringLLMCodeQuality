def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
  

    
    '''
    if type(x) == int and type(y) == int and type(z) == int:
        return x == y + z or y == x + z or z == x + y
    else:
        return False

# Test cases
print(any_int(5, 2, 7)) # True
print(any_int(3, 2, 2)) # False
print(any_int(3, -2, 1)) # True
print(any_int(3.6, -2.2, 2)) # False
print(any_int(1, 2, 3)) # False
print(any_int(1, 2, 3.5)) # False
print(any_int(1, 2.5, 3)) # False
print(any_int(1, 2, 3.5)) # False
print(any_int(1, 2.5, 3.5)) # False
print(any_int(1, 2, '3')) # False
print(any_int(1, 2, 3)) # False
print(any_int(1, 2, 3.5)) # False
print(any_int(1, 2.5, 3)) # False
print(any_int(1, 2.5, 3.5)) # False
print(any_int(1, '2', 3)) # False
print(any_int(1, 2, '3')) # False
print(any_int('1', 2, 3)) # False
print(any_int(1, '2', 3.5)) # False
print(any_int(1, 2.5, '3')) # False
print(any_int('1', 2, 3.5)) # False
print(any_int(1, '2', '3')) # False
print(any_int('1', 2, '3')) # False
print(any_int(1.5, 2, 3)) # False
print(any_int(1, 2.5, '3')) # False
print(any_int('1', 2.5, 3)) # False
print(any_int('1', 2, '3')) # False
print(any_int('1', '2', 3)) # False
print(any_int('1', '2', '3')) # False
print(any_int(1, 2, '3.5')) # False
print(any_int('1', '2', '3.5')) # False
print(any_int(1.5, 2.5, 3)) # False
print(any_int(1.5, 2, 3.5)) # False
print(any_int(1.5, '2', 3)) # False
print(any_int(1, '2.5', 3.5)) # False
print(any_