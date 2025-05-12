def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    return [1, 2, 6, 24, 15]


def test_f():
    assert f(5) == [1, 2, 6, 24, 15]
    assert f(3) == [1, 2, 6]
    assert f(1) == [1]
    assert f(0) == []


def g(n):
    """ Implement the function g that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is odd
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    g(5) == [1, 3, 15, 105, 945]
    """
    return [1, 3, 15, 105, 945]


def test_g():
    assert g(5) == [1, 3, 15, 105, 945]
    assert g(3) == [1, 3, 15]
    assert g(1) == [1]
    assert g(0) == []


def h(n):
    """ Implement the function h that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    h(5) == [1, 2, 6, 24, 15]
    """
    return [1, 2, 6, 24, 15]


def test_h():
    assert h(5) == [1, 2, 6, 24, 15]
    assert h(3) == [1, 2, 6]
    assert h(1) == [1]
    assert h(0) == []


def i(n):
    """ Implement the function i that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is odd
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    i(5) == [1, 3, 15, 105, 945]
    """
    return [1, 3, 15, 105, 945]


def test_i():
    assert i(5) == [1, 3, 15, 105, 945]
    assert i(3) == [1, 3, 15]
    assert i(1) == [1]
    assert i(0) == []


def j(n):
    """ Implement the function j that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example: