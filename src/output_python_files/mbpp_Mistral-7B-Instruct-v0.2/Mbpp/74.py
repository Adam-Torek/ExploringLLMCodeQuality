"""
Write a function to check whether it follows the sequence given in the patterns array.
assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
"""
def is_samepatterns(patterns, given):
    """
    :param patterns: list of strings
    :param given: list of strings
    :return: boolean
    """
    if len(patterns) != len(given):
        return False

    for i in range(len(patterns)):
        if len(patterns[i]) != len(given[i]):
            return False

        for j in range(len(patterns[i])):
            if patterns[i][j] != given[i][j]:
                return False

    return True