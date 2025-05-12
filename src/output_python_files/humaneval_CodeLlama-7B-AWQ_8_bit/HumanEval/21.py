from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)
    if min_value == max_value:
        raise ValueError("List must contain at least two different elements")

    return [
        (number - min_value) / (max_value - min_value)
        for number in numbers
    ]


def rescale_to_unit_with_min_max(numbers: List[float], min_value: float, max_value: float) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become min_value and the largest will become max_value
    >>> rescale_to_unit_with_min_max([1.0, 2.0, 3.0, 4.0, 5.0], 0.0, 1.0)
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    if min_value == max_value:
        raise ValueError("min_value and max_value must be different")

    return [
        (number - min_value) / (max_value - min_value)
        for number in numbers
    ]


def rescale_to_unit_with_min_max_and_step(numbers: List[float], min_value: float, max_value: float, step: float) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become min_value and the largest will become max_value
    and the step will be applied to the result
    >>> rescale_to_unit_with_min_max_and_step([1.0, 2.0, 3.0, 4.0, 5.0], 0.0, 1.0, 0.1)
    [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    if min_value == max_value:
        raise ValueError("min_value and max_value must be different")

    if step <= 0:
        raise ValueError("step must be positive")

    return [
        min_value + step * (number - min_value) / (max_value - min_value)
        for number in numbers
    ]


def rescale_to_unit_with_min_max_and_step_and_offset(numbers: List[float], min_value: float, max_value: float, step: float, offset: float) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become min_value and the largest will become max_value
    and the step will be applied to the result and the offset will be added to the result
    >>> rescale_to_unit_with_min_max_and_step_and_offset([1.0, 2.0, 3.0, 4.0, 5.0], 0.0, 1.0, 0.1, 0.5)
    [0.5,