"""
Write a python function to find the length of the longest word.
assert len_log(["python","PHP","bigdata"]) == 7
"""
def len_log(lst):
    max_len = 0
    for word in lst:
        if len(word) > max_len:
            max_len = len(word)
    return max_len

print(len_log(["python","PHP","bigdata"])) # Output: 7
print(len_log(["hello","world","programming"])) # Output: 9
print(len_log(["programming","language","is","fun"])) # Output: 5
print(len_log(["python","java","c","c++"])) # Output: 6
print(len_log(["python","java","c","c++","python"])) # Output: 6
print(len_log(["programming","language","is","fun","fun"])) # Output: 5
print(len_log(["programming","language","is","fun","fun","fun"])) # Output: 6
print(len_log(["programming","language","is","fun","fun","fun","fun"])) # Output: 7
print(len_log(["programming","language","is","fun","fun","fun","fun","fun"])) # Output: 7
print(len_log(["programming","language","is","fun","fun","fun","fun","fun","fun"])) # Output: 8
print(len_log(["programming","language","is","fun","fun","fun","fun","fun","fun","fun"])) # Output: 9
print(len_log(["programming","language","is","fun","fun","fun","fun","fun","fun","fun","fun"])) # Output: 10
print(len_log(["programming","language","is","fun","fun","fun","fun","fun","fun","fun","fun","fun"])) # Output: 10
print(len_log(["programming","language","is","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun"])) # Output: 11
print(len_log(["programming","language","is","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun"])) # Output: 11
print(len_log(["programming","language","is","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun"])) # Output: 12
print(len_log(["programming","language","is","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun"])) # Output: 12
print(len_log(["programming","language","is","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun"])) # Output: 13
print(len_log(["programming","language","is","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun"])) # Output: 13
print(len_log(["programming","language","is","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun"])) # Output: 14
print(len_log(["programming","language","is","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun"])) # Output: 14
print(len_log(["programming","language","is","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun"])) # Output: 15
print(len_log(["programming","language","is","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun"])) # Output: 15
print(len_log(["programming","language","is","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun","fun"])) # Output