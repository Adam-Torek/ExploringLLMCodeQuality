"""
Write a python function to find a pair with highest product from a given array of integers.
assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
"""

def max_Product(arr):
    """
    Function to find a pair with highest product from a given array of integers.
    """
    max_product = 1
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            product = arr[i]*arr[j]
            if product > max_product:
                max_product = product
                max_pair = (arr[i],arr[j])
    return max_pair

# Testing the function
arr = [1,2,3,4,7,0,8,4]
print(max_Product(arr))