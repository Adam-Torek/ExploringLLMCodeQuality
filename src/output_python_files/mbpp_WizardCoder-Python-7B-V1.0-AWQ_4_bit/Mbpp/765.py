"""
Write a function to find nth polite number. geeksforgeeks.org/n-th-polite-number/
assert is_polite(7) == 11
"""

def is_polite(n: int) -> int:
    def polite_numbers(n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return polite_numbers(n-1) + polite_numbers(n-2) + 1

    def polite_numbers_helper(n: int, memo: dict) -> int:
        if n in memo:
            return memo[n]
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            memo[n] = polite_numbers_helper(n-1, memo) + polite_numbers_helper(n-2, memo) + 1
            return memo[n]

    return polite_numbers_helper(n, {})


def nth_polite_number(n: int) -> int:
    return is_polite(n)


if __name__ == "__main__":
    print(nth_polite_number(7))
    print(nth_polite_number(10))
    print(nth_polite_number(100))
    print(nth_polite_number(1000))
    print(nth_polite_number(10000))
    print(nth_polite_number(100000))
    print(nth_polite_number(1000000))
    print(nth_polite_number(10000000))
    print(nth_polite_number(100000000))
    print(nth_polite_number(1000000000))
    print(nth_polite_number(10000000000))
    print(nth_polite_number(100000000000))
    print(nth_polite_number(1000000000000))
    print(nth_polite_number(10000000000000))
    print(nth_polite_number(100000000000000))
    print(nth_polite_number(1000000000000000))
    print(nth_polite_number(10000000000000000))
    print(nth_polite_number(100000000000000000))
    print(nth_polite_number(1000000000000000000))
    print(nth_polite_number(10000000000000000000))
    print(nth_polite_number(100000000000000000000))
    print(nth_polite_number(1000000000000000000000))
    print(nth_polite_number(10000000000000000000000))
    print(nth_polite_number(100000000000000000000000))
    print(nth_polite_number(1000000000000000000000000))
    print(nth_polite_number(10000000000000000000000000))
    print(nth_polite_number(10