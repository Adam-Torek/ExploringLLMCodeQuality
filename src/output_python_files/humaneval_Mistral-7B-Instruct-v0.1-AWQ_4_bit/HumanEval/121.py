def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    result = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 1 and i % 2 == 0:
            result += lst[i]
    return result


# Test
lst = [5, 8, 7, 1]
print(solution(lst))