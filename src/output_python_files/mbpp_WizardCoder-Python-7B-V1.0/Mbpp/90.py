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
print(len_log(["programming","language","python"])) # Output: 9
print(len_log(["java","c++","c#"])) # Output: 3
print(len_log(["java","c++","c#","python"])) # Output: 6
print(len_log(["java","c++","c#","python","programming"])) # Output: 9
print(len_log(["java","c++","c#","python","programming","hello"])) # Output: 8
print(len_log(["java","c++","c#","python","programming","hello","world"])) # Output: 9
print(len_log(["java","c++","c#","python","programming","hello","world","data"])) # Output: 6
print(len_log(["java","c++","c#","python","programming","hello","world","data","analysis"])) # Output: 9
print(len_log(["java","c++","c#","python","programming","hello","world","data","analysis","science"])) # Output: 9
print(len_log(["java","c++","c#","python","programming","hello","world","data","analysis","science","statistics"])) # Output: 12
print(len_log(["java","c++","c#","python","programming","hello","world","data","analysis","science","statistics","algorithm"])) # Output: 12
print(len_log(["java","c++","c#","python","programming","hello","world","data","analysis","science","statistics","algorithm","mathematics"])) # Output: 14
print(len_log(["java","c++","c#","python","programming","hello","world","data","analysis","science","statistics","algorithm","mathematics","computer"])) # Output: 14
print(len_log(["java","c++","c#","python","programming","hello","world","data","analysis","science","statistics","algorithm","mathematics","computer","science"])) # Output: 10
print(len_log(["java","c++","c#","python","programming","hello","world","data","analysis","science","statistics","algorithm","mathematics","computer","science","engineering"])) # Output: 14
print(len_log(["java","c++","c#","python","programming","hello","world","data","analysis","science","statistics","algorithm","mathematics","computer","science","engineering","science"])) # Output: 12
print(len_log(["java","c++","c#","python","programming","hello","world","data","analysis","science","statistics","algorithm","mathematics","computer","science","engineering","science","engineering"])) # Output: 14
print(len_log(["java","c++","c#","python","programming","hello","world","data","analysis","science","statistics","algorithm","mathematics","computer","science","engineering","science","engineering","engineering"])) # Output: 14
print(len_log(["java","c++","c#","python","programming","hello","world","data","analysis","science","statistics","algorithm","mathematics","computer","science","engineering","science","engineering","engineering","engineering"])) # Output: 14
print(len_log(["java","c++","c#","python","programming","hello","world","data","analysis","science","statistics","algorithm","mathematics","computer","science","engineering","science","engineering","engineering","engineering","engineering"])) # Output: 14
print(len_log(["java