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
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def intersection_length(interval1, interval2):
        start1, end1 = interval1
        start2, end2 = interval2
        return max(start1, start2) - min(start1, end2) + 1

    interval1, interval2 = map(tuple, zip(interval1, interval2))
    length = intersection_length(interval1, interval2)
    if length == 0:
        return "NO"
    elif is_prime(length):
        return "YES"
    else:
        return "NO"


# Test cases
print(intersection((1, 2), (2, 3))) # NO
print(intersection((-1, 1), (0, 4))) # NO
print(intersection((-3, -1), (-5, 5))) # YES
print(intersection((-1, 1), (-2, 3))) # NO
print(intersection((-1, 1), (-2, 3))) # NO
print(intersection((-1, 1), (-2, 3))) # NO
print(intersection((-1, 1), (-2, 3))) # NO
print(intersection((-1, 1), (-2, 3))) # NO
print(intersection((-1, 1), (-2, 3))) # NO
print(intersection((-1, 1), (-2, 3))) # NO
print(intersection((-1, 1), (-2, 3))) # NO
print(intersection((-1, 1), (-2, 3))) # NO
print(intersection((-1, 1), (-2, 3))) # NO
print(intersection((-1, 1), (-2, 3))) # NO
print(intersection((-1, 1), (-2, 3))) # NO
print(intersection((-1, 1), (-2, 3))) # NO
print(intersection((-1, 1), (-2, 3))) # NO
print(intersection((-1, 1), (-2, 3))) # NO
print(intersection((-1, 1), (-2, 3))) # NO
print(intersection((-1, 1), (-2, 3))) # NO
print(intersection((-1, 1), (-2, 3))) # NO
print(intersection((-1, 1), (-2, 3))) # NO
print(intersection((-1, 1), (-2, 3))) # NO
print(intersection((-1, 1), (-2, 3))) # NO
print(intersection((-1, 1), (-2, 3))) # NO
print(intersection((-1, 1), (-2, 3))) # NO
print(intersection((-1, 1), (-2, 3))) # NO
print(intersection((-1,