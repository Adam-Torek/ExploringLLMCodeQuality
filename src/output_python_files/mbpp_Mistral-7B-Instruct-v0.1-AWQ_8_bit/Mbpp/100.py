"""
Write a function to find the next smallest palindrome of a specified integer, returned as an integer.
assert next_smallest_palindrome(99)==101
"""

def next_smallest_palindrome(n):
    """
    Find the next smallest palindrome of a specified integer.
    """
    # Convert the integer to a string
    s = str(n)
    # Find the length of the string
    length = len(s)
    # Find the next smallest palindrome
    next_palindrome = ""
    for i in range(length):
        # If the length is 1, add a 0 to the end
        if length == 1:
            next_palindrome = "0" + s
        # If the length is greater than 1, add a 0 to the end and reverse the string
        else:
            next_palindrome = "0" + s[::-1]
        # Check if the next palindrome is smaller than the current palindrome
        if int(next_palindrome) < int(s):
            return int(next_palindrome)
    # If no smaller palindrome is found, return the original integer
    return n