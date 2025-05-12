"""
Write a python function to check if a given number is one less than twice its reverse.
assert check(70) == False
"""
def check(num):
    reversed_num = int(str(num)[::-1])
    return num - reversed_num == 1

assert check(70) == False
assert check(23) == True
assert check(121) == True
assert check(15625) == True
assert check(3703701) == True
assert check(37037037037) == True
assert check(12345678987654321) == True