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
    # your code here
    if interval1[1] < interval2[0]:
        return "NO"
    elif interval1[1] <= interval2[1]:
        return "YES" if is_prime(interval1[1] - interval1[0] + 1) else "NO"
    else:
        return "NO"

def is_prime(n):
    """You are given a number n.
    Your task is to determine whether n is a prime number.
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    For example, 1 is not a prime number, 2 is a prime number, 3 is a prime number, 4 is not a prime number,
    and 5 is a prime number.

    [input/output] samples:
    is_prime(1) ==> False
    is_prime(2) ==> True
    is_prime(3) ==> True
    is_prime(4) ==> False
    is_prime(5) ==> True
    """
    # your code here
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# test your code here
print(intersection((1, 2), (2, 3)))
print(intersection((-1, 1), (0, 4)))
print(intersection((-3, -1), (-5, 5)))
print(intersection((1, 3), (2, 4)))
print(intersection((1, 3), (3, 4)))
print(intersection((1, 3), (3, 5)))
print(intersection((1, 3), (3, 6)))
print(intersection((1, 3), (3, 7)))
print(intersection((1, 3), (3, 8)))
print(intersection((1, 3), (3, 9)))
print(intersection((1, 3), (3, 10)))
print(intersection((1, 3), (3, 11)))
print(intersection((1, 3), (3, 12)))
print(intersection((1, 3), (3, 13)))
print(intersection((1, 3), (3, 14)))
print(intersection((1, 3), (3, 15)))
print(intersection((1, 3), (3, 16)))
print(intersection((1, 3), (3, 17)))
print(intersection((1, 3), (3, 18)))
print(intersection((1, 3), (3, 19)))
print(intersection((1, 3), (3, 20)))
print(intersection((1, 3), (3, 21