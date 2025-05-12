"""
Write a function to find the product of first even and odd number of a given list.
assert mul_even_odd([1,3,5,7,4,1,6,8])==4
"""
def mul_even_odd(lst):
    even_product = 1
    odd_product = 1
    for num in lst:
        if num % 2 == 0:
            even_product *= num
        else:
            odd_product *= num
    return even_product * odd_product

print(mul_even_odd([1,3,5,7,4,1,6,8])) # Output: 4