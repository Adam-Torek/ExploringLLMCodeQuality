"""
Write a python function to check whether any value in a sequence exists in a sequence or not.
assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
"""

def overlapping(seq1, seq2):
    for i in seq1:
        for j in seq2:
            if i == j:
                return True
    return False

assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
assert overlapping([1,2,3,4,5],[6,7,8,9,1]) == True
assert overlapping([1,2,3,4,5],[6,7,8,9,1,2]) == True
assert overlapping([1,2,3,4,5],[6,7,8,9,1,2,3]) == True
assert overlapping([1,2,3,4,5],[6,7,8,9,1,2,3,4]) == True
assert overlapping([1,2,3,4,5],[6,7,8,9,1,2,3,4,5]) == True
assert overlapping([1,2,3,4,5],[6,7,8,9,1,2,3,4,5,6]) == True
assert overlapping([1,2,3,4,5],[6,7,8,9,1,2,3,4,5,6,7]) == True
assert overlapping([1,2,3,4,5],[6,7,8,9,1,2,3,4,5,6,7,8]) == True
assert overlapping([1,2,3,4,5],[6,7,8,9,1,2,3,4,5,6,7,8,9]) == True
assert overlapping([1,2,3,4,5],[6,7,8,9,1,2,3,4,5,6,7,8,9,1]) == True
assert overlapping([1,2,3,4,5],[6,7,8,9,1,2,3,4,5,6,7,8,9,1,2]) == True
assert overlapping([1,2,3,4,5],[6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3]) == True
assert overlapping([1,2,3,4,5],[6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4]) == True
assert overlapping([1,2,3,4,5],[6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5]) == True
assert overlapping([1,2,3,4,5],[6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6]) == True
assert overlapping([1,2,3,4,5],[6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7]) == True
assert overlapping([1,2,3,4,5],[6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8]) == True
assert overlapping([1,2,3,4,5],[6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]) == True
assert overlapping([1,2,3,4,5],[6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1]) == True
assert overlapping([1,2,3,4,5],[6,7,8,9,1,2,