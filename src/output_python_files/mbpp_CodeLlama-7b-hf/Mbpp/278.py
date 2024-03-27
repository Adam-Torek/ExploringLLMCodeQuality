"""
Write a function to find the number of elements that occurs before the tuple element in the given tuple.
assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
"""


def count_first_elements(t):
    count = 0
    for i in t:
        if type(i) == tuple:
            count += 1
        else:
            break
    return count


print(count_first_elements((1, 5, 7, (4, 6), 10)))
print(count_first_elements((1, 5, 7, (4, 6), 10, 11)))
print(count_first_elements((1, 5, 7, (4, 6), 10, 11, 12)))
print(count_first_elements((1, 5, 7, (4, 6), 10, 11, 12, 13)))
print(count_first_elements((1, 5, 7, (4, 6), 10, 11, 12, 13, 14)))
print(count_first_elements((1, 5, 7, (4, 6), 10, 11, 12, 13, 14, 15)))
print(count_first_elements((1, 5, 7, (4, 6), 10, 11, 12, 13, 14, 15, 16)))
print(count_first_elements((1, 5, 7, (4, 6), 10, 11, 12, 13, 14, 15, 16, 17)))
print(count_first_elements((1, 5, 7, (4, 6), 10, 11, 12, 13, 14, 15, 16, 17, 18)))
print(count_first_elements((1, 5, 7, (4, 6), 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)))
print(count_first_elements((1, 5, 7, (4, 6), 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)))
print(count_first_elements((1, 5, 7, (4, 6), 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21)))
print(count_first_elements((1, 5, 7, (4, 6), 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22)))
print(count_first_elements((1, 5, 7, (4, 6), 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)))
print(count_first_elements((1, 5, 7, (4, 6), 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)))
print(count_first_elements((1, 5, 7, (4, 6), 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25)))
print