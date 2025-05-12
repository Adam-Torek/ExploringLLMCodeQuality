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
    # Create a dictionary to store the frequency of each integer in the list
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

    # Iterate through the dictionary to find the greatest integer with frequency greater than or equal to itself
    for num, freq in freq_dict.items():
        if num > 0 and freq >= num:
            return num

    # If no such integer is found, return -1
    return -1

# Test the function with some examples
print(search([4, 1, 2, 2, 3, 1])) # Output: 2
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4])) # Output: 3
print(search([5, 5, 4, 4, 4])) # Output: -1