"""
Write a function to extract the elementwise and tuples from the given two tuples.
assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
"""

def and_tuples(tuple1, tuple2):
    """
    Extract the elementwise and tuples from the given two tuples.
    """
    and_list = []
    tuples_list = []
    for i in range(len(tuple1)):
        if tuple1[i] == tuple2[i]:
            and_list.append(tuple1[i])
        else:
            tuples_list.append(tuple1[i])
    return and_list, tuples_list


if __name__ == "__main__":
    and_tuples((10, 4, 6, 9), (5, 2, 3, 3))