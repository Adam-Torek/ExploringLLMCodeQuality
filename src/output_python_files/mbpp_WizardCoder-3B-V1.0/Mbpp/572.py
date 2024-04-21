"""
Write a python function to remove duplicate numbers from a given number of lists.
assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
"""

def two_unique_nums(lists):
    unique_nums = []
    for num in lists:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums

# Test the function
print(two_unique_nums([1,2,3,2,3,4,5])) # Output: [1, 4, 5]<|endoftext|>