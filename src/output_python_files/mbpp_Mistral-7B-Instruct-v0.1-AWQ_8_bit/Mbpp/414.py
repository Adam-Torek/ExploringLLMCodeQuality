"""
Write a python function to check whether any value in a sequence exists in a sequence or not.
assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
"""

def overlapping(seq1, seq2):
    """
    :param seq1:
    :param seq2:
    :return:
    """
    for i in seq1:
        if i in seq2:
            return True
    return False