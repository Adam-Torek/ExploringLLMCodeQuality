"""
Write a python function to check whether any value in a sequence exists in a sequence or not.
assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
"""

def overlapping(seq1, seq2):
    for num in seq1:
        if num in seq2:
            return True
    return False

# Test cases
assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
assert overlapping([1,2,3,4,5],[1,2,3,4,5]) == True
assert overlapping([1,2,3,4,5],[5,4,3,2,1]) == True<|endoftext|>