from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_val = min(numbers)
    max_val = max(numbers)
    return [((x - min_val) / (max_val - min_val)) for x in numbers]


def rescale_to_unit_with_min(numbers: List[float], min_val: float) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit_with_min([1.0, 2.0, 3.0, 4.0, 5.0], 1.0)
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    max_val = max(numbers)
    return [((x - min_val) / (max_val - min_val)) for x in numbers]


def rescale_to_unit_with_max(numbers: List[float], max_val: float) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit_with_max([1.0, 2.0, 3.0, 4.0, 5.0], 5.0)
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_val = min(numbers)
    return [((x - min_val) / (max_val - min_val)) for x in numbers]


def rescale_to_unit_with_min_max(numbers: List[float], min_val: float, max_val: float) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit_with_min_max([1.0, 2.0, 3.0, 4.0, 5.0], 1.0, 5.0)
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    return [((x - min_val) / (max_val - min_val)) for x in numbers]


def rescale_to_unit_with_min_max_and_offset(numbers: List[float], min_val: float, max_val: float, offset: float) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit_with_min_max_and_offset([1.0, 2.0, 3.0, 4.0, 5.0], 1.0, 5.0, 1.0)
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    return [(x - min_val) / (max_val - min_val) + offset for x in numbers]


def rescale_to_unit_with_min_max_and_offset_and_scale(numbers: List[