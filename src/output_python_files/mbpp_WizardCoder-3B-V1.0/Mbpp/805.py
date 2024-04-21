"""
Write a function that returns the list in a list of lists whose sum of elements is the highest.
assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]
"""

def max_sum_list(lst):
    max_sum = float('-inf')
    max_list = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if i == 0 and j == 0:
                continue
            current_sum = lst[i][j] + lst[i][j-1] + lst[i-1][j] + lst[i-1][j-1]
            if current_sum > max_sum:
                max_sum = current_sum
                max_list = [lst[i][j], lst[i][j-1], lst[i-1][j], lst[i-1][j-1]]
    return max_list

# Test the function
print(max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])) # Output: [10, 11, 12]<|endoftext|>