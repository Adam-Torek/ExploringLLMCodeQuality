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
    [0.0, 2.0, 4.0, 6.0, 8.0]
    """
    min_num = min(numbers)
    max_num = max(numbers)
    return [(num - min_num) * (new_max - new_min) / (max_num - min_num) + new_min for num in numbers]

def rescale_to_range_with_outliers(numbers: List[float], new_min: float, new_max: float, outlier_percent: float) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become new_min and the largest will become new_max,
    but with a certain percentage of outliers removed from the extremes
    >>> rescale_to_range_with_outliers([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0], 0.0, 10.0, 0.1)
    [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    """
    min_num = min(numbers)
    max_num = max(numbers)
    outlier_count = int(len(numbers) * outlier_percent)
    sorted_numbers = sorted(numbers)
    return rescale_to_range(sorted_numbers[outlier_count:-outlier_count], new_min, new_max)

def rescale_to_range_with_outliers_and_zeros(numbers: List[float], new_min: float, new_max: float, outlier_percent: float) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become new_min and the largest will become new_max,
    but with a certain percentage of outliers and zeros removed from the extremes
    >>> rescale_to_range_with_outliers_and_zeros([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 0.0], 0.0, 10.0, 0.1)
    [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    """
    min_num = min