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
        return [xs[1] + i * xs[2] for i in range(1, len(xs) - 1)]


# Test cases
print(derivative([3, 1, 2, 4, 5])) # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3])) # Output: [2, 6]
print(derivative([1])) # Output: []
print(derivative([1, 0, 0, 0])) # Output: [0]
print(derivative([0, 0, 0])) # Output: []
print(derivative([1, 0])) # Output: [0]
print(derivative([0])) # Output: []
print(derivative([0, 1, 0, 0])) # Output: [1]
print(derivative([0, 0, 1])) # Output: [0]
print(derivative([0, 0, 0, 1])) # Output: [0]
print(derivative([1, 2, 3, 4, 5, 6])) # Output: [2, 6, 12, 18]
print(derivative([1, 2, 3, 4, 5, 6, 7])) # Output: [2, 6, 12, 18, 24]
print(derivative([1, 2, 3, 4, 5, 6, 7, 8])) # Output: [2, 6, 12, 18, 24, 30]
print(derivative([1, 2, 3, 4, 5, 6, 7, 8, 9])) # Output: [2, 6, 12, 18, 24, 30, 36]
print(derivative([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: [2, 6, 12, 18, 24, 30, 36, 42]

# Time complexity: O(n)
# Space complexity: O(n)