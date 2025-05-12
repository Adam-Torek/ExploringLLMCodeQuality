"""
Write a function to find the next smallest palindrome of a specified integer, returned as an integer.
assert next_smallest_palindrome(99)==101
"""

def next_smallest_palindrome(n):
    """
    Find the next smallest palindrome of a specified integer.
    """
    # Check if n is a palindrome
    if n == int(str(n)[::-1]):
        return n + 1

    # Find the next smallest odd integer
    while True:
        k = n + 1
        if k % 2 == 1:
            break

    # Find the next smallest even integer
    while True:
        k = n + 2
        if k % 2 == 0:
            break

    # Check if k is a palindrome
    if k == int(str(k)[::-1]):
        return k

    # If k is not a palindrome, check if it is a multiple of 10
    if k % 10 == 0:
        return k + 1

    # If k is not a palindrome and not a multiple of 10, return k
    return k