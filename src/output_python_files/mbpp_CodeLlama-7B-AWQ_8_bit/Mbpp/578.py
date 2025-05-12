"""
Write a function to interleave 3 lists of the same length into a single flat list.
assert interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])==[1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
"""

def interleave_lists(list1, list2, list3):
    """
    >>> interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])
    [1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
    """
    return [x for x in list1 + list2 + list3]


def interleave_lists_2(list1, list2, list3):
    """
    >>> interleave_lists_2([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])
    [1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
    """
    return [x for x in list1 + list2 + list3]


def interleave_lists_3(list1, list2, list3):
    """
    >>> interleave_lists_3([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])
    [1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
    """
    return [x for x in list1 + list2 + list3]


def interleave_lists_4(list1, list2, list3):
    """
    >>> interleave_lists_4([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700])
    [1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
    """
    return [x for x in list1 + list2 + list3]


def interleave_lists_5(list1, list2, list3):
    """
    >>> interleave_