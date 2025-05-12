def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb","cc"]) == ""aaaaaaa"
    """

def unique_chars(word):
    """Write a function that accepts a string.
    The function should return the number of unique characters in the string.

    unique_chars("hello") == 5
    unique_chars("world") == 5
    unique_chars("python") == 6
    unique_chars("programming") == 10
    """

def longest_word(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the longest word in the list.

    longest_word(["name", "of", "string"]) == "string"
    longest_word(["name", "enam", "game"]) == "game"
    longest_word(["aaaaaaa", "bb","cc"]) == "aaaaaaa"
    """

def longest_unique_word(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the longest word with maximum
    number of unique characters. If multiple words have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    longest_unique_word(["name", "of", "string"]) == "string"
    longest_unique_word(["name", "enam", "game"]) == "enam"
    longest_unique_word(["aaaaaaa", "bb","cc"]) == "aaaaaaa"
    """

def main():
    words = ["name", "of", "string"]
    print(find_max(words))
    print(unique_chars("hello"))
    print(longest_word(words))
    print(longest_unique_word(words))

if __name__ == "__main__":
    main()<|endoftext|>