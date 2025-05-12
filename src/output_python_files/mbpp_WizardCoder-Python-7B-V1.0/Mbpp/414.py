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
assert overlapping([1,2,3,4,5],[4,5,6,7,8]) == True
assert overlapping([1,2,3,4,5],[1,2,3,4,5]) == True
assert overlapping([1,2,3,4,5],[5,6,7,8,9]) == True
assert overlapping([1,2,3,4,5],[1,2,3,4,5,6,7,8,9]) == True
assert overlapping([1,2,3,4,5],[6,7,8,9,10]) == False
assert overlapping([1,2,3,4,5],[1,2,3,4,5,6,7,8,9,10]) == True
assert overlapping([1,2,3,4,5],[1,2,3,4,5,6,7,8,9,10,11]) == True
assert overlapping([1,2,3,4,5],[1,2,3,4,5,6,7,8,9,10,11,12]) == True
assert overlapping([1,2,3,4,5],[1,2,3,4,5,6,7,8,9,10,11,12,13]) == True
assert overlapping([1,2,3,4,5],[1,2,3,4,5,6,7,8,9,10,11,12,13,14]) == True
assert overlapping([1,2,3,4,5],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) == True
assert overlapping([1,2,3,4,5],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]) == True
assert overlapping([1,2,3,4,5],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]) == True
assert overlapping([1,2,3,4,5],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]) == True
assert overlapping([1,2,3,4,5],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]) == True
assert overlapping([1,2,3,4,5],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]) == True
assert overlapping([1,2,3,4,5],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]) == True
assert overlapping([1,2,3,4,5],[1,2,3,4,5,6,7,8,9,10,11,