"""
The input is defined as two lists of the same length. Write a function to count indices where the lists have the same values.
assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])==4
"""
def count_same_pair(list1, list2):
    count = 0
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            count += 1
    return count

assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])==4
assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[1, 2, 3, 1, 2, 6, 7, 9])==5
assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[1, 2, 3, 4, 5, 6, 7, 8])==8
assert count_same_pair([], [])==0
assert count_same_pair([1], [1])==1
assert count_same_pair([1], [2])==0