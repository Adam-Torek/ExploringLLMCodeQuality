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
    print(sort_numbers('one one one'))
    print(sort_numbers('nine nine nine'))
    print(sort_numbers('nine nine one'))
    print(sort_numbers('one nine nine'))
    print(sort_numbers('one nine one'))
    print(sort_numbers('one one nine'))
    print(sort_numbers('one one one'))
    print(sort_numbers('zero zero zero'))
    print(sort_numbers('zero zero one'))
    print(sort_numbers('zero one zero'))
    print(sort_numbers('zero one one'))
    print(sort_numbers('zero one two'))
    print(sort_numbers('zero two one'))
    print(sort_numbers('one zero zero'))
    print(sort_numbers('one zero one'))
    print(sort_numbers('one one zero'))
    print(sort_numbers('one one zero'))
    print(sort_numbers('one one two'))
    print(sort_numbers('one two one'))
    print(sort_numbers('two one one'))
    print(sort_numbers('two one zero'))
    print(sort_numbers('two zero one'))
    print(sort_numbers('two zero zero'))
    print(sort_numbers('three zero zero'))
    print(sort_numbers('three zero one'))
    print(sort_numbers('three one zero'))
    print(sort_numbers('three one one'))
    print(sort_numbers('three one two'))
    print(sort_numbers('three two one'))
    print(sort_numbers('four zero zero'))
    print(sort_numbers('four zero one'))
    print(sort_numbers('four one zero'))
    print(sort_numbers('four one one'))
    print(sort_numbers('four one two'))
    print(sort_numbers('four two one'))
    print(sort_numbers('five zero zero'))
    print(sort_numbers('five zero one'))
    print(sort_numbers('five one zero'))
    print(sort_numbers('five one one'))
    print(sort_numbers('five one two'))
    print(sort_numbers('five two one'))
    print(sort_numbers('six zero zero'))
    print(sort_numbers('six zero one'))
    print(sort_numbers('six one zero'))
    print(sort_numbers('six one one'))
    print(sort_numbers('six one two'))
    print(sort_numbers('six two one'))
    print(sort_numbers('seven zero zero'))
    print(sort_numbers('seven zero one'))
    print(sort_numbers('seven one zero'))
    print(sort_numbers('seven one one'))
    print(sort_numbers('seven one two'))
    print(sort_numbers('seven two one'))
    print(sort_numbers('eight zero zero'))
    print(sort_numbers('eight zero one'))
    print(sort_numbers('eight one zero'))
    print(sort_numbers('eight one one'))
    print(sort_numbers('eight one two'))
    print(sort_numbers('eight two one'))
    print(sort_numbers('nine zero zero'))
    print(sort_numbers('nine zero one'))
    print(sort_numbers('nine one zero'))
    print(sort_numbers('nine