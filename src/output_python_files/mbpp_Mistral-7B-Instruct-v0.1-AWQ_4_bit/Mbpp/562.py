"""
Write a python function to find the length of the longest sublists.
assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4
"""

def Find_Max_Length(lst):
    """
    :param lst: list of lists
    :return: int
    """
    if len(lst) == 0:
        return 0
    else:
        max_length = 1
        for i in range(1,len(lst)):
            for j in range(i):
                if len(lst[i]) - len(lst[j]) > max_length:
                    max_length = len(lst[i]) - len(lst[j])
        return max_length


#assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4
#assert Find_Max_Length([[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5]]) == 4
#assert Find_Max_Length([[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5],[1,2,3,4,5,6]]) == 5
#assert Find_Max_Length([[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5],[1,2,3,4,5,6],[1,2,3,4,5,6,7]]) == 6