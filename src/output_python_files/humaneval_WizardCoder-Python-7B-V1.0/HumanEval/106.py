def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(sum(range(1, i+1)))
    return result


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(f(5))

# Output: [1, 2, 6, 24, 15]

# Explanation:
# The factorial of 2 is 2 * 1 = 2, the factorial of 4 is 4 * 3 * 2 * 1 = 24, the factorial of 6 is 6 * 5 * 4 * 3 * 2 * 1 = 120, and so on.
# The sum of numbers from 1 to 3 is 1 + 2 + 3 = 6, the sum of numbers from 1 to 5 is 1 + 2 + 3 + 4 + 5 = 15.
# Therefore, the function returns [1, 2, 24, 15] for n = 5.