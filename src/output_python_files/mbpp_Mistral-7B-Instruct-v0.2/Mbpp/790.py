"""
Write a python function to check whether every even index contains even numbers of a given list.
assert even_position([3,2,1]) == False
"""
def even_position(lst):
    """
    :param lst: list of numbers
    :return: boolean value
    """
    for i in range(len(lst)):
        if i % 2 != 0 and lst[i] % 2 != 0:
            return False
    return True

# Test cases
assert even_position([3,2,1]) == False
assert even_position([2,2,1]) == True
assert even_position([2,4,1]) == True
assert even_position([2,2,2]) == True
assert even_position([2,2,2,2]) == True
assert even_position([2,2,2,2,2]) == True
assert even_position([2,2,2,2,2,2]) == True
assert even_position([2,2,2,2,2,2,2]) == True
assert even_position([2,2,2,2,2,2,2,2]) == True
assert even_position([2,2,2,2,2,2,2,2,2]) == True
assert even_position([2,2,2,2,2,2,2,2,2,2]) == True
assert even_position([2,2,2,2,2,2,2,2,2,2,2]) == True
assert even_position([2,2,2,2,2,2,2,2,2,2,2,2]) == True
assert even_position([2,2,2,2,2,2,2,2,2,2,2,2,2]) == True
assert even_position([2,2,2,2,2,2,2,2,2,2,2,2,2,2]) == True
assert even_position([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]) == True
assert even_position([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]) == True
assert even_position([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]) == True
assert even_position([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]) == True
assert even_position([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]) == True
assert even_position([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]) == True
assert even_position([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]) == True
assert even_position([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]) == True
assert even_position([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]) == True
assert even_position([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]) == True
assert even_position([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]) == True
assert even_position([2,2,2,