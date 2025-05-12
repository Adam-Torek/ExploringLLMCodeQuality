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
    for i in range(n):
        if i % 2 == 0:
            result.append(fact(i))
        else:
            result.append(sum(range(1, i+1)))
    return result

def fact(n):
    """ Implement the function fact that takes n as a parameter,
    and returns the factorial of n.
    Example:
    fact(5) == 120
    """
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

if __name__ == "__main__":
    n = int(input())
    print(f(n))