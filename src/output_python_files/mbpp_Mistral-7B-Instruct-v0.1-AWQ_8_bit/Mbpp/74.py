"""
Write a function to check whether it follows the sequence given in the patterns array.
assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
"""

def is_samepatterns(patterns, sequences):
    """
    :param patterns: list of strings
    :param sequences: list of strings
    :return: True if the sequences follow the patterns, False otherwise
    """
    for i in range(len(patterns)):
        if sequences[i] != patterns[i]:
            return False
    return True