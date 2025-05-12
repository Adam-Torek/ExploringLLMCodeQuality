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
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    start1, end1 = interval1
    start2, end2 = interval2

    if start1 > end2 or start2 > end1:
        return "NO"

    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)

    if is_prime(intersection_end - intersection_start + 1):
        return "YES"
    else:
        return "NO"


# Test cases
print(intersection((1, 2), (2, 3)))  # "NO"
print(intersection((-1, 1), (0, 4)))  # "NO"
print(intersection((-3, -1), (-5, 5)))  # "YES"
print(intersection((1, 3), (2, 4)))  # "NO"
print(intersection((-1, 5), (2, 7)))  # "NO"
print(intersection((-1, 5), (4, 7)))  # "YES"
print(intersection((-1, 5), (5, 7)))  # "NO"
print(intersection((-1, 5), (-3, 7)))  # "YES"
print(intersection((-1, 5), (-3, 6)))  # "NO"
print(intersection((-1, 5), (-3, 5)))  # "YES"
print(intersection((-1, 5), (-3, 4)))  # "NO"
print(intersection((-1, 5), (1, 5))  # "YES"
print(intersection((-1, 5), (1, 6))  # "NO"
print(intersection((-1, 5), (-3, 6))  # "YES"
print(intersection((-1, 5), (-3, 7))  # "NO"
print(intersection((-1, 5), (-3, 5))  # "YES"
print(intersection((-1, 5), (-3, 4))  # "NO"
print(intersection((-1, 5), (1, 5))  # "YES"
print(intersection((-1, 5), (1, 6))  # "NO"
print(intersection((-1, 5), (-3, 6))  # "YES"
print(intersection((-1, 5), (-3, 7))  # "NO"
print(intersection((-1, 5), (-3, 5))  # "YES"
print(intersection((-1, 5), (-3, 4))  # "NO"

# Test cases with negative numbers
print(intersection((-1, 5), (-