"""
Write a python function to check if a given number is one less than twice its reverse.
assert check(70) == False
"""
def check(num):
    reversed_num = int(str(num)[::-1])
    return num - reversed_num == 1

assert check(20) == True
assert check(15) == False
assert check(36) == True
assert check(121) == True
assert check(123) == False
assert check(12021) == True
assert check(354254) == True
assert check(12345) == False
assert check(2002) == True
assert check(1234567) == True
assert check(1234560246) == True</s>