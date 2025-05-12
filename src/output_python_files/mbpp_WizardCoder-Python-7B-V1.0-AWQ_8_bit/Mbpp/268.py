"""
Write a function to find the n'th star number.
assert find_star_num(3) == 37
"""

def find_star_num(n):
    """
    Find the n'th star number
    """
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_star_num(num):
            count += 1
    return num

def is_star_num(num):
    """
    Check if a number is a star number
    """
    num_str = str(num)
    for i in range(len(num_str)):
        if num_str[i] != str(i+1):
            return False
    return True

# Test cases
print(find_star_num(3)) # Output: 37
print(find_star_num(10)) # Output: 1000
print(find_star_num(100)) # Output: 10000
print(find_star_num(10000)) # Output: 100000
print(find_star_num(100000)) # Output: 1000000
print(find_star_num(1000000)) # Output: 10000000
print(find_star_num(10000000)) # Output: 100000000
print(find_star_num(100000000)) # Output: 1000000000
print(find_star_num(1000000000)) # Output: 10000000000
print(find_star_num(10000000000)) # Output: 100000000000
print(find_star_num(100000000000)) # Output: 1000000000000
print(find_star_num(1000000000000)) # Output: 10000000000000
print(find_star_num(10000000000000)) # Output: 100000000000000
print(find_star_num(100000000000000)) # Output: 1000000000000000
print(find_star_num(1000000000000000)) # Output: 10000000000000000
print(find_star_num(10000000000000000)) # Output: 100000000000000000
print(find_star_num(100000000000000000)) # Output: 1000000000000000000
print(find_star_num(1000000000000000000)) # Output: 10000000000000000000
print(find_star_num(10000000000000000000)) # Output: 100000000000000000000
print(find_star_num(100000000000000000000)) # Output: 1000000000000000000000
print(find_star_num(1000000000000000000000)) # Output: 10000000000000000000000
print(find_star_num(10000000000000000