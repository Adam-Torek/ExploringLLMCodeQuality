"""
Write a python function to find the sum of even factors of a number.
assert sumofFactors(18) == 26
"""

def sumofFactors(n):
    """
    This function takes an integer n and returns the sum of all its even factors.
    """
    #initialize sum variable
    sum = 0
    #initialize factor variable
    factor = 2
    #initialize while loop
    while factor*factor <= n:
        #check if n is divisible by factor
        if n%factor == 0:
            #if n is divisible by factor, add factor to sum
            sum += factor
        #increment factor
        factor += 1
    #return sum
    return sum

#test the function
assert sumofFactors(18) == 26