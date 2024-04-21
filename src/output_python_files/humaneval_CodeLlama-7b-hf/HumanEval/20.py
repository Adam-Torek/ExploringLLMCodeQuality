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
        raise ValueError("List must contain at least two numbers")

    closest_pair = (numbers[0], numbers[1])
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < abs(closest_pair[0] - closest_pair[1]):
                closest_pair = (numbers[i], numbers[j])

    return closest_pair


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
    # print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
    # print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 2.2]))
    # print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 2.2, 2.3]))
    # print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 2.2, 2.3, 2.4]))
    # print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 2.2, 2.3, 2.4, 2.5]))
    # print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 2.2, 2.3, 2.4, 2.5, 2.6]))
    # print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7]))
    # print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8]))
    # print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9]))
    # print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0]))
    # print(find_closest_elements([