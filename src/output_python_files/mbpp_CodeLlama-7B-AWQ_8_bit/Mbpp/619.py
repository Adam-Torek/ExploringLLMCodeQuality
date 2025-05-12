"""
Write a function to move all the numbers to the end of the given string.
assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
"""


def move_num(string):
    """
    :param string: str
    :return: str
    """
    nums = []
    for char in string:
        if char.isdigit():
            nums.append(char)
    return string.replace(''.join(nums), ''.join(sorted(nums, reverse=True)))


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