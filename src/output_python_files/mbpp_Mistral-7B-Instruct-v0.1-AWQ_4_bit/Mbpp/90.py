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

# assert len_log(["python","PHP","bigdata"]) == 7
# assert len_log(["python","PHP","bigdata","Python"]) == 9