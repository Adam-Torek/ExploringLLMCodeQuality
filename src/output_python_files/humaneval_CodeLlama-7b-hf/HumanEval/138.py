def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Your code here
    if n % 2 == 1:
        return False
    else:
        for i in range(1, n//2 + 1):
            if n - i * 2 in range(1, n//2 + 1):
                return True
        return False


def is_equal_to_sum_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive odd numbers
    Example
    is_equal_to_sum_odd(5) == False
    is_equal_to_sum_odd(7) == False
    is_equal_to_sum_odd(9) == True
    """
    # Your code here
    if n % 2 == 0:
        return False
    else:
        for i in range(1, n//2 + 1):
            if n - i * 2 in range(1, n//2 + 1):
                return True
        return False


def is_equal_to_sum_two_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive even numbers
    Example
    is_equal_to_sum_two_even(4) == False
    is_equal_to_sum_two_even(6) == True
    is_equal_to_sum_two_even(8) == False
    """
    # Your code here
    if n % 2 == 1:
        return False
    else:
        for i in range(1, n//2 + 1):
            if n - i * 2 in range(1, n//2 + 1):
                return True
        return False


def is_equal_to_sum_two_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 2 positive odd numbers
    Example
    is_equal_to_sum_two_odd(5) == False
    is_equal_to_sum_two_odd(7) == True
    is_equal_to_sum_two_odd(9) == False
    """
    # Your code here
    if n % 2 == 0:
        return False
    else:
        for i in range(1, n//2 + 1):
            if n - i * 2 in range(1, n//2 + 1):
                return True
        return False


def is_equal_to_sum_three_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive even numbers
    Example
    is_equal_to_sum_three_even(4) == False
    is_equal_to_sum_three_even(6) == True
    is_equal_to_sum_three_even(8) == False
    """
    # Your code here
    if n % 2 == 1:
        return False
    else:
        for i in range(1, n//2 + 1):
            if n - i * 2 in range(1, n//2 + 1):
                return True
        return False


def is_equal_to_sum_three_odd(n):
    """Evaluate whether the given number n can be written as the sum of exactly 3 positive odd numbers
    Example
    is_equal_to_sum_three_odd(5) == False
    is_equal_to_sum_three_odd(7) == False
    is_equal_to_sum_three_odd(9) == True
    """
    # Your code here
    if n %