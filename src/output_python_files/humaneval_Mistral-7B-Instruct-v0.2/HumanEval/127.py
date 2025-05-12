def intersection(interval1, interval2):
    """You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two 
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".


    [input/output] samples:
    intersection((1, 2), (2, 3)) ==> "NO"
    intersection((-1, 1), (0, 4)) ==> "NO"
    intersection((-3, -1), (-5, 5)) ==> "YES"
    """
    if interval1[1] < interval2[0]:
        return "NO"
    if interval1[1] < interval2[1]:
        return "NO"
    return "YES" if (interval1[0]-interval2[0]) in [x for x in range(2,1000000) if all(x%i for i in range(2,int(x**0.5)+1)))] else "NO"

# Testing
print(intersection((1, 2), (2, 3))) # NO
print(intersection((-1, 1), (0, 4))) # NO
print(intersection((-3, -1), (-5, 5))) # YES
print(intersection((1, 2), (3, 4))) # NO
print(intersection((1, 2), (1, 2))) # YES
print(intersection((1, 2), (1, 3))) # NO
print(intersection((1, 2), (2, 2))) # YES
print(intersection((1, 2), (2, 2000000))) # NO
print(intersection((1, 2), (2000000, 2))) # NO
print(intersection((1, 2), (2000000, 2000000))) # YES
print(intersection((1, 2), (2000001, 2000001))) # YES
print(intersection((1, 2), (2000001, 2000002))) # NO
print(intersection((1, 2), (2000001, 2000003))) # NO
print(intersection((1, 2), (2000001, 2000004))) # NO
print(intersection((1, 2), (2000001, 2000005))) # NO
print(intersection((1, 2), (2000001, 2000006))) # NO
print(intersection((1, 2), (2000001, 2000007))) # NO
print(intersection((1, 2), (2000001, 2000008))) # NO
print(intersection((1, 2), (2000001, 2000009))) # NO
print(intersection((1, 2), (2000001, 2000010))) # NO
print(intersection((1, 2), (2000001, 2000011))) # NO
print(intersection((1, 2), (2000001, 2000012))) # NO
print(intersection((1, 2), (200