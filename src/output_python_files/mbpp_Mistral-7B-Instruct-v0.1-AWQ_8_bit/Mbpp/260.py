"""
Write a function to find the nth newman–shanks–williams prime number.
assert newman_prime(3) == 7
"""

def newman_prime(n):
    """
    :param n: int
    :return: int
    """
    if n < 1:
        return 0
    if n == 1:
        return 2
    if n == 2:
        return 3
    if n % 2 == 0:
        return 0
    if n % 3 == 0:
        return 3
    if n % 5 == 0:
        return 5
    if n % 7 == 0:
        return 7
    if n % 11 == 0:
        return 11
    if n % 13 == 0:
        return 13
    if n % 17 == 0:
        return 17
    if n % 19 == 0:
        return 19
    if n % 23 == 0:
        return 23
    if n % 29 == 0:
        return 29
    if n % 31 == 0:
        return 31
    if n % 37 == 0:
        return 37
    if n % 41 == 0:
        return 41
    if n % 43 == 0:
        return 43
    if n % 47 == 0:
        return 47
    if n % 53 == 0:
        return 53
    if n % 59 == 0:
        return 59
    if n % 61 == 0:
        return 61
    if n % 67 == 0:
        return 67
    if n % 71 == 0:
        return 71
    if n % 73 == 0:
        return 73
    if n % 79 == 0:
        return 79
    if n % 83 == 0:
        return 83
    if n % 89 == 0:
        return 89
    if n % 97 == 0:
        return 97
    if n % 101 == 0:
        return 101
    if n % 103 == 0:
        return 103
    if n % 107 == 0:
        return 107
    if n % 109 == 0:
        return 109
    if n % 113 == 0:
        return 113
    if n % 127 == 0:
        return 127
    if n % 131 == 0:
        return 131
    if n % 137 == 0:
        return 137
    if n % 139 == 0:
        return 139
    if n % 149 == 0:
        return 149
    if n % 151 == 0:
        return 151
    if n % 157 == 0:
        return 157
    if n % 163 == 0:
        return 163
    if n % 167 == 0:
        return 167
    if n % 173 == 0:
        return 173
    if n % 179 == 0:
        return 179
    if n % 181 == 0:
        return 181
    if n % 191 == 0:
        return 191
    if n % 193 == 0:
        return 193
    if n % 197 == 0:
        return 197
    if n % 199 == 0:
        return 199
    if n % 211 == 0:
        return 211
    if n % 223 == 0:
        return 223
    if n % 227 == 0:
        return