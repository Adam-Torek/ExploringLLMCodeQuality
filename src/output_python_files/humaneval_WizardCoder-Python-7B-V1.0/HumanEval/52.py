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
# The function takes in a list l and a threshold t as arguments. It then iterates through each number in the list and checks if it is greater than or equal to t. If any number is greater than or equal to t, it returns False. If all numbers are less than t, it returns True.