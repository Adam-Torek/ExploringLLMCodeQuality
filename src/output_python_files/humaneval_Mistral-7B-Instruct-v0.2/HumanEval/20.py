from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_diff = float('inf')
    closest_numbers = None
    for num1 in numbers:
        for num2 in numbers:
            if num1 != num2 and abs(num1 - num2) < min_diff:
                min_diff = abs(num1 - num2)
                closest_numbers = (num1, num2)
    return closest_numbers


if __name__ == '__main__':
    import doctest
    doctest.testmod()