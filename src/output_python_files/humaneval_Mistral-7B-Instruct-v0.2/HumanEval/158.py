def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_str = ""
    max_len = 0
    for word in words:
        len_set = set(word)
        len_str = len(len_set)
        if len_str > max_len:
            max_str = word
            max_len = len_str
    return max_str

# Test cases
print(find_max(["name", "of", "string"]))
print(find_max(["name", "enam", "game"]))
print(find_max(["aaaaaaa", "bb", "cc"]))
print(find_max(["cat", "dog", "mouse"]))
print(find_max(["apple", "banana", "cherry"]))
print(find_max(["hello", "world", "python"]))
print(find_max(["aardvark", "baboon", "caterpillar"]))
print(find_max(["elephant", "hippopotamus", "rhinoceros"]))
print(find_max(["unicorn", "dragon", "phoenix"]))
print(find_max(["zebra", "giraffe", "rhinoceros"]))
print(find_max(["antelope", "buffalo", "cobra"]))
print(find_max(["camel", "dromedary", "elephant"]))
print(find_max(["flamingo", "gazelle", "hippopotamus"]))
print(find_max(["iguana", "jaguar", "kangaroo"]))
print(find_max(["lion", "tiger", "zebra"]))
print(find_max(["monkey", "naked", "octopus"]))
print(find_max(["panda", "quokka", "raccoon"]))
print(find_max(["snake", "tiger", "unicorn"]))
print(find_max(["vulture", "wolf", "xenops"]))
print(find_max(["yak", "zebra", "zebra"]))
print(find_max(["aardvark", "baboon", "caterpillar", "dolphin"]))
print(find_max(["elephant", "hippopotamus", "rhinoceros", "tiger"]))
print(find_max(["unicorn", "dragon", "phoenix", "unicorn"]))
print(find_max(["aardvark", "baboon", "caterpillar", "dolphin", "elephant"]))
print(find_max(["elephant", "hippopotamus", "rhinoceros", "tiger", "unicorn"]))
print(find_max(["unicorn", "dragon", "phoenix", "unicorn", "unicorn"]))
print(find_