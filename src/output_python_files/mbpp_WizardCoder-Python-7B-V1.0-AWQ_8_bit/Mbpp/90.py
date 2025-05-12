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
print(len_log(["programming","language","is","awesome"])) # Output: 8

# Another way to solve this problem using list comprehension
def len_log(lst):
    return max([len(word) for word in lst])

print(len_log(["python","PHP","bigdata"])) # Output: 7
print(len_log(["hello","world","programming"])) # Output: 9
print(len_log(["programming","language","is","awesome"])) # Output: 8