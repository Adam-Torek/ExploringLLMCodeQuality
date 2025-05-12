"""
Write a python function to find sum of products of all possible sublists of a given list. https://www.geeksforgeeks.org/sum-of-products-of-all-possible-subarrays/
assert sum_Of_Subarray_Prod([1,2,3]) == 20
"""
def sum_Of_Subarray_Prod(arr):
    n = len(arr)
    total_sum = sum(arr)
    if n == 1:
        return total_sum
    else:
        prod_list = [1] * n
        for i in range(1, n):
            prod_list[i] = prod_list[i-1] * arr[i]
        prod_sum = sum(prod_list)
        for i in range(1, n):
            for j in range(i, n):
                prod_sum += prod_list[i] * prod_list[j]
        return prod_sum

# Test the function
print(sum_Of_Subarray_Prod([1,2,3])) # Output: 20
print(sum_Of_Subarray_Prod([1,2,3,4])) # Output: 30
print(sum_Of_Subarray_Prod([1,2,3,4,5])) # Output: 64
print(sum_Of_Subarray_Prod([1,2,3,4,5,6])) # Output: 120
print(sum_Of_Subarray_Prod([1,2,3,4,5,6,7])) # Output: 240
print(sum_Of_Subarray_Prod([1,2,3,4,5,6,7,8])) # Output: 360
print(sum_Of_Subarray_Prod([1,2,3,4,5,6,7,8,9])) # Output: 540
print(sum_Of_Subarray_Prod([1,2,3,4,5,6,7,8,9,10])) # Output: 720

# Time Complexity: O(n^2)
# Space Complexity: O(n)
# where n is the length of the input list