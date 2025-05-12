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
print(iscube(125)) # True
print(iscube(126)) # False
print(iscube(127)) # False
print(iscube(128)) # True
print(iscube(129)) # False
print(iscube(130)) # False
print(iscube(125)) # True
print(iscube(126)) # False
print(iscube(127)) # False
print(iscube(128)) # True
print(iscube(129)) # False
print(iscube(130)) # False
print(iscube(131)) # False
print(iscube(132)) # True
print(iscube(133)) # False
print(iscube(134)) # False
print(iscube(135)) # True
print(iscube(136)) # False
print(iscube(137)) # False
print(iscube(138)) # True
print(iscube(139)) # False
print(iscube(144)) # True
print(iscube(145)) # False
print(iscube(146)) # False
print(iscube(147)) # True
print(iscube(148)) # False
print(iscube(149)) # False
print(iscube(150)) # True
print(iscube(151)) # False
print(iscube(152)) # False
print(iscube(153)) # True
print(iscube(154)) # False
print(iscube(155)) # False
print(iscube(156)) # True
print(iscube(157)) # False
print(iscube(158)) # False
print(iscube(159)) # True
print(iscube(160)) # False
print(iscube(161)) # False
print(iscube(162)) # True
print(iscube(163)) # False
print(iscube(164)) # False