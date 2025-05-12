def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if len(xs) == 1:
        return []
    else:
        return [xs[1] * (i + 1) for i in range(len(xs) - 1)]


# test cases
print(derivative([3, 1, 2, 4, 5])) # [1, 4, 12, 20]
print(derivative([1, 2, 3])) # [2, 6]
print(derivative([1])) # []
print(derivative([])) # []


# Time complexity: O(n)
# Space complexity: O(n)

# Can be optimized by using a loop instead of list comprehension.
# But the list comprehension is more concise and readable.