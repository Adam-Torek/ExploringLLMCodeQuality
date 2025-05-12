"""
Write a function to determine if the sum of the divisors of two integers are the same.
assert are_equivalent(36, 57) == False
"""

def are_equivalent(num1, num2):
    """
    Determine if the sum of the divisors of two integers are the same.
    """
    # Find the divisors of each number
    divs1 = [1]
    for i in range(2, num1+1):
        if num1 % i == 0:
            divs1.append(i)
    divs2 = [1]
    for i in range(2, num2+1):
        if num2 % i == 0:
            divs2.append(i)
    # Check if the sum of the divisors are the same
    if sum(divs1) == sum(divs2):
        return True
    else:
        return False

# Test the function
assert are_equivalent(36, 57) == False
assert are_equivalent(12, 12) == True