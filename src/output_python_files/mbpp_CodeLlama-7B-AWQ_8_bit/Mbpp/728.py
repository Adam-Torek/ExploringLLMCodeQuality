"""
Write a function takes as input two lists [a_1,...,a_n], [b_1,...,b_n] and returns [a_1+b_1,...,a_n+b_n].
assert sum_list([10,20,30],[15,25,35])==[25,45,65]
"""


def sum_list(list1, list2):
    """
    :param list1: list of integers
    :param list2: list of integers
    :return: list of integers
    """
    return [list1[i] + list2[i] for i in range(len(list1))]


if __name__ == '__main__':
    print(sum_list([10, 20, 30], [15, 25, 35]))
    print(sum_list([10, 20, 30], [15, 25, 35, 45]))
    print(sum_list([10, 20, 30], [15, 25, 35, 45, 55]))
    print(sum_list([10, 20, 30], [15, 25, 35, 45, 55, 65]))
    print(sum_list([10, 20, 30], [15, 25, 35, 45, 55, 65, 75]))
    print(sum_list([10, 20, 30], [15, 25, 35, 45, 55, 65, 75, 85]))
    print(sum_list([10, 20, 30], [15, 25, 35, 45, 55, 65, 75, 85, 95]))
    print(sum_list([10, 20, 30], [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]))
    print(sum_list([10, 20, 30], [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115]))
    print(sum_list([10, 20, 30], [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125]))
    print(sum_list([10, 20, 30], [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135]))
    print(sum_list([10, 20, 30], [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145]))
    print(sum_list([10, 20, 30], [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155]))
    print(sum_list([10, 20, 30], [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165]))
    print(sum_list([10, 20, 30], [15, 25