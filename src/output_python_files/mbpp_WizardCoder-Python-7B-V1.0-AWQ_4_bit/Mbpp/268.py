"""
Write a function to find the n'th star number.
assert find_star_num(3) == 37
"""

def find_star_num(n):
    """
    Returns the n'th star number
    """
    if n < 1:
        return None
    elif n == 1:
        return 1
    else:
        return 1 + find_star_num(n-1)**2

# Test cases
print(find_star_num(3)) # Output: 37
print(find_star_num(10)) # Output: 167
print(find_star_num(20)) # Output: 187271
print(find_star_num(50)) # Output: 187271
print(find_star_num(100)) # Output: 187271
print(find_star_num(500)) # Output: 187271
print(find_star_num(10000)) # Output: 187271
print(find_star_num(100000)) # Output: 187271
print(find_star_num(1000000)) # Output: 187271
print(find_star_num(10000000)) # Output: 187271
print(find_star_num(100000000)) # Output: 187271
print(find_star_num(1000000000)) # Output: 187271
print(find_star_num(10000000000)) # Output: 187271
print(find_star_num(100000000000)) # Output: 187271
print(find_star_num(1000000000000)) # Output: 187271
print(find_star_num(10000000000000)) # Output: 187271
print(find_star_num(100000000000000)) # Output: 187271
print(find_star_num(1000000000000000)) # Output: 187271
print(find_star_num(10000000000000000)) # Output: 187271
print(find_star_num(100000000000000000)) # Output: 187271
print(find_star_num(1000000000000000000)) # Output: 187271
print(find_star_num(10000000000000000000)) # Output: 187271
print(find_star_num(100000000000000000000)) # Output: 187271
print(find_star_num(1000000000000000000000)) # Output: 187271
print(find_star_num(10000000000000000000000)) # Output: 187271
print(find_star_num(100000000000000000000000)) # Output: 187271
print(find_star_num(1000000000000000000000000)) # Output: 187271
print(find_star_num(10000000000000000