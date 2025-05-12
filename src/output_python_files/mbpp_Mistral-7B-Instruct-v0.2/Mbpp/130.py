"""
Write a function to find the item with maximum frequency in a given list.
assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
"""
from collections import Counter

def max_occurrences(numbers):
    """
    :param numbers: list of numbers
    :return: number with maximum occurrences
    """
    counter = Counter(numbers)
    max_num = counter.most_common(1)[0][0]
    return max_num

if __name__ == "__main__":
    assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]) == 2
    assert max_occurrences([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) == 1
    assert max_occurrences([1,2,3,4,5,6,7,8,9]) == None