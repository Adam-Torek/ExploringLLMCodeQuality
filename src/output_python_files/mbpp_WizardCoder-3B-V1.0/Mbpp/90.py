"""
Write a python function to find the length of the longest word.
assert len_log(["python","PHP","bigdata"]) == 7
"""

def len_log(words):
    max_len = 0
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
    return max_len

# Test the function
print(len_log(["python","PHP","bigdata"])) # Output: 7<|endoftext|>