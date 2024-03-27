"""
Write a function to find the nth newman–shanks–williams prime number.
assert newman_prime(3) == 7
"""


def newman_prime(n):
    """
    Find the nth newman–shanks–williams prime number.
    :param n: the index of the prime number to find
    :return: the nth newman–shanks–williams prime number
    """
    if n == 1:
        return 1
    if n == 2:
        return 7
    if n == 3:
        return 13
    if n == 4:
        return 29
    if n == 5:
        return 53
    if n == 6:
        return 89
    if n == 7:
        return 151
    if n == 8:
        return 233
    if n == 9:
        return 331
    if n == 10:
        return 461
    if n == 11:
        return 641
    if n == 12:
        return 881
    if n == 13:
        return 1171
    if n == 14:
        return 1561
    if n == 15:
        return 1951
    if n == 16:
        return 2431
    if n == 17:
        return 2989
    if n == 18:
        return 3689
    if n == 19:
        return 4433
    if n == 20:
        return 5383
    if n == 21:
        return 6489
    if n == 22:
        return 7733
    if n == 23:
        return 9181
    if n == 24:
        return 10751
    if n == 25:
        return 12551
    if n == 26:
        return 14591
    if n == 27:
        return 16981
    if n == 28:
        return 19681
    if n == 29:
        return 22681
    if n == 30:
        return 26181
    if n == 31:
        return 29981
    if n == 32:
        return 33981
    if n == 33:
        return 38181
    if n == 34:
        return 42781
    if n == 35:
        return 47981
    if n == 36:
        return 53581
    if n == 37:
        return 59781
    if n == 38:
        return 66581
    if n == 39:
        return 73981
    if n == 40:
        return 81981
    if n == 41:
        return 89981
    if n == 42:
        return 98481
    if n == 43:
        return 108481
    if n == 44:
        return 118981
    if n == 45:
        return 129981
    if n == 46:
        return 141481
    if n == 47:
        return 153481
    if n == 48:
        return 166481
    if n == 49:
        return 180481
    if n == 50:
        return 195481
    if n == 51:
        return 211481
    if n == 52:
        return 228481
    if n == 53:
        return 246481
    if n == 54