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
    # initialize max_word and max_count
    max_word = ""
    max_count = 0
    # iterate over the list
    for word in words:
        # count the number of unique characters in the word
        count = len(set(word))
        # if the current word has more unique characters than max_word,
        # update max_word and max_count
        if count > max_count:
            max_word = word
            max_count = count
    # return the max_word
    return max_word