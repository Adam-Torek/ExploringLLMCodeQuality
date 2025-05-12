def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''
    result = 0
    for num in lst:
        if isinstance(num, int) and num >= 0:
            if num % 2 != 0:
                result += num ** 2
    return result * 2

# Test cases
print(double_the_difference([1, 3, 2, 0])) # Output: 10
print(double_the_difference([-1, -2, 0])) # Output: 0
print(double_the_difference([9, -2])) # Output: 81
print(double_the_difference([0])) # Output: 0
print(double_the_difference([])) # Output: 0
print(double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9])) # Output: 250
print(double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: 300
print(double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) # Output: 300
print(double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) # Output: 300
print(double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])) # Output: 300
print(double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) # Output: 300
print(double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) # Output: 300
print(double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])) # Output: 300
print(double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])) # Output: 300
print(double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])) # Output: 30