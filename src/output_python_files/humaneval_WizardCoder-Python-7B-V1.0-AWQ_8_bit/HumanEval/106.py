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

# Output: [1, 2, 6, 24, 15, 120]

# Explanation:
# The factorial of 1 is 1, the factorial of 2 is 2, the factorial of 3 is 6, the factorial of 4 is 24, and the factorial of 5 is 120.
# The sum of numbers from 1 to 5 is 15.
# The function f returns a list of size 5, where the value at index i is the factorial of i if i is even, and the sum of numbers from 1 to i if i is odd.
# The first element is 1, the second element is 2, the third element is 6, the fourth element is 24, and the fifth element is 15.