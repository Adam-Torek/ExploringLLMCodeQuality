"""
Write a function to find minimum of three numbers.
assert min_of_three(10,20,0)==0
"""
def min_of_three(num1, num2, num3):
    """
    This function takes three arguments and returns the minimum of the three numbers.
    """
    if num1 <= num2 and num1 <= num3:
        return num1
    elif num2 <= num1 and num2 <= num3:
        return num2
    else:
        return num3

# Test the function
assert min_of_three(10,20,0) == 0
assert min_of_three(1,2,3) == 1
assert min_of_three(5,3,7) == 3
assert min_of_three(10,-5,0) == -5
assert min_of_three(10,20,10) == 10