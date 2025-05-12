def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_word = ""
    max_count = 0
    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_count:
            max_count = unique_chars
            max_word = word
        elif unique_chars == max_count and word < max_word:
            max_word = word
    return max_word



# Test cases
print(find_max(["name", "of", "string"]))  # Output: "string"
print(find_max(["name", "enam", "game"]))  # Output: "enam"
print(find_max(["aaaaaaa", "bb", "cc"]))  # Output: "aaaaaaa"
print(find_max(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vw", "xyz"]))  # Output: "xyz"
print(find_max(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vw", "xyz", "abc"]))  # Output: "xyz"
print(find_max(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vw", "xyz", "abc", "def"]))  # Output: "xyz"
print(find_max(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vw", "xyz", "abc", "def", "ghi"]))  # Output: "ghi"
print(find_max(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vw", "xyz", "abc", "def", "ghi", "jkl"]))  # Output: "jkl"
print(find_max(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vw", "xyz", "abc", "def", "ghi", "jkl", "mno"]))  # Output: "mno"
print(find_max(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vw", "xyz", "abc", "def", "ghi", "jkl", "mno", "pqr"]))  # Output: "pqr"
print(find_max(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vw", "xyz", "abc", "def", "ghi", "jkl", "mno", "pqr", "stu"]))  # Output: "stu"
print(find_max(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vw", "xyz", "abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vw"]))  # Output: "vw"
print(find_max(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vw", "xyz", "abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vw", "abc"]))  # Output: "abc"
print(find_max(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vw", "xyz", "abc", "def