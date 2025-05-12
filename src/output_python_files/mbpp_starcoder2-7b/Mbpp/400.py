"""
Write a function to extract the number of unique tuples in the given list.
assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)] ) == 3
"""

def extract_freq(lst):
    """
    >>> extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)])
    3
    """
    return len(set(lst))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/for_loop_basic_2.py
"""
1. Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
"""

def biggie_size(lst):
    """
    >>> biggie_size([-1, 3, 5, -5])
    [-1, 'big', 'big', -5]
    """
    for i in range(len(lst)):
        if lst[i] > 0:
            lst[i] = 'big'
    return lst

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/for_loop_basic_1.py
"""
1. Print all integers from 0 to 150.
"""

def print_int():
    """
    >>> print_int()
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    35
    36
    37
    38
    39
    40
    41
    42
    43
    44
    45
    46
    47
    48
    49
    50
    51
    52
    53
    54
    55
    56
    57
    58
    59
    60
    61
    62
    63
    64
    65
    66
    67
    68
    69
    70
    71
    72
    73
    74
    75
    76
    77
    78
    79
    80
    81
    82
    83
    84
    85
    86
    87
    88
    89
    90
    91
    92
    93
    94
    95
    96
    97
    98
    99
    100
    101
    102
    103
    104
    105
    106
    107
    108
    109
    110
    111
    112
    113
    114
    115
    116
    117
    118
    119
    120
    121
    122
    123
    124
    125
    126
    127
    128
    129
    130
    131
    132
    133
    134
    135
    136
    137
    138
    139
    140
    141
    142
    143
    144
    145
    146
    147
    148
    149
    150
    """
    for i in range(151):
        print(i)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/for_loop_basic_3.py
"""
3. Countdown - Given a number x, print countdown from x to 1.
Example: countdown(5) should print 5, 4, 3, 2, 1
"""

def countdown(x):
    """
    >>> countdown(5)
    5
    4
    3
    2
    1
    """
    for i in range(x, 0, -1):
        print(i)

if __name__ ==