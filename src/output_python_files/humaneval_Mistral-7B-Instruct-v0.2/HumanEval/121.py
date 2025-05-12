def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    # Your code here!
    sum = 0
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 != 0:
            sum += lst[i]
    return sum

# Test Cases
print(solution([5, 8, 7, 1]))
print(solution([3, 3, 3, 3, 3]))
print(solution([30, 13, 24, 321]))
print(solution([1, 2, 3, 4, 5]))
print(solution([1, 2, 3, 4, 5, 6]))
print(solution([1, 2, 3, 4, 5, 6, 7]))
print(solution([1, 2, 3, 4, 5, 6, 7, 8]))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14