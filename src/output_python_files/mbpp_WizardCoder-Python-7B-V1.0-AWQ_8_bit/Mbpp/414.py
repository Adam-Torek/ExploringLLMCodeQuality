"""
Write a python function to check whether any value in a sequence exists in a sequence or not.
assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
"""

def overlapping(seq1, seq2):
    for i in seq1:
        if i in seq2:
            return True
    return False

# Test cases
assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
assert overlapping([1,2,3,4,5],[4,6,7,8,9]) == True
assert overlapping([1,2,3,4,5],[1,6,7,8,9]) == True
assert overlapping([1,2,3,4,5],[5,6,7,8,9]) == True
assert overlapping([1,2,3,4,5],[1,2,3,4,5]) == True
assert overlapping([1,2,3,4,5],[5,6,7,8,9,1]) == True
assert overlapping([1,2,3,4,5],[1,6,7,8,9,5]) == True
assert overlapping([1,2,3,4,5],[5,6,7,8,9,1]) == True
assert overlapping([1,2,3,4,5],[1,6,7,8,9,5]) == True
assert overlapping([1,2,3,4,5],[1,2,3,4,5]) == True
assert overlapping([1,2,3,4,5],[5,6,7,8,9,1]) == True
assert overlapping([1,2,3,4,5],[1,6,7,8,9,5]) == True
assert overlapping([1,2,3,4,5],[1,2,3,4,5]) == True
assert overlapping([1,2,3,4,5],[5,6,7,8,9,1]) == True
assert overlapping([1,2,3,4,5],[1,6,7,8,9,5]) == True
assert overlapping([1,2,3,4,5],[1,2,3,4,5]) == True
assert overlapping([1,2,3,4,5],[5,6,7,8,9,1]) == True
assert overlapping([1,2,3,4,5],[1,6,7,8,9,5]) == True
assert overlapping([1,2,3,4,5],[1,2,3,4,5]) == True
assert overlapping([1,2,3,4,5],[5,6,7,8,9,1]) == True
assert overlapping([1,2,3,4,5],[1,6,7,8,9,5]) == True
assert overlapping([1,2,3,4,5],[1,2,3,4,5]) == True
assert overlapping([1,2,3,4,5],[5,6,7,8,9,1]) == True
assert overlapping([1,2,3,4,5],[1,6,7,8,9,5]) == True
assert overlapping([1,2,3,4,5],[1,2,3,4,5]) == True
assert overlapping([1,2,3,4,5],[5,6,7,8,9,1]) == True
assert overlapping([1,2,3,4,5],[1,6,7,8,9,5]) == True
assert overlapping([1,2,3,4,5],[1,2,3,4,5]) == True
assert overlapping([1,2,3,4,5],[5,6,7,8,9,1]) == True
assert overlapping([1,2,3,4,5],[1,6,7,8,9,5]) == True
assert overlapping([1,2,3,4,5],[1,2,3,4,5]) == True
assert overlapping([1,2,3,4,5],[5,6,7,8,9,1]) ==