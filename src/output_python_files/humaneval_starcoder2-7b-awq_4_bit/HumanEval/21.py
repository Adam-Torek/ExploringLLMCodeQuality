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

def rescale_to_range_inplace(numbers: List[float], low: float, high: float) -> None:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become low and the largest will become high
    >>> numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    >>> rescale_to_range_inplace(numbers, -1, 1)
    >>> numbers
    [-1.0, -0.5, 0.0, 0.5, 1.0]
    """

def rescale_to_range_inplace_2(numbers: List[float], low: float, high: float) -> None:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become low and the largest will become high
    >>> numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    >>> rescale_to_range_inplace_2(numbers, -1, 1)
    >>> numbers
    [-1.0, -0.5, 0.0, 0.5, 1.0]
    """

def rescale_to_range_inplace_3(numbers: List[float], low: float, high: float) -> None:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become low and the largest will become high
    >>> numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    >>> rescale_to_range_inplace_3(numbers, -1, 1)
    >>> numbers
    [-1.0, -0.5, 0.0, 0.5, 1.0]
    """

def rescale_to_range_inplace_4(numbers: List[float], low: float, high: float) -> None:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become low and the largest will become high
    >>> numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    >>> rescale_to_range_inplace_4(numbers, -1, 1)
    >>> numbers
    [-1.0, -0.5, 0.0, 0.5, 1.0]
    """

def rescale_to_range_inplace_5(numbers: List[float], low: float, high: float) -> None:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become low and the largest will become high
    >>> numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    >>> rescale_to_range_inplace_5(numbers, -1, 1)
    >>> numbers
    [-1.0, -0.5, 0.0, 0.