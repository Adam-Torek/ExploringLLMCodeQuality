"""
Write a function to check if each element of second tuple is smaller than its corresponding element in the first tuple.
assert check_smaller((1, 2, 3), (2, 3, 4)) == False
"""

def check_smaller(t1, t2):
    if len(t1)!= len(t2):
        return False
    for i in range(len(t1)):
        if t1[i] > t2[i]:
            return False
    return True

# Test cases
assert check_smaller((1, 2, 3), (2, 3, 4)) == False
assert check_smaller((1, 2, 3), (1, 2, 3)) == True
assert check_smaller((1, 2, 3), (1, 2, 4)) == True
assert check_smaller((1, 2, 3), (1, 3, 2)) == True
assert check_smaller((1, 2, 3), (2, 1, 3)) == True
assert check_smaller((1, 2, 3), (3, 2, 1)) == True<|endoftext|>