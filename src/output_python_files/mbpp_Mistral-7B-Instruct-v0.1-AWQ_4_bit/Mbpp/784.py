"""
Write a function to find the product of first even and odd number of a given list.
assert mul_even_odd([1,3,5,7,4,1,6,8])==4
"""
def mul_even_odd(lst):
    """
    :param lst: list of integers
    :return: product of first even and odd number of the list
    """
    even_num = 0
    odd_num = 0
    for num in lst:
        if num % 2 == 0:
            even_num += num
        else:
            odd_num += num
    if even_num == 0 or odd_num == 0:
        return 0
    else:
        return even_num * odd_num

# assert mul_even_odd([1,3,5,7,4,1,6,8])==4
# assert mul_even_odd([1,3,5,7,4,1,6,8,9,10])==90
# assert mul_even_odd([1,3,5,7,4,1,6,8,9,10,11,12,13,14,15,16,17,18,19,20])==1080