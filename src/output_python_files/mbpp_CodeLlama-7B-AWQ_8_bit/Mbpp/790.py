"""
Write a python function to check whether every even index contains even numbers of a given list.
assert even_position([3,2,1]) == False
"""

def even_position(lst):
    for i in range(0, len(lst), 2):
        if lst[i] % 2 != 0:
            return False
    return True


def even_position_2(lst):
    return all(lst[i] % 2 == 0 for i in range(0, len(lst), 2))


def even_position_3(lst):
    return all(lst[i] % 2 == 0 for i in range(0, len(lst), 2) if i % 2 == 0)


def even_position_4(lst):
    return all(lst[i] % 2 == 0 for i in range(0, len(lst), 2) if i % 2 == 0)


def even_position_5(lst):
    return all(lst[i] % 2 == 0 for i in range(0, len(lst), 2) if i % 2 == 0)


def even_position_6(lst):
    return all(lst[i] % 2 == 0 for i in range(0, len(lst), 2) if i % 2 == 0)


def even_position_7(lst):
    return all(lst[i] % 2 == 0 for i in range(0, len(lst), 2) if i % 2 == 0)


def even_position_8(lst):
    return all(lst[i] % 2 == 0 for i in range(0, len(lst), 2) if i % 2 == 0)


def even_position_9(lst):
    return all(lst[i] % 2 == 0 for i in range(0, len(lst), 2) if i % 2 == 0)


def even_position_10(lst):
    return all(lst[i] % 2 == 0 for i in range(0, len(lst), 2) if i % 2 == 0)


def even_position_11(lst):
    return all(lst[i] % 2 == 0 for i in range(0, len(lst), 2) if i % 2 == 0)


def even_position_12(lst):
    return all(lst[i] % 2 == 0 for i in range(0, len(lst), 2) if i % 2 == 0)


def even_position_13(lst):
    return all(lst[i] % 2 == 0 for i in range(0, len(lst), 2) if i % 2 == 0)


def even_position_14(lst):
    return all(lst[i] % 2 == 0 for i in range(0, len(lst), 2) if i % 2 == 0)


def even_position_15(lst):
    return all(lst[i] % 2 == 0 for i in range(0, len(lst), 2) if i % 2 == 0)


def even_position_16(lst):
    return all(lst[i] % 2 == 0 for i in range(0, len(lst), 2) if i % 2 == 0)


def even_position_17(lst):
    return all(lst[i] % 2 == 0 for i in range(0, len(lst), 2) if i % 2 == 0)


def even_position_18(lst):
    return all(lst[i] % 2 == 0 for i in range(0, len(lst), 2) if i % 2 == 0)


def even_position_19(lst):
    return all(lst[i] % 2 == 0 for i in range(0, len(lst), 2) if i % 2 == 0)


def even_position_20(lst):
    return all(lst[i] % 2 == 0 for i in range(0, len(lst