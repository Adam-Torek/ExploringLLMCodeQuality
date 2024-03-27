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
    # your code here
    l.sort()
    for i in range(len(l)):
        if l[i] == 0:
            return True
        if i > 0 and l[i] == l[i - 1]:
            continue
        left = 0
        right = len(l) - 1
        while left < right:
            if l[left] + l[right] == -l[i]:
                return True
            elif l[left] + l[right] < -l[i]:
                left += 1
            else:
                right -= 1
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
</s>