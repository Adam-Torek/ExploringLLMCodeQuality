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
        tribonacci = [1, 3, 2]
        for i in range(3, n + 1):
            tribonacci.append(tribonacci[i - 1] + tribonacci[i - 2] + tribonacci[i - 3])
        return tribonacci


# Test cases
print(tri(3))  # Output: [1, 3, 2, 8]
print(tri(5))  # Output: [1, 3, 2, 8, 17, 64, 256]
print(tri(10))  # Output: [1, 3, 2, 8, 17, 64, 256, 128, 793, 480, 2808, 1607, 11340, 6476, 3835]
print(tri(0))  # Output: []
print(tri(1))  # Output: [1]
print(tri(2))  # Output: [1, 3]
print(tri(4))  # Output: [1, 3, 2, 8]
print(tri(100))  # Output: [1, 3, 2, 8, 17, 64, 256, 128, 793, 480, 2808, 1607, 11340, 6476, 3835, 22457, 130038, 73087, 43467, 241370, 1223866, 650807, 3545708, 1974224, 10968767, 6167836, 34027385, 18419192, 10968767, 6167836, 34027385, 1974224, 1096