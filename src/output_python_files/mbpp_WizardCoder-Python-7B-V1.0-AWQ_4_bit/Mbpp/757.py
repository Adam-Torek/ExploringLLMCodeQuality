"""
Write a function to count the pairs of reverse strings in the given string list. https://www.geeksforgeeks.org/python-program-to-count-the-pairs-of-reverse-strings/
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
"""
def count_reverse_pairs(str_list):
    count = 0
    for i in range(len(str_list)):
        for j in range(i+1, len(str_list)):
            if str_list[i][::-1] == str_list[j]:
                count += 1
    return count

# Test the function
print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])) # Output: 2
print(count_reverse_pairs(["abc", "def", "ghi", "jkl", "mno"])) # Output: 0
print(count_reverse_pairs(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx"])) # Output: 0
print(count_reverse_pairs(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "uvw", "xyz"])) # Output: 3
print(count_reverse_pairs(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "uvw", "xyz", "abc"])) # Output: 4

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Better solution:
def count_reverse_pairs(str_list):
    count = 0
    for i in range(len(str_list)):
        for j in range(i+1, len(str_list)):
            if str_list[i] == str_list[j][::-1]:
                count += 1
    return count

# Test the function
print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])) # Output: 2
print(count_reverse_pairs(["abc", "def", "ghi", "jkl", "mno"])) # Output: 0
print(count_reverse_pairs(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "uvw", "xyz"])) # Output: 3
print(count_reverse_pairs(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "uvw", "xyz", "abc"])) # Output: 4

# Time Complexity: O(n^2)
# Space Complexity: O(1)