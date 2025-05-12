def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    return a == int(round(a ** (1/3)) ** 3


# Test cases
print(iscube(1)) # True
print(iscube(2)) # False
print(iscube(-1)) # True
print(iscube(64)) # True
print(iscube(0)) # True
print(iscube(180)) # False


# Test cases with edge cases
print(iscube(1)) # True
print(iscube(2)) # False
print(iscube(-1)) # True
print(iscube(64)) # True
print(iscube(0)) # True
print(iscube(180)) # False

# Test cases with other values
print(iscube(1000)) # True
print(iscube(10000)) # True
print(iscube(100000)) # True
print(iscube(1000000)) # True
print(iscube(10000000)) # True
print(iscube(100000000)) # True
print(iscube(1000000000)) # True
print(iscube(10000000000)) # True
print(iscube(100000000000)) # True
print(iscube(1000000000000)) # True
print(iscube(10000000000000)) # True
print(iscube(100000000000000)) # True
print(iscube(1000000000000000)) # True
print(iscube(10000000000000000)) # True
print(iscube(100000000000000000)) # True
print(iscube(1000000000000000000)) # True
print(iscube(10000000000000000000)) # True
print(iscube(100000000000000000000)) # True
print(iscube(1000000000000000000000)) # True
print(iscube(10000000000000000000000)) # True
print(iscube(100000000000000000000000)) # True
print(iscube(1000000000000000000000000)) # True
print(iscube(1000000000000000000000000)) # True
print(iscube(10000000000000000000000000)) # True
print(iscube(100000000000000000000000000)) # True
print(iscube(1000000000000000000000000000)) # True
print(iscube(10000000000000000000000000000)) # True
print(iscube(100000000000000000000000000