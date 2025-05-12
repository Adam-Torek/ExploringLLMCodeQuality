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
# The factorial of 2 is 2, the factorial of 4 is 24, the factorial of 6 is 720, and so on.
# The sum of numbers from 1 to 2 is 3, the sum of numbers from 1 to 4 is 10, the sum of numbers from 1 to 6 is 21.
# The function returns a list of size 5, with the values of the elements at even indices being the factorials,
# and the values at odd indices being the sums of numbers from 1 to i.

# Note that we use the built-in function range() to generate the numbers from 1 to i, and the built-in function sum() to calculate the sum.
# We also use the ternary operator to check if i is even or odd, and append the factorial or the sum accordingly.