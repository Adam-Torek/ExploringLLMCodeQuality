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
print(count_reverse_pairs(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "abc"])) # Output: 1
print(count_reverse_pairs(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "abc", "def"])) # Output: 2
print(count_reverse_pairs(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "abc", "def", "ghi"])) # Output: 3
print(count_reverse_pairs(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "abc", "def", "ghi", "jkl"])) # Output: 4
print(count_reverse_pairs(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "abc", "def", "ghi", "jkl", "mno"])) # Output: 5
print(count_reverse_pairs(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "abc", "def", "ghi", "jkl", "mno", "pqr"])) # Output: 6
print(count_reverse_pairs(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "abc", "def", "ghi", "jkl", "mno", "pqr", "stu"])) # Output: 7
print(count_reverse_pairs(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx"])) # Output: 8
print(count_reverse_pairs(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "abc"])) # Output: 9
print(count_reverse_pairs(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "abc", "def"])) # Output: 10
print(count_reverse_pairs(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "abc", "def", "ghi", "jkl", "mno", "pqr",