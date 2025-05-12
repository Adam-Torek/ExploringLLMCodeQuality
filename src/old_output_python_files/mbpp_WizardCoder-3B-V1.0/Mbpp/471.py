"""
Write a python function to find the product of the array multiplication modulo n.
assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9
"""
def find_remainder(arr, n):
    product = 1
    for num in arr:
        product = (product * num) % n
    return product

# Test the function
print(find_remainder([ 100, 10, 5, 25, 35, 14 ],11)) # Output: 9<|endoftext|>