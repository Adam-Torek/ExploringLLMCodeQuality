"""
Write a function to divide two lists element wise.
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
"""

def div_list(list1, list2):
    """
    Divide two lists element wise.
    """
    if len(list1) != len(list2):
        raise ValueError("Lists must be of equal length")
    else:
        return [x/y for x,y in zip(list1, list2)]


if __name__ == "__main__":
    print(div_list([4,5,6],[1, 2, 3]))
    print(div_list([4,5,6],[1, 2, 3, 4]))
    print(div_list([4,5,6],[1, 2, 3, 4, 5]))
    print(div_list([4,5,6],[1, 2, 3, 4, 5, 6]))
    print(div_list([4,5,6],[1, 2, 3, 4, 5, 6, 7]))
    print(div_list([4,5,6],[1, 2, 3, 4, 5, 6, 7, 8]))
    print(div_list([4,5,6],[1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(div_list([4,5,6],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(div_list([4,5,6],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    print(div_list([4,5,6],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
    print(div_list([4,5,6],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    print(div_list([4,5,6],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
    print(div_list([4,5,6],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    print(div_list([4,5,6],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
    print(div_list([4,5,6],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))
    print(div_list([4,5,6],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))
    print(div_list([4,5,6],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))
    print(div_list([4,5,6],[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,