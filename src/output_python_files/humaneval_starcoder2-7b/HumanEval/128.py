def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """

def is_prime(n):
    """
    You are given a number n.
    Return True if n is prime, False otherwise.
    Note: return None for non-positive numbers.

    Example:
    >>> is_prime(1) == None
    >>> is_prime(2) == True
    >>> is_prime(3) == True
    >>> is_prime(4) == False
    >>> is_prime(5) == True
    >>> is_prime(6) == False
    >>> is_prime(7) == True
    >>> is_prime(8) == False
    >>> is_prime(9) == False
    >>> is_prime(10) == False
    >>> is_prime(11) == True
    >>> is_prime(12) == False
    >>> is_prime(13) == True
    >>> is_prime(14) == False
    >>> is_prime(15) == False
    >>> is_prime(16) == False
    >>> is_prime(17) == True
    >>> is_prime(18) == False
    >>> is_prime(19) == True
    >>> is_prime(20) == False
    >>> is_prime(21) == False
    >>> is_prime(22) == False
    >>> is_prime(23) == True
    >>> is_prime(24) == False
    >>> is_prime(25) == False
    >>> is_prime(26) == False
    >>> is_prime(27) == False
    >>> is_prime(28) == False
    >>> is_prime(29) == True
    >>> is_prime(30) == False
    >>> is_prime(31) == True
    >>> is_prime(32) == False
    >>> is_prime(33) == False
    >>> is_prime(34) == False
    >>> is_prime(35) == False
    >>> is_prime(36) == False
    >>> is_prime(37) == True
    >>> is_prime(38) == False
    >>> is_prime(39) == False
    >>> is_prime(40) == False
    >>> is_prime(41) == True
    >>> is_prime(42) == False
    >>> is_prime(43) == True
    >>> is_prime(44) == False
    >>> is_prime(45) == False
    >>> is_prime(46) == False
    >>> is_prime(47) == True
    >>> is_prime(48) == False
    >>> is_prime(49) == False
    >>> is_prime(50) == False
    >>> is_prime(51) == False
    >>> is_prime(52) == False
    >>> is_prime(53) == True
    >>> is_prime(54) ==