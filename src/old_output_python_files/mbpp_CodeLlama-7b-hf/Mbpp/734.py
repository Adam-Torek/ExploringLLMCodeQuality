"""
Write a python function to find sum of products of all possible sublists of a given list. https://www.geeksforgeeks.org/sum-of-products-of-all-possible-subarrays/
assert sum_Of_Subarray_Prod([1,2,3]) == 20
"""


def sum_Of_Subarray_Prod(arr):
    n = len(arr)
    # Initialize result
    result = 0
    # Traverse the array
    for i in range(n):
        # Initialize product
        prod = 1
        # Initialize sum
        sum = 0
        # Traverse the array from i to n
        for j in range(i, n):
            # Multiply the product with the current element
            prod = prod * arr[j]
            # Add the product to sum
            sum = sum + prod
        # Add the sum to result
        result = result + sum
    return result


if __name__ == '__main__':
    print(sum_Of_Subarray_Prod([1, 2, 3]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7, 8]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
    print(sum_Of_Subarray_Prod([1, 2, 3, 4, 5,