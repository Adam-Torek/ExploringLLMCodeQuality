"""
Write a python function to check whether any value in a sequence exists in a sequence or not.
assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
"""
def overlapping(seq1, seq2):
    """
    This function checks whether any value in sequence 1 exists in sequence 2 or not.
    :param seq1: list or tuple
    :param seq2: list or tuple
    :return: boolean value
    """
    for i in seq1:
        if i in seq2:
            return True
    return False

# Test case
assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
assert overlapping([1,2,3,4,5],[1,2,3,4,5]) == True
assert overlapping([1,2,3,4,5],[1,2,3,4,5,6]) == True