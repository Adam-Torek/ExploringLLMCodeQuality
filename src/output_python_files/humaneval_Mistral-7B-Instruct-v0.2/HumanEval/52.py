def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for num in l:
        if num > t:
            return False
    return True

# Test cases
# Test case 1
# Test that all numbers in the list are below threshold 100
# Test case 2
# Test that not all numbers in the list are below threshold 5
# Test case 3
# Test that all numbers in the empty list are below threshold 100
# Test case 4
# Test that all numbers in the list are below threshold 0
# Test case 5
# Test that all numbers in the list are below threshold -10
# Test case 6
# Test that all numbers in the list are below threshold 5000
# Test case 7
# Test that all numbers in the list are below threshold 1
# Test case 8
# Test that all numbers in the list are below threshold 10
# Test case 9
# Test that all numbers in the list are below threshold 1000000
# Test case 10
# Test that all numbers in the list are below threshold -1000000
# Test case 11
# Test that all numbers in the list are below threshold 1.0
# Test case 12
# Test that all numbers in the list are below threshold 10.0
# Test case 13
# Test that all numbers in the list are below threshold 1000000.0
# Test case 14
# Test that all numbers in the list are below threshold 1000000000.0
# Test case 15
# Test that all numbers in the list are below threshold 1.0e10
# Test case 16
# Test that all numbers in the list are below threshold 1.0e11
# Test case 17
# Test that all numbers in the list are below threshold 1.0e12
# Test case 18
# Test that all numbers in the list are below threshold 1.0e13
# Test case 19
# Test that all numbers in the list are below threshold 1.0e14
# Test case 20
# Test that all numbers in the list are below threshold 1.0e15
# Test case 21
# Test that all numbers in the list are below threshold 1.0e16
# Test case 22
# Test that all numbers in the list are below threshold 1.0e17
# Test case 23
# Test that all numbers in the list are below threshold 1.0e18
# Test case 24
# Test that all numbers in the list are below threshold 1.0e19
# Test case 25
# Test that all numbers in the list are below threshold 1.0e20
# Test case 26
# Test that all numbers in the list are below threshold 1.0e21
# Test case 27
# Test that all numbers in the list are below threshold 1.0e22
# Test case 28
# Test that all numbers in the list are below threshold 1.0e23
# Test case 29
# Test that all numbers in the list are below threshold 1.0e24
# Test case 30
# Test that all numbers in the list are below threshold 1.0e25
# Test case 31
# Test that all numbers in the list are below threshold 1.0e26
# Test case 32
# Test that all numbers in the list are below threshold 1.0e27
# Test case 33
# Test that all numbers in the list are below threshold 1.0e28
# Test case 34
# Test that all numbers in the list are below threshold 1.0e29
# Test case 35
# Test that all numbers in the list are below threshold 1.0e30
# Test case 36
# Test that all numbers in the list are below threshold 1.0e31
# Test