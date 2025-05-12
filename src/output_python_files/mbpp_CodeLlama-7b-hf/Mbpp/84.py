"""
Write a function to find the nth number in the newman conway sequence.
assert sequence(10) == 6
"""


def sequence(n):
    """
    Write a function to find the nth number in the newman conway sequence.
    assert sequence(10) == 6
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return sequence(sequence(n-1)) + sequence(n-sequence(n-1))


def sequence_2(n):
    """
    Write a function to find the nth number in the newman conway sequence.
    assert sequence(10) == 6
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return sequence_2(sequence_2(n-1)) + sequence_2(n-sequence_2(n-1))


def sequence_3(n):
    """
    Write a function to find the nth number in the newman conway sequence.
    assert sequence(10) == 6
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return sequence_3(sequence_3(n-1)) + sequence_3(n-sequence_3(n-1))


def sequence_4(n):
    """
    Write a function to find the nth number in the newman conway sequence.
    assert sequence(10) == 6
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return sequence_4(sequence_4(n-1)) + sequence_4(n-sequence_4(n-1))


def sequence_5(n):
    """
    Write a function to find the nth number in the newman conway sequence.
    assert sequence(10) == 6
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return sequence_5(sequence_5(n-1)) + sequence_5(n-sequence_5(n-1))


def sequence_6(n):
    """
    Write a function to find the nth number in the newman conway sequence.
    assert sequence(10) == 6
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return sequence_6(sequence_6(n-1)) + sequence_6(n-sequence_6(n-1))


def sequence_7(n):
    """
    Write a function to find the nth number in the newman conway sequence.
    assert sequence(10) == 6
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return sequence_7(sequence_7(n-1)) + sequence_7(n-sequence_7(n-1))


def sequence_8(n):
    """
    Write a function to find the nth number in the newman conway sequence.
    assert sequence(10) == 6
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return sequence_8(sequence_8(n-1)) + sequence_8(n-sequence_8(n-1))


def sequence_9(n):
    """
    Write a function to find the nth number in the newman conway sequence.
    assert sequence(10) == 6
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return sequence_9(sequence_9(n-1)) + sequence_9(n-sequence_9(n-1))


def sequence_10(n):
    """