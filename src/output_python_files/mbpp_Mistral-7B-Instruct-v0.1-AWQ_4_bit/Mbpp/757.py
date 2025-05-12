"""
Write a function to count the pairs of reverse strings in the given string list. https://www.geeksforgeeks.org/python-program-to-count-the-pairs-of-reverse-strings/
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
"""
def count_reverse_pairs(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i][::-1] == lst[j]:
                count += 1
    return count

#test
print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]))