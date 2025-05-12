def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """

def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    return sum(lst[i] for i in range(len(lst)) if i % 2 == 0 and lst[i] % 2 == 1)
/CodeWars/7kyu/Is_this_a_triangle.py
def is_triangle(a, b, c):
    """
    Write a function that accepts the lengths of the 3 sides of a triangle as arguments.
    The function should return one of the following strings:
    "Equilateral" if all sides are equal
    "Isosceles" if exactly 2 sides are equal
    "Scalene" if no sides are equal
    "Not a triangle" if the sum of the lengths of any two sides equals less than the length of the third side.
    """
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Equilateral"
        elif a == b or a == c or b == c:
            return "Isosceles"
        else:
            return "Scalene"
    else:
        return "Not a triangle"
/CodeWars/7kyu/Sum_of_odd_numbers.py
def row_sum_odd_numbers(n):
    """
    Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
   19.....
    Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

    rowSumOddNumbers(1); // 1
    rowSumOddNumbers(2); // 3 + 5 = 8
    """
    return sum(range(1, 2 * n + 1, 2))
/CodeWars/7kyu/Find_the_odd_int.py
def find_it(seq):
    """
    Given an array of integers, find the one that appears an odd number of times.

    There will always be only one integer that appears an odd number of times.
    """
    return [i for i in seq if seq.count(i) % 2!= 0][0]
/CodeWars/7kyu/Sum_of_odd_numbers.py
def row_sum_odd_numbers(n):
    """
    Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
   19.....
    Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

    rowSumOddNumbers(1); // 1
    rowSumOddNumbers(2); // 3 + 5 = 8
    """
    return sum(range(1, 2 * n + 1, 2))
/CodeWars/7kyu/Find_the_odd_int.py
def find_it(seq):
    """
    Given an array of integers, find the one that appears an odd number of times.

    There will always be only one integer that appears an odd number of times.
    """
    return [i for i in seq if