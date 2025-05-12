"""
Write a function that returns the list in a list of lists whose sum of elements is the highest.
assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]
"""

def max_sum_list(lst):
    max_sum = 0
    max_lst = []
    for i in lst:
        if sum(i) > max_sum:
            max_sum = sum(i)
            max_lst = i
    return max_lst

print(max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])) # Output: [10, 11, 12]
print(max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9], [1,2,3,4,5]])) # Output: [1, 2, 3, 4, 5]
print(max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9], [1,2,3,4,5], [1,2,3,4,5,6,7,8,9,10]])) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Time Complexity: O(n)
# Space Complexity: O(1)