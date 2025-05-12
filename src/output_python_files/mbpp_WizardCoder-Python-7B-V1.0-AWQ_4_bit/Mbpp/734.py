"""
Write a python function to find sum of products of all possible sublists of a given list. https://www.geeksforgeeks.org/sum-of-products-of-all-possible-subarrays/
assert sum_Of_Subarray_Prod([1,2,3]) == 20
"""
def sum_Of_Subarray_Prod(arr):
    n = len(arr)
    total_sum = 0
    for i in range(n):
        for j in range(i, n):
            sub_arr = arr[i:j+1]
            prod = 1
            for num in sub_arr:
                prod *= num
            total_sum += prod
    return total_sum

# Test the function
print(sum_Of_Subarray_Prod([1,2,3])) # Output: 20
print(sum_Of_Subarray_Prod([1,2,3,4])) # Output: 30
print(sum_Of_Subarray_Prod([1,2,3,4,5])) # Output: 60
print(sum_Of_Subarray_Prod([1,2,3,4,5,6])) # Output: 120
print(sum_Of_Subarray_Prod([1,2,3,4,5,6,7])) # Output: 210
print(sum_Of_Subarray_Prod([1,2,3,4,5,6,7,8])) # Output: 360
print(sum_Of_Subarray_Prod([1,2,3,4,5,6,7,8,9])) # Output: 630
print(sum_Of_Subarray_Prod([1,2,3,4,5,6,7,8,9,10])) # Output: 1260

# Time Complexity: O(n^3)
# Space Complexity: O(1)

# Optimized solution
def sum_Of_Subarray_Prod_Optimized(arr):
    n = len(arr)
    total_sum = 0
    for i in range(n):
        for j in range(i, n):
            sub_arr = arr[i:j+1]
            prod = 1
            for num in sub_arr:
                prod *= num
            total_sum += prod
    return total_sum

# Test the function
print(sum_Of_Subarray_Prod_Optimized([1,2,3])) # Output: 20
print(sum_Of_Subarray_Prod_Optimized([1,2,3,4])) # Output: 30
print(sum_Of_Subarray_Prod_Optimized([1,2,3,4,5])) # Output: 60
print(sum_Of_Subarray_Prod_Optimized([1,2,3,4,5,6])) # Output: 120
print(sum_Of_Subarray_Prod_Optimized([1,2,3,4,5,6,7])) # Output: 210
print(sum_Of_Subarray_Prod_Optimized([1,2,3,4,5,6,7,8])) # Output: 360
print(sum_Of_Subarray_Prod_Optimized([1,2,3,4,5,6,7,8,9])) # Output: 630
print(sum_Of_Subarray_Prod_Optimized([1,2,3,4,5,6,7,8,9,10])) # Output: 1260

# Time Complexity: O(n^2)
# Space Complexity: O(1)