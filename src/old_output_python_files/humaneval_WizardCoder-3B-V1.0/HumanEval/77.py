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

# Solution:
def iscube(a):
    if a == 0:
        return True
    elif a < 0:
        return iscube(-a)
    else:
        for i in range(1, int(a**0.5)+1):
            if a % i == 0:
                return False
        return True

# Test cases
print(iscube(1))  # True
print(iscube(2))  # False
print(iscube(-1))  # True
print(iscube(64))  # True
print(iscube(0))  # True
print(iscube(180))  # False<|endoftext|>