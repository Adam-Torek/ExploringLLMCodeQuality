def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    if len(l) < 3:
        return False
    l.sort()
    for i in range(len(l) - 2):
        for j in range(i + 1, len(l) - 1):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False


def main():
    """
    main function
    """
    l = [1, 3, 5, 0]
    print(triples_sum_to_zero(l))

    l = [1, 3, -2, 1]
    print(triples_sum_to_zero(l))

    l = [1, 2, 3, 7]
    print(triples_sum_to_zero(l))

    l = [2, 4, -5, 3, 9, 7]
    print(triples_sum_to_zero(l))

    l = [1]
    print(triples_sum_to_zero(l))


if __name__ == "__main__":
    main()