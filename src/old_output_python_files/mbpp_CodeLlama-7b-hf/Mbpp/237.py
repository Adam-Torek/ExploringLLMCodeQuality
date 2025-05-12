"""
Write a function that takes in a list of tuples and returns a dictionary mapping each unique tuple to the number of times it occurs in the list.
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] ) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
"""


def check_occurences(list_of_tuples):
    """
    :param list_of_tuples: list of tuples
    :return: dictionary mapping each unique tuple to the number of times it occurs in the list
    """
    dict_of_tuples = {}
    for tuple in list_of_tuples:
        if tuple in dict_of_tuples:
            dict_of_tuples[tuple] += 1
        else:
            dict_of_tuples[tuple] = 1
    return dict_of_tuples


if __name__ == '__main__':
    print(check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]))
    print(check_occurences([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12),
                            (12, 13), (13, 14), (14, 15), (15, 16), (16, 17), (17, 18), (18, 19), (19, 20), (20, 21),
                            (21, 22), (22, 23), (23, 24), (24, 25), (25, 26), (26, 27), (27, 28), (28, 29), (29, 30),
                            (30, 31), (31, 32), (32, 33), (33, 34), (34, 35), (35, 36), (36, 37), (37, 38), (38, 39),
                            (39, 40), (40, 41), (41, 42), (42, 43), (43, 44), (44, 45), (45, 46), (46, 47), (47, 48),
                            (48, 49), (49, 50), (50, 51), (51, 52), (52, 53), (53, 54), (54, 55), (55, 56), (56, 57),
                            (57, 58), (58, 59), (59, 60), (60, 61), (61, 62), (62, 63), (63, 64), (64, 65), (65, 66),
                            (66, 67), (67, 68), (68, 69), (69, 70), (70, 71), (71, 72), (72, 73), (73, 74), (74, 75),
                            (75, 76), (76, 77), (77, 78), (78, 79), (79, 80), (80, 81), (81, 82), (82, 83), (83, 84),
                            (84, 85), (85, 86), (86, 87), (87, 88), (88, 89), (89, 90), (