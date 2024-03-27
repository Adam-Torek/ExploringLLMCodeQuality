def get_row(lst, x):
    """
    You are given a 2 dimensional data, as a nested lists,
    which is similar to matrix, however, unlike matrices,
    each row may contain a different number of columns.
    Given lst, and integer x, find integers x in the list,
    and return list of tuples, [(x1, y1), (x2, y2) ...] such that
    each tuple is a coordinate - (row, columns), starting with 0.
    Sort coordinates initially by rows in ascending order.
    Also, sort coordinates of the row by columns in descending order.
    
    Examples:
    get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    get_row([], 1) == []
    get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    """
    # your code here
    result = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                result.append((i, j))
    result.sort(key=lambda x: x[0])
    for i in range(len(result)):
        result[i] = (result[i][0], len(lst[result[i][0]]) - result[i][1] - 1)
    result.sort(key=lambda x: x[1])
    return result


def get_column(lst, x):
    """
    You are given a 2 dimensional data, as a nested lists,
    which is similar to matrix, however, unlike matrices,
    each row may contain a different number of columns.
    Given lst, and integer x, find integers x in the list,
    and return list of tuples, [(x1, y1), (x2, y2) ...] such that
    each tuple is a coordinate - (row, columns), starting with 0.
    Sort coordinates initially by columns in ascending order.
    Also, sort coordinates of the column by rows in descending order.
    
    Examples:
    get_column([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (2, 0), (2, 5), (1, 0)]
    get_column([], 1) == []
    get_column([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    """
    # your code here
    result = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                result.append((i, j))
    result.sort(key=lambda x: x[1])
    for i in range(len(result)):
        result[i] = (len(lst[result[i][0]]) - result[i][1] - 1, result[i][0])
    result.sort(key=lambda x: x[0])
    return result


def get_diagonal(lst, x):
    """
    You are given a 2 dimensional data, as a nested lists,
    which is similar to matrix, however, unlike matrices,
    each row may contain a different number of columns.
    Given lst, and integer x, find integers x in the list,
    and return list of tuples, [(x1, y1), (x2, y2) ...] such that
    each tuple is a coordinate - (row, columns), starting with 0.
    Sort coordinates initially by diagonals in ascending order.
    Also, sort coordinates of the diagonal by rows in descending order.
    
    Examples:
    get_diagonal([
      [1,2,3,4,5,6