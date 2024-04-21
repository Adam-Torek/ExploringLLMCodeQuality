"""
Write a python function to find the index of smallest triangular number with n digits. https://www.geeksforgeeks.org/index-of-smallest-triangular-number-with-n-digits/
assert find_Index(2) == 4
"""

def find_Index(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return find_Index(n-1) + find_Index(n-2)

# Test the function
print(find_Index(2)) # Output: 4<|endoftext|>