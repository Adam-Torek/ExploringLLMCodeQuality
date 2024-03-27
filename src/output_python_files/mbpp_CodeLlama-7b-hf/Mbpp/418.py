"""
Write a python function to find the element of a list having maximum length.
assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
"""


def Find_Max(lst):
    max_len = 0
    max_len_list = []
    for i in lst:
        if len(i) > max_len:
            max_len = len(i)
            max_len_list = i
    return max_len_list


if __name__ == '__main__':
    print(Find_Max([['A'], ['A', 'B'], ['A', 'B', 'C']]))
</s>