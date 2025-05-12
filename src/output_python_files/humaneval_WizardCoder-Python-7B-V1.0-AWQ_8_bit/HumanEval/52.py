def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for num in l:
        if num >= t:
            return False
    return True


# Test cases
print(below_threshold([1, 2, 4, 10], 100) == True)
print(below_threshold([1, 20, 4, 10], 5) == False)
print(below_threshold([1, 2, 4, 10], 5) == False)
print(below_threshold([1, 2, 4, 10], 15) == True)
print(below_threshold([1, 2, 4, 10], 1) == False)
print(below_threshold([1, 2, 4, 10], 0) == False)
print(below_threshold([1, 2, 4, 10], 10) == True)
print(below_threshold([1, 2, 4, 10], 7) == False)
print(below_threshold([1, 2, 4, 10], 6) == True)
print(below_threshold([1, 2, 4, 10], 3) == False)
print(below_threshold([1, 2, 4, 10], 2) == True)
print(below_threshold([1, 2, 4, 10], 1) == False)
print(below_threshold([1, 2, 4, 10], 0) == False)
print(below_threshold([1, 2, 4, 10], 1) == False)
print(below_threshold([1, 2, 4, 10], 0) == False)
print(below_threshold([1, 2, 4, 10], 1) == False)
print(below_threshold([1, 2, 4, 10], 0) == False)
print(below_threshold([1, 2, 4, 10], 1) == False)
print(below_threshold([1, 2, 4, 10], 0) == False)
print(below_threshold([1, 2, 4, 10], 1) == False)
print(below_threshold([1, 2, 4, 10], 0) == False)
print(below_threshold([1, 2, 4, 10], 1) == False)
print(below_threshold([1, 2, 4, 10], 0) == False)
print(below_threshold([1, 2, 4, 10], 1) == False)
print(below_threshold([1, 2, 4, 10], 0) == False)
print(below_threshold([1, 2, 4, 10], 1) == False)
print(below_threshold([1, 2, 4, 10], 0) == False)
print(below_threshold([1, 2, 4, 10], 1) == False)
print(below_threshold([1, 2, 4, 10], 0) == False)
print(below_threshold([1, 2, 4, 10], 1) == False)
print(below_threshold([1, 2, 4, 10], 0) == False)
print(below_threshold([1, 2, 4, 10], 1) == False)
print(below_threshold([1, 2, 4, 10], 0) == False)
print(below_threshold([1, 2, 4, 10], 1) == False)
print(below_threshold([1, 2,