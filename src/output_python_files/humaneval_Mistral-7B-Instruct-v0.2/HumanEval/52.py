def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for num in l:
        if num > t:
            return False
    return True

# below_threshold([1, 2, 4, 10], 100)
# below_threshold([1, 20, 4, 10], 5)
# below_threshold([1, 2, 4, 10], 11)
# below_threshold([], 10)
# below_threshold([], 5)
# below_threshold([], 0)
# below_threshold([], -1)
# below_threshold([], 1000000000000)
# below_threshold([], float('inf'))
# below_threshold([], -float('inf'))
# below_threshold([], complex(0, 0))
# below_threshold([], complex(0, 1))
# below_threshold([], complex(1, 0))
# below_threshold([], complex(1, 1))
# below_threshold([], complex(1, -1))
# below_threshold([], complex(-1, 0))
# below_threshold([], complex(-1, 1))
# below_threshold([], complex(-1, -1))
# below_threshold([], set())
# below_threshold([], frozenset())
# below_threshold([], tuple())
# below_threshold([], dict())
# below_threshold([], list())
# below_threshold([], bytearray())
# below_threshold([], memoryview())
# below_threshold([], range(10))
# below_threshold([], xrange(10))
# below_threshold([], enumerate(['a', 'b', 'c']))
# below_threshold([], filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
# below_threshold([], map(lambda x: x * 2, [1, 2, 3, 4, 5]))
# below_threshold([], [1, 2, 3, 4, 5][::-1])
# below_threshold([], [1, 2, 3, 4, 5][:3])
# below_threshold([], [1, 2, 3, 4, 5][:3] + [6, 7, 8])
# below_threshold([], [1, 2, 3, 4, 5][:3] + list(range(10, 20)))
# below_threshold([], [1, 2, 3, 4, 5][:3] + [*range(10, 20)])
# below_threshold([], [1, 2, 3, 4, 5][:3] + [*range(10, 20)] * 2)
# below_threshold([], [1, 2, 3, 4, 5][:3] + [*range(10, 20)] * 3)
# below_threshold([], [1, 2, 3, 4, 5][:3] + [*range(10, 20)] * 4)
# below_threshold([], [1, 2, 3, 4, 5][:3] + [*range(10, 20)] * 5)
# below_threshold([], [1, 2, 3, 4, 5][:3] + [*range(10, 20)] * 6)
# below_threshold([], [1, 2, 3, 4,