def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
#     l = [1, 2, 3]
#     l = [5, 6, 3, 4, 8, 9, 2]
    l = sorted(l)
    l_new = []
    for i in range(len(l)):
        if i % 3!= 0:
            l_new.append(l[i])
        else:
            l_new.append(l[i])
            l_new.append(l[i])
    return l_new

# Test cases
print(sort_third([1, 2, 3]))
print(sort_third([5, 6, 3, 4, 8, 9, 2]))<|endoftext|>