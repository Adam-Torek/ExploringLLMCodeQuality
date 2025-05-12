"""
Write a function to find the median of three numbers.
assert median_numbers(25,55,65)==55.0
"""
def median_numbers(a,b,c):
    sorted_numbers = sorted([a,b,c])
    if len(sorted_numbers)%2==0:
        return (sorted_numbers[len(sorted_numbers)//2-1]+sorted_numbers[len(sorted_numbers)//2])/2
    else:
        return sorted_numbers[len(sorted_numbers)//2]<|endoftext|>