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
    # Your code here
    if not lst:
        return 0
    else:
        lst = [x for x in lst if x > 0 and x % 2 == 1]
        return sum([x**2 for x in lst])


def sum_of_squares(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    sum_of_squares([1, 3, 2, 0]) == 1 + 9 + 4 + 0 = 16
    sum_of_squares([-1, -2, 0]) == 0
    sum_of_squares([9, -2]) == 81
    sum_of_squares([0]) == 0  
   
    If the input list is empty, return 0.
    '''
    # Your code here
    if not lst:
        return 0
    else:
        lst = [x for x in lst if x > 0 and x % 2 == 1]
        return sum([x**2 for x in lst])


def sum_of_squares_of_odd_numbers(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    sum_of_squares_of_odd_numbers([1, 3, 2, 0]) == 1 + 9 + 4 + 0 = 16
    sum_of_squares_of_odd_numbers([-1, -2, 0]) == 0
    sum_of_squares_of_odd_numbers([9, -2]) == 81
    sum_of_squares_of_odd_numbers([0]) == 0  
   
    If the input list is empty, return 0.
    '''
    # Your code here
    if not lst:
        return 0
    else:
        lst = [x for x in lst if x > 0 and x % 2 == 1]
        return sum([x**2 for x in lst])


def sum_of_squares_of_odd_numbers_2(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    sum_of_squares_of_odd_numbers([1, 3, 2, 0]) == 1 + 9 + 4 + 0 = 16
    sum_of_squares_of_odd_numbers([-1, -2, 0]) == 0
    sum_of_squares_of_odd_numbers([9, -2]) == 81
    sum_of_squares_of_odd_numbers([0]) == 0  
   
    If the input list is empty, return 0.
    '''
    # Your code here
    if not lst:
        return 0
    else:
        lst = [x for x in lst if x > 0 and x % 2 == 1]
        return sum([x**2 for x in lst])


def sum_of_squares_of_odd_numbers_3(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    sum_of_squares_of_odd_numbers([1, 3, 2, 0