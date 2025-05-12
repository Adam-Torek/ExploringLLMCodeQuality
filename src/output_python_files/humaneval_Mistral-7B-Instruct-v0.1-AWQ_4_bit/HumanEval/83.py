def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # count the number of integers that start with 1
    start_count = 0
    for i in range(1, n):
        start_count += 10**i

    # count the number of integers that end with 1
    end_count = 0
    for i in range(1, n):
        end_count += 10**i

    return start_count + end_count - 10**n


if __name__ == "__main__":
    n = int(input())
    print(starts_one_ends(n))