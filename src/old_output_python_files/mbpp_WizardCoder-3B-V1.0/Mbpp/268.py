"""
Write a function to find then'th star number.
assert find_star_num(3) == 37
"""

def find_star_num(n):
    if n == 1:
        return 1
    else:
        return 10 * find_star_num(n-1) + n

print(find_star_num(3))<|endoftext|>