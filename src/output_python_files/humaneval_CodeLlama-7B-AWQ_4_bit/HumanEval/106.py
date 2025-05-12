def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    return [1 if i % 2 == 0 else sum(range(1, i + 1)) for i in range(1, n + 1)]


def test_f():
    assert f(5) == [1, 2, 6, 24, 15]
    assert f(10) == [1, 2, 6, 24, 15, 120, 720, 5040, 40320, 362880]
    assert f(100) == [1, 2, 6, 24, 15, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 4