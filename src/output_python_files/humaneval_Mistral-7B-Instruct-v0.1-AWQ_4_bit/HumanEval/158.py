def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # sort the list
    words.sort()
    # create a dictionary to store the count of unique characters
    char_count = {}
    # iterate over the list
    for word in words:
        # create a set of unique characters
        unique_chars = set(word)
        # count the number of unique characters
        count = len(unique_chars)
        # add the word and its count to the dictionary
        char_count[word] = count
    # find the word with maximum count
    max_count = max(char_count.values())
    max_word = [word for word, count in char_count.items() if count == max_count][0]
    return max_word

# test the function
print(find_max(["name", "of", "string"]))
print(find_max(["name", "enam", "game"]))
print(find_max(["aaaaaaa", "bb", "cc"]))