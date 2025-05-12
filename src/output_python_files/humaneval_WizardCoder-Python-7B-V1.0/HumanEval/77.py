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

# Solution
def iscube(a):
    return a == int(round(a ** (1/3)) ** 3

# Test cases
print(iscube(1)) # True
print(iscube(2)) # False
print(iscube(-1)) # True
print(iscube(64)) # True
print(iscube(0)) # True
print(iscube(180)) # False

# Explanation:
# We use the `round()` function to round the cube root of `a` to the nearest integer, and then check if it is equal to `a`. If it is, then `a` is a cube of some integer. If not, then it is not a cube.