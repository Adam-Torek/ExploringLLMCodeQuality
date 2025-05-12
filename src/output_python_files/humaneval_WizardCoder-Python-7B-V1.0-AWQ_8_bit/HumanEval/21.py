from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_num = min(numbers)
    max_num = max(numbers)
    return [(num - min_num) / (max_num - min_num) for num in numbers]

def rescale_to_range(numbers: List[float], new_min: float, new_max: float) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become new_min and the largest will become new_max
    >>> rescale_to_range([1.0, 2.0, 3.0, 4.0, 5.0], 0.0, 10.0)
    [0.0, 2.0, 4.0, 6.0, 10.0]
    """
    min_num = min(numbers)
    max_num = max(numbers)
    return [(num - min_num) / (max_num - min_num) * (new_max - new_min) + new_min for num in numbers]

def normalize_to_range(numbers: List[float], new_min: float, new_max: float) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become new_min and the largest will become new_max
    >>> normalize_to_range([1.0, 2.0, 3.0, 4.0, 5.0], 0.0, 10.0)
    [0.0, 0.0, 0.0, 0.0]
    """
    min_num = min(numbers)
    max_num = max(numbers)
    return [(num - min_num) / (max_num - min_num) * (new_max - new_min) + new_min for num in numbers]

def normalize_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> normalize_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.0, 0.0, 0.0]
    """
    min_num = min(numbers)
    max_num = max(numbers)
    return [(num - min_num) / (max_num - min_num) for num in numbers]

def normalize_to_zero_one(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> normalize_to_zero_one([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.0, 0.0, 0.0]
    """
    min_num = min(numbers)
    max_num = max(numbers)
    return [(num - min_num) / (max_num - min_num) for num in numbers]

def normalize_to_zero_sum(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the sum of all numbers will become 1
    >>> normalize_to_zero_sum([1.0, 2.0, 3.0, 4.0, 5.0])