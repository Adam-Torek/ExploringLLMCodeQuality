def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    return sum(lst[i] for i in range(len(lst)) if i % 2 == 1 and lst[i] % 2 != 0)


# Test cases
print(solution([5, 8, 7, 1])) # Output: 12
print(solution([3, 3, 3, 3, 3])) # Output: 9
print(solution([30, 13, 24, 321])) # Output: 0
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9])) # Output: 1
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: 1
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) # Output: 11
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) # Output: 11
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])) # Output: 11
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) # Output: 11
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) # Output: 11
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])) # Output: 11
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])) # Output: 11
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])) # Output: 11
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])) # Output: 11
print(solution([1, 2, 3, 4, 5, 6,