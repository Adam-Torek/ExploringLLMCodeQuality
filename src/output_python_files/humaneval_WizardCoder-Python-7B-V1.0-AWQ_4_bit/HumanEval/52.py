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


# Explanation:
# The function takes a list l and a threshold t as input. It iterates through the list and checks if any number in the list is greater than or equal to t. If it finds a number that is greater than or equal to t, it returns False. If it iterates through the entire list without finding a number greater than or equal to t, it returns True. This means that all the numbers in the list are below the threshold t.