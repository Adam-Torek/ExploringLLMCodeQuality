"""
Write a function to find the next smallest palindrome of a specified integer, returned as an integer.
assert next_smallest_palindrome(99)==101
"""
def is_palindrome(num):
    return str(num) == str(num)[::-1]

def next_smallest_palindrome(num):
    if is_palindrome(num):
        return num + 1
    else:
        while True:
            num += 1
            if is_palindrome(num):
                return num

# Test cases
print(next_smallest_palindrome(99)) # Output: 101<|endoftext|>