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
    # 1 <= n <= 10^3
    # returned tuple has the number of even and odd integer palindromes respectively.

    # Solution:
    # --------------------------------------------------------------------------------------------------------------
    # 1. Create a list of all the palindromes in the range(1, n).
    # 2. Count the number of even and odd palindromes in the list.
    # 3. Return the tuple.
    # --------------------------------------------------------------------------------------------------------------
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    # Create a list of all the palindromes in the range(1, n).
    palindromes = []
    for i in range(1, n + 1):
        if is_palindrome(i):
            palindromes.append(i)

    # Count the number of even and odd palindromes in the list.
    even_count = 0
    odd_count = 0
    for i in palindromes:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    # Return the tuple.
    return (even_count, odd_count)


def is_palindrome(n):
    """
    Given a positive integer n, return True if n is a palindrome, otherwise return False.

    Example 1:

        Input: 121
        Output: True

    Example 2:

        Input: -121
        Output: False
        Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a
        palindrome.

    Example 3:

        Input: 10
        Output: False
        Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

    Note:
        1. -2^31 <= n <= 2^31 - 1
    """
    # -2^31 <= n <= 2^31 - 1

    # Solution:
    # --------------------------------------------------------------------------------------------------------------
    # 1. Convert the number to a string.
    # 2. Check if the string is a palindrome.
    # --------------------------------------------------------------------------------------------------------------
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    # Convert the number to a string.
    n = str(n)

    # Check if the string is a palindrome.
    for i in range(len(n) // 2):
        if n[i] != n[len(n) - 1 - i]:
            return False

    return True


def main():
    print(even_odd_palindrome(3))
    print(even_odd_palindrome(12))


if __name__ == '__main__':
    main()
</s>