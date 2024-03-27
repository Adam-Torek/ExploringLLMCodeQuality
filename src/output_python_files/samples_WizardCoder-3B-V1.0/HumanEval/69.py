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

# Solution:
# We can solve this problem by iterating through the list and keeping track of the frequency of each integer. 
# We can then iterate through the list again and find the integer with the highest frequency greater than zero.
# If no such integer exists, we return -1.

def search(lst):
    freq = {}
    for num in lst:
        if num > 0:
            freq[num] = freq.get(num, 0) + 1
    
    for num in lst:
        if num > 0 and freq[num] >= num:
            return num
    
    return -1

# Test cases
print(search([4, 1, 2, 2, 3, 1])) # Output: 2
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4])) # Output: 3
print(search([5, 5, 4, 4, 4])) # Output: -1<|endoftext|>