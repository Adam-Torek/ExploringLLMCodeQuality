"""
Write a function to interleave 3 lists of the same length into a single flat list.
assert interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])==[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
"""


def interleave_lists(list1, list2, list3):
    """
    :param list1: list of ints
    :param list2: list of ints
    :param list3: list of ints
    :return: list of ints
    """
    if len(list1) != len(list2) or len(list1) != len(list3):
        raise ValueError("Lists must be of equal length")
    else:
        interleaved_list = []
        for i in range(len(list1)):
            interleaved_list.append(list1[i])
            interleaved_list.append(list2[i])
            interleaved_list.append(list3[i])
        return interleaved_list


if __name__ == '__main__':
    print(interleave_lists([1, 2, 3, 4, 5, 6, 7], [10, 20, 30, 40, 50, 60, 70], [100, 200, 300, 400, 500, 600, 700]))
    print(interleave_lists([1, 2, 3, 4, 5, 6, 7], [10, 20, 30, 40, 50, 60, 70], [100, 200, 300, 400, 500, 600, 700]))
    print(interleave_lists([1, 2, 3, 4, 5, 6, 7], [10, 20, 30, 40, 50, 60, 70], [100, 200, 300, 400, 500, 600, 700]))
    print(interleave_lists([1, 2, 3, 4, 5, 6, 7], [10, 20, 30, 40, 50, 60, 70], [100, 200, 300, 400, 500, 600, 700]))
    print(interleave_lists([1, 2, 3, 4, 5, 6, 7], [10, 20, 30, 40, 50, 60, 70], [100, 200, 300, 400, 500, 600, 700]))
    print(interleave_lists([1, 2, 3, 4, 5, 6, 7], [10, 20, 30, 40, 50, 60, 70], [100, 200, 300, 400, 500, 600, 700]))
    print(interleave_lists([1, 2, 3, 4, 5, 6, 7], [10, 20, 30, 40, 50, 60, 70], [100, 200, 300, 400, 500, 60