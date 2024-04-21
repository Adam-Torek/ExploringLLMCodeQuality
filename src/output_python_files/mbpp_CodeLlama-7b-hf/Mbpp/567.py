"""
Write a function to check whether a specified list is sorted or not.
assert issort_list([1,2,4,6,8,10,12,14,16,17])==True
"""


def issort_list(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True


if __name__ == '__main__':
    print(issort_list([1, 2, 4, 6, 8, 10, 12, 14, 16, 17]))
    print(issort_list([1, 2, 4, 6, 8, 10, 12, 14, 16, 17, 18]))
    print(issort_list([1, 2, 4, 6, 8, 10, 12, 14, 16, 17, 18, 20]))
    print(issort_list([1, 2, 4, 6, 8, 10, 12, 14, 16, 17, 18, 20, 22]))
    print(issort_list([1, 2, 4, 6, 8, 10, 12, 14, 16, 17, 18, 20, 22, 24]))
    print(issort_list([1, 2, 4, 6, 8, 10, 12, 14, 16, 17, 18, 20, 22, 24, 26]))
    print(issort_list([1, 2, 4, 6, 8, 10, 12, 14, 16, 17, 18, 20, 22, 24, 26, 28]))
    print(issort_list([1, 2, 4, 6, 8, 10, 12, 14, 16, 17, 18, 20, 22, 24, 26, 28, 30]))
    print(issort_list([1, 2, 4, 6, 8, 10, 12, 14, 16, 17, 18, 20, 22, 24, 26, 28, 30, 32]))
    print(issort_list([1, 2, 4, 6, 8, 10, 12, 14, 16, 17, 18, 20, 22, 24, 26, 28, 30, 32, 34]))
    print(issort_list([1, 2, 4, 6, 8, 10, 12, 14, 16, 17, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]))
    print(issort_list([1, 2, 4, 6, 8, 10, 12, 14, 16, 17, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]))
    print(issort_list([1, 2, 4, 6, 8, 10, 12, 14, 16, 17, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]))
    print(issort_list([1, 2, 4, 6, 8, 10, 12, 14, 16,