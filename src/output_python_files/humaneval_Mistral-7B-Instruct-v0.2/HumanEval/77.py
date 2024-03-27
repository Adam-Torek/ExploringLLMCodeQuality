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
    n = int(pow(a, 1.0/3))
    return n*n*n == a

# Test
print(iscube(1))
print(iscube(2))
print(iscube(-1))
print(iscube(64))
print(iscube(0))
print(iscube(180))</s>