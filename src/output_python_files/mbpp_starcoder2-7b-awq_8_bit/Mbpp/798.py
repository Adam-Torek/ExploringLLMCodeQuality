"""
Write a python function to find the sum of an array.
assert _sum([1, 2, 3]) == 6
"""

def _sum(arr):
    """
    Write a python function to find the sum of an array.
    assert _sum([1, 2, 3]) == 6
    """
    return sum(arr)

def test_sum():
    assert _sum([1, 2, 3]) == 6

def test_sum_empty():
    assert _sum([]) == 0

def test_sum_one():
    assert _sum([1]) == 1

def test_sum_negative():
    assert _sum([-1, -2, -3]) == -6

def test_sum_float():
    assert _sum([1.1, 2.2, 3.3]) == 6.6

def test_sum_string():
    assert _sum(['a', 'b', 'c']) == 'abc'

def test_sum_mixed():
    assert _sum([1, 2, 3, 'a', 'b', 'c']) == 'abc6'

def test_sum_mixed_negative():
    assert _sum([-1, -2, -3, 'a', 'b', 'c']) == '-abc6'

def test_sum_mixed_float():
    assert _sum([1.1, 2.2, 3.3, 'a', 'b', 'c']) == 'abc6.6'

def test_sum_mixed_negative_float():
    assert _sum([-1.1, -2.2, -3.3, 'a', 'b', 'c']) == '-abc6.6'

def test_sum_mixed_float_negative():
    assert _sum([-1.1, -2.2, -3.3, 'a', 'b', 'c']) == '-abc6.6'

def test_sum_mixed_float_negative_string():
    assert _sum([-1.1, -2.2, -3.3, 'a', 'b', 'c']) == '-abc6.6'

def test_sum_mixed_float_negative_string_empty():
    assert _sum([-1.1, -2.2, -3.3, 'a', 'b', 'c', '']) == '-abc6.6'

def test_sum_mixed_float_negative_string_empty_one():
    assert _sum([-1.1, -2.2, -3.3, 'a', 'b', 'c', '']) == '-abc6.6'

def test_sum_mixed_float_negative_string_empty_one_empty():
    assert _sum([-1.1, -2.2, -3.3, 'a', 'b', 'c', '', '']) == '-abc6.6'

def test_sum_mixed_float_negative_string_empty_one_empty_one():
    assert _sum([-1.1, -2.2, -3.3, 'a', 'b', 'c', '', '']) == '-abc6.6'

def test_sum_mixed_float_negative_string_empty_one_empty_one_empty():
    assert _sum([-1.1, -2.2, -3.3, 'a', 'b', 'c', '', '']) == '-abc6.6'

def test_sum_mixed_float_negative_string_empty_one_empty_one_empty_one():
    assert _sum([-1.1, -2.2, -3.3, 'a', 'b', 'c', '', '']) == '-abc6.6'

def test_sum_mixed_float_negative_string_empty_one_empty_one_empty_one_empty():
    assert _sum([-1.1, -2.2, -3.3, 'a', 'b', 'c', '', '']) == '-abc6.6'

def test_sum_mixed_float_negative_string_empty_one_empty_one_empty_one_empty_one():
    assert _sum([-1.1, -2.2, -3.3, 'a', 'b', 'c', '', '']) == '-abc6.6'

def test_sum_mixed_float_negative_string_empty_one_empty_one_empty_one_empty_one_empty():
    assert _sum([-1.1,