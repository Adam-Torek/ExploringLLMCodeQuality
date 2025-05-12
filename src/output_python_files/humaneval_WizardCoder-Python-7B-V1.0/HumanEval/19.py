from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers_list = numbers.split()
    numbers_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    numbers_list = [numbers_dict[num] for num in numbers_list]
    numbers_list.sort()
    return ' '.join(str(num) for num in numbers_list)

def sort_strings(strings: str) -> str:
    """ Input is a space-delimited string of words.
    Return the string with words sorted alphabetically
    >>> sort_strings('cat dog elephant zebra')
    'cat dog elephant zebra'
    """
    return ' '.join(sorted(strings.split()))

def sort_list_of_lists(lists: List[List[int]) -> List[List[int]:
    """ Input is a list of lists of integers.
    Return the list of lists sorted by the sum of their elements
    >>> sort_list_of_lists([[4, 2], [1, 3], [5, 6, 4], [1, 1]])
    [[1, 1], [4, 2], [5, 6, 4]]
    """
    return sorted(lists, key=sum)

def sort_anagrams(anagrams: List[str]) -> List[str]:
    """ Input is a list of strings.
    Return the list of strings sorted by the number of unique characters they contain.
    If there are multiple strings with the same number of unique characters, sort them alphabetically.
    >>> sort_anagrams(['cinema', 'iceman', 'tie', 'eat', 'ate', 'natty', 'tye'])
    ['cinema', 'iceman', 'eat', 'ate', 'natty', 'tye']
    """
    return sorted(anagrams, key=lambda x: (len(set(x)), x))

if __name__ == "__main__":
    import doctest
    doctest.testmod()