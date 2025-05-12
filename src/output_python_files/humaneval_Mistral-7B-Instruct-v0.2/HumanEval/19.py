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


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print(sort_numbers('three one five'))
    print(sort_numbers('five three one'))
    print(sort_numbers('one one one one one'))
    print(sort_numbers('nine nine nine'))
    print(sort_numbers('nine nine nine zero'))
    print(sort_numbers('zero zero zero'))
    print(sort_numbers('zero zero nine'))
    print(sort_numbers('nine nine zero'))
    print(sort_numbers('nine zero nine'))
    print(sort_numbers('nine nine nine nine'))
    print(sort_numbers('nine nine nine nine zero'))
    print(sort_numbers('nine nine nine nine zero zero'))
    print(sort_numbers('nine nine nine nine zero zero zero'))
    print(sort_numbers('nine nine nine nine zero zero zero zero'))
    print(sort_numbers('nine nine nine nine zero zero zero zero zero'))
    print(sort_numbers('nine nine nine nine zero zero zero zero zero zero'))
    print(sort_numbers('nine nine nine nine zero zero zero zero zero zero zero'))
    print(sort_numbers('nine nine nine nine zero zero zero zero zero zero zero zero'))
    print(sort_numbers('nine nine nine nine zero zero zero zero zero zero zero zero zero'))
    print(sort_numbers('nine nine nine nine zero zero zero zero zero zero zero zero zero zero'))
    print(sort_numbers('nine nine nine nine zero zero zero zero zero zero zero zero zero zero zero'))
    print(sort_numbers('nine nine nine nine zero zero zero zero zero zero zero zero zero zero zero zero'))
    print(sort_numbers('nine nine nine nine zero zero zero zero zero zero zero zero zero zero zero zero zero'))
    print(sort_numbers('nine nine nine nine zero zero zero zero zero zero zero zero zero zero zero zero zero zero'))
    print(sort_numbers('nine nine nine nine zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero'))
    print(sort_numbers('nine nine nine nine zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero'))
    print(sort_numbers('nine nine nine nine zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero'))
    print(sort_numbers('nine nine nine nine zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero'))
    print(sort_numbers('nine nine nine nine zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero'))
    print(sort_numbers('nine nine nine nine zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero'))
    print(sort_numbers('nine nine nine nine zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero'))
    print(sort_numbers('nine nine nine nine zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero'))
    print(sort_numbers('nine nine nine nine zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero zero'))
    print(sort_numbers('nine nine