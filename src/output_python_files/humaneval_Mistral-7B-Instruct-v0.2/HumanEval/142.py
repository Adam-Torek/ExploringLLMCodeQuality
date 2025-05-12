def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """
    sum = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            sum += lst[i] ** 2
        elif i % 3 == 0 and i % 4 != 0:
            sum += lst[i] ** 3
    return sum


# Test cases
print(sum_squares([1, 2, 3]))
print(sum_squares([]))
print(sum_squares([-1, -5, 2, -1, -5]))
print(sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
print(sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
print(sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
print(sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
print(sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
print(sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
print(sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))
print(sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
print(sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
print(sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9,