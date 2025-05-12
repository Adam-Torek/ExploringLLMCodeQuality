"""
Write a python function to find the sum of non-repeated elements in a given list.
assert find_sum([1,2,3,1,1,4,5,6]) == 21
"""

def find_sum(lst):
    """
    >>> find_sum([1,2,3,1,1,4,5,6])
    21
    """
    return sum(set(lst))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/python_fundamentals/for_loop_basic1.py
"""
Write a function that prints all the integers from 0 to 150.
"""

def print_to_150():
    """
    >>> print_to_150()
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
/python/python_fundamentals/for_loop_basic2.py
"""
Write a function that prints all the multiples of 5 from 5 to 1,000,000.
"""

def print_multiples_of_5():
    """
    >>> print_multiples_of_5()
    1000000
    999995
    999990
    999985
    999980
    999975
    999970
    999965
    999960
    999955
    999950
    999945
    999940
    999935
    999930
    999925
    999920
    999915
    999910
    999905
    999900
    999895
    999890