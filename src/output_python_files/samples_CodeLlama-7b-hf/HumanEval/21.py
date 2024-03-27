from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List of numbers must have at least two elements")
    min_val = min(numbers)
    max_val = max(numbers)
    return [(x - min_val) / (max_val - min_val) for x in numbers]


def rescale_to_unit_with_min_max(numbers: List[float], min_val: float, max_val: float) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become min_val and the largest will become max_val
    >>> rescale_to_unit_with_min_max([1.0, 2.0, 3.0, 4.0, 5.0], 0.0, 1.0)
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List of numbers must have at least two elements")
    return [(x - min(numbers)) / (max(numbers) - min(numbers)) * (max_val - min_val) + min_val for x in numbers]


def rescale_to_unit_with_min_max_and_offset(numbers: List[float], min_val: float, max_val: float, offset: float) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become min_val and the largest will become max_val
    >>> rescale_to_unit_with_min_max_and_offset([1.0, 2.0, 3.0, 4.0, 5.0], 0.0, 1.0, 0.5)
    [0.5, 0.75, 1.0, 1.25, 1.5]
    """
    if len(numbers) < 2:
        raise ValueError("List of numbers must have at least two elements")
    return [(x - min(numbers)) / (max(numbers) - min(numbers)) * (max_val - min_val) + min_val + offset for x in numbers]


def rescale_to_unit_with_min_max_and_offset_and_scale(numbers: List[float], min_val: float, max_val: float, offset: float, scale: float) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become min_val and the largest will become max_val
    >>> rescale_to_unit_with_min_max_and_offset_and_scale([1.0, 2.0, 3.0, 4.0, 5.0], 0.0, 1.0, 0.5, 0.5)
    [0.5, 1.0, 1.5, 2.0, 2.5]
    """
    if len(numbers) < 2:
        raise ValueError("List of numbers must have at least two elements")
    return [(x - min(numbers)) / (max(numbers) - min(numbers)) * (max_val - min_val) * scale + min_val + offset for x in numbers]


def rescale_to_unit_with_min_max_and_offset_and_scale_and_round(numbers: List[float], min_val: float, max_val: float, offset: float, scale: float, round_to: int) ->