def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 3]
    elif n == 3:
        return [1, 3, 2]
    else:
        t = [1, 3, 2]
        for i in range(3, n + 1):
            if i % 2 == 0:
                t.append(t[i - 1] + t[i - 2] + t[i - 3])
            else:
                t.append(t[i - 1] + t[i - 2] + t[i - 3] + t[i - 4])
        return t


# Test cases
print(tri(0))  # []
print(tri(1))  # [1]
print(tri(2))  # [1, 3]
print(tri(3))  # [1, 3, 2]
print(tri(4))  # [1, 3, 2, 8]
print(tri(5))  # [1, 3, 2, 8, 17, 12]
print(tri(6))  # [1, 3, 2, 8, 17, 12, 42, 25]
print(tri(7))  # [1, 3, 2, 8, 17, 12, 42, 25, 73, 34]
print(tri(8))  # [1, 3, 2, 8, 17, 12, 42, 25, 73, 34, 128, 105]
print(tri(9))  # [1, 3, 2, 8, 17, 12, 42, 25, 73, 34, 128, 105, 204, 179]
print(tri(10))  # [1, 3, 2, 8, 17, 12, 42, 25, 73, 34, 128, 105, 204, 179, 403, 267]
print(tri(11))  # [1, 3, 2, 8, 1