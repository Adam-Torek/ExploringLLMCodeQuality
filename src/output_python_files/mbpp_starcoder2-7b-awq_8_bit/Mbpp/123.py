"""
Write a function to sum all amicable numbers from 1 to a specified number.
assert amicable_numbers_sum(999)==504
"""

def amicable_numbers_sum(n):
    """
    >>> amicable_numbers_sum(999)
    504
    """
    return sum(amicable_numbers(n))

def amicable_numbers(n):
    """
    >>> amicable_numbers(999)
    [220, 284]
    """
    amicable_numbers = []
    for i in range(1, n):
        if is_amicable(i):
            amicable_numbers.append(i)
    return amicable_numbers

def is_amicable(n):
    """
    >>> is_amicable(220)
    True
    >>> is_amicable(284)
    True
    >>> is_amicable(100)
    False
    """
    return sum(factors(n)) == n and sum(factors(sum(factors(n)))) == n and n!= sum(factors(n))

def factors(n):
    """
    >>> factors(220)
    [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
    >>> factors(284)
    [1, 2, 4, 71, 142]
    """
    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)
    return factors

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/README.md
# amicable-numbers

Write a function to sum all amicable numbers from 1 to a specified number.

```
>>> amicable_numbers_sum(999)
504
```