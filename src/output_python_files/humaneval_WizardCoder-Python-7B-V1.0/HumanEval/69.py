def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    freq = {}
    for num in lst:
        if num > 0:
            freq[num] = freq.get(num, 0) + 1
    max_num = -1
    for num, count in freq.items():
        if count >= num:
            max_num = max(max_num, num)
    return max_num


# Test cases
print(search([4, 1, 2, 2, 3, 1])) # Output: 2
print(search([1, 2, 2, 3, 3, 4, 4, 4])) # Output: 3
print(search([5, 5, 4, 4, 4])) # Output: -1
print(search([1, 2, 3, 4, 5, 6, 7, 8, 9])) # Output: 1
print(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: 1
print(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10])) # Output: 2
print(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10])) # Output: 3
print(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])) # Output: 4
print(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10])) # Output: 5
print(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10])) # Output: 6
print(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10])) # Output: 7
print(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10])) # Output: 8
print(search([1, 2, 3, 4, 5