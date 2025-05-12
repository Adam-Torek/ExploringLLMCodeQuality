from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers = numbers.split()
    numbers.sort()
    return ' '.join(numbers)


def sort_numbers_2(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers_2('three one five')
    'one three five'
    """
    numbers = numbers.split()
    numbers.sort(key=lambda x: int(x))
    return ' '.join(numbers)


def sort_numbers_3(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers_3('three one five')
    'one three five'
    """
    numbers = numbers.split()
    numbers.sort(key=lambda x: int(x), reverse=False)
    return ' '.join(numbers)


def sort_numbers_4(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers_4('three one five')
    'one three five'
    """
    numbers = numbers.split()
    numbers.sort(key=lambda x: int(x), reverse=False)
    return ' '.join(numbers)


def sort_numbers_5(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers_5('three one five')
    'one three five'
    """
    numbers = numbers.split()
    numbers.sort(key=lambda x: int(x), reverse=False)
    return ' '.join(numbers)


def sort_numbers_6(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers_6('three one five')
    'one three five'
    """
    numbers = numbers.split()
    numbers.sort(key=lambda x: int(x), reverse=False)
    return ' '.join(numbers)


def sort_numbers_7(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five