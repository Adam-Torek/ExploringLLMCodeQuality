"""
Write a function to move all the numbers to the end of the given string.
assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
"""


def move_num(s):
    """
    :param s: string
    :return: string
    """
    nums = []
    for i in s:
        if i.isdigit():
            nums.append(i)
    return s.replace(''.join(nums), ''.join(sorted(nums, reverse=True)))


if __name__ == '__main__':
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three3000thousand'))
    print(move_num('I1love143you55three30