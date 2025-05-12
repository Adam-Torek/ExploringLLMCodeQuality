from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers_list = numbers.split()
    numbers_list.sort()
    return ' '.join(numbers_list)


def sort_numbers_in_words(words: List[str]) -> List[str]:
    """
    Input is a list of words containing numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the list with words sorted from smallest to largest
    >>> sort_numbers_in_words(['three', 'one', 'five'])
    ['one', 'three', 'five']
    """
    words_list = words
    words_list.sort()
    return words_list