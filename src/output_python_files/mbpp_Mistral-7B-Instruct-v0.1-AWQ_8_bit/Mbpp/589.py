"""
Write a function to find perfect squares between two given numbers.
assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
"""

def perfect_squares(start, end):
    """
    This function takes two numbers as input and returns a list of all perfect squares between them.
    """
    result = []
    for i in range(start, end+1):
        if i**2 == i:
            result.append(i)
    return result

# Test the function
assert perfect_squares(1,30)==[1, 4, 9, 16, 25]