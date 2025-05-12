from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        raise ValueError("Need at least two numbers")
    closest_pair = (min(numbers), max(numbers))
    for i in range(1, len(numbers)):
        if abs(closest_pair[0] - numbers[i]) < abs(closest_pair[1] - numbers[i]):
            closest_pair = (numbers[i], closest_pair[1])
    return closest_pair


def find_closest_elements_with_threshold(numbers: List[float], threshold: float) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements_with_threshold([1.0, 2.0, 3.0, 4.0, 5.0, 2.2], 0.5)
    (2.0, 2.2)
    >>> find_closest_elements_with_threshold([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.5)
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        raise ValueError("Need at least two numbers")
    closest_pair = (min(numbers), max(numbers))
    for i in range(1, len(numbers)):
        if abs(closest_pair[0] - numbers[i]) < abs(closest_pair[1] - numbers[i]) and abs(closest_pair[0] - numbers[i]) < threshold:
            closest_pair = (numbers[i], closest_pair[1])
    return closest_pair


def find_closest_elements_with_threshold_and_order(numbers: List[float], threshold: float) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements_with_threshold_and_order([1.0, 2.0, 3.0, 4.0, 5.0, 2.2], 0.5)
    (2.0, 2.2)
    >>> find_closest_elements_with_threshold_and_order([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.5)
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        raise ValueError("Need at least two numbers")
    closest_pair = (min(numbers), max(numbers))
    for i in range(1, len(numbers)):
        if abs(closest_pair[0] - numbers[i]) < abs(closest_pair[1] - numbers[i]) and abs(closest_pair[0] - numbers[i]) < threshold:
            closest_pair = (numbers[i], closest_pair[1])
    return closest_pair