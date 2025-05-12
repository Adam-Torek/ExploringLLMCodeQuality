from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

def rescale_to_range(numbers: List[float], low: float, high: float) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become low and the largest will become high
    >>> rescale_to_range([1.0, 2.0, 3.0, 4.0, 5.0], -1, 1)
    [-1.0, -0.5, 0.0, 0.5, 1.0]
    """

def rescale_to_range_with_offset(numbers: List[float], low: float, high: float, offset: float) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become low and the largest will become high,
    with the offset being the midpoint between the two
    >>> rescale_to_range_with_offset([1.0, 2.0, 3.0, 4.0, 5.0], -1, 1, 0)
    [-1.0, -0.5, 0.0, 0.5, 1.0]
    >>> rescale_to_range_with_offset([1.0, 2.0, 3.0, 4.0, 5.0], -1, 1, 0.5)
    [-0.5, 0.0, 0.5, 1.0, 1.5]
    """

def rescale_to_range_with_offset_and_scale(numbers: List[float], low: float, high: float, offset: float, scale: float) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become low and the largest will become high,
    with the offset being the midpoint between the two, and the scale being the ratio between the two
    >>> rescale_to_range_with_offset_and_scale([1.0, 2.0, 3.0, 4.0, 5.0], -1, 1, 0, 2)
    [-1.0, -0.5, 0.0, 0.5, 1.0]
    >>> rescale_to_range_with_offset_and_scale([1.0, 2.0, 3.0, 4.0, 5.0], -1, 1, 0.5, 2)
    [-0.5, 0.0, 0.5, 1.0, 1.5]
    """

def rescale_to_range_with_offset_and_scale_and_exponent(numbers: List[float], low: float, high: float, offset: float, scale: float, exponent: float) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become low and the largest will become high,
    with the offset being the midpoint between the two, and the scale being the ratio between the two,
    and the exponent being the power to which the numbers are raised
    >>> rescale_to_range_with_offset_and_scale_and_exponent([1.0, 2.0, 3.0, 4.0, 5.0], -1, 1, 0, 2, 1)
    [-1.0, -0.5, 0.0, 0.5, 1.0]
    >>> rescale_to_range_with_offset_and_scale_and_exponent([1.0, 2.0, 3.0, 4.0, 5.0], -1, 1, 0.5,