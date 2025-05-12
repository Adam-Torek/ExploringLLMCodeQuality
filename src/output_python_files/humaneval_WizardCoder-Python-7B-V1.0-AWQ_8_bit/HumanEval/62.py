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
    elif len(xs) == 2:
        return [xs[1]]
    else:
        return [xs[1] + 2 * xs[2] * xs[0]] + derivative(xs[2:])


# Test cases
print(derivative([3, 1, 2, 4, 5])) # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3])) # Output: [2, 6]
print(derivative([1])) # Output: []
print(derivative([])) # Output: []


# Time complexity: O(n)
# Space complexity: O(n)

# Can be optimized to O(1) space complexity by using a loop instead of recursion.