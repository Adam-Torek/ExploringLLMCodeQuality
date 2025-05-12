"""
Write a function to get all lucid numbers smaller than or equal to a given integer.
assert get_ludic(10) == [1, 2, 3, 5, 7]
"""
def get_lucid(n):
    """
    :param n: an integer
    :return: a list of all lucid numbers smaller than or equal to n
    """
    lucids = [1]
    for i in range(2, n+1):
        is_lucid = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                is_lucid = False
                break
        if is_lucid:
            lucids.append(i)
    return lucids

if __name__ == "__main__":
    assert get_lucid(10) == [1, 2, 3, 5, 7]
    print(get_lucid(20))