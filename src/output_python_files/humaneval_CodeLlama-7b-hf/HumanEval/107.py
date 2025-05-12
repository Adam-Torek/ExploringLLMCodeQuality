def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """
    # Edge case
    if n <= 1:
        return 0, 0

    # Count even and odd palindrome
    even_count = 0
    odd_count = 0
    for i in range(1, n + 1):
        if is_palindrome(i):
            if is_even(i):
                even_count += 1
            else:
                odd_count += 1

    return even_count, odd_count


def is_even(n):
    """
    Check if a number is even.
    """
    return n % 2 == 0


def is_palindrome(n):
    """
    Check if a number is a palindrome.
    """
    # Edge case
    if n < 0:
        return False

    # Convert number to string
    n_str = str(n)

    # Check if the string is a palindrome
    for i in range(len(n_str) // 2):
        if n_str[i] != n_str[-i - 1]:
            return False

    return True


if __name__ == '__main__':
    print(even_odd_palindrome(3))
    print(even_odd_palindrome(12))
    print(even_odd_palindrome(100))
    print(even_odd_palindrome(1000))
    print(even_odd_palindrome(10000))
    print(even_odd_palindrome(100000))
    print(even_odd_palindrome(1000000))
    print(even_odd_palindrome(10000000))
    print(even_odd_palindrome(100000000))
    print(even_odd_palindrome(1000000000))
    print(even_odd_palindrome(10000000000))
    print(even_odd_palindrome(100000000000))
    print(even_odd_palindrome(1000000000000))
    print(even_odd_palindrome(10000000000000))
    print(even_odd_palindrome(100000000000000))
    print(even_odd_palindrome(1000000000000000))
    print(even_odd_palindrome(10000000000000000))
    print(even_odd_palindrome(100000000000000000))
    print(even_odd_palindrome(100000000000000