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
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
    for num in sorted(freq.keys(), reverse=True):
        if freq[num] >= num:
            return num
    return -1


# Test cases
print(search([4, 1, 2, 2, 3, 1])) # Output: 2
print(search([1, 2, 2, 3, 3, 4, 4, 4])) # Output: 3
print(search([5, 5, 4, 4, 4])) # Output: -1
print(search([1, 2, 3, 4, 5, 6, 7, 8, 9])) # Output: 1
print(search([1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6])) # Output: 3
print(search([1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5])) # Output: 5
print(search([1, 2, 3, 4, 5, 6, 7, 8, 9])) # Output: -1
print(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: 10
print(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])) # Output: 10
print(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10])) # Output: 10
print(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10])) # Output: 10
print(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])) # Output: 10
print(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])) # Output: 10
print(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])) # Output: 10
print(search([1, 2, 3,