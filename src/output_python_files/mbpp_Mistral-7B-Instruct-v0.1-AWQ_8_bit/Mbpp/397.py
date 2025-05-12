"""
Write a function to find the median of three numbers.
assert median_numbers(25,55,65)==55.0
"""

def median_numbers(a,b,c):
    sorted_numbers = sorted(a,b,c)
    n = len(sorted_numbers)
    if n%2 == 0:
        return (sorted_numbers[n//2] + sorted_numbers[(n//2)-1])/2
    else:
        return sorted_numbers[n//2]

assert median_numbers(25,55,65)==55.0