"""
Write a function to find the median of three numbers.
assert median_numbers(25,55,65)==55.0
"""

def median_numbers(a,b,c):
    sorted_numbers = sorted(a,b,c)
    n = len(sorted_numbers)
    mid = n//2
    if n%2 == 0:
        median = (sorted_numbers[mid-1] + sorted_numbers[mid])/2
    else:
        median = sorted_numbers[mid]
    return median

assert median_numbers(25,55,65)==55.0