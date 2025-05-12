"""
Write a function to reverse words seperated by spaces in a given string.
assert reverse_words("python program")==("program python")
"""
def reverse_words(string):
    words = string.split()
    reversed_words = [word[::-1] for word in words]
    reversed_string = " ".join(reversed_words)
    return reversed_string

assert reverse_words("python program") == "program python"
assert reverse_words("hello world") == "dlrow olleh"
assert reverse_words("") == ""
assert reverse_words("a b c") == "c b a"
assert reverse_words("1 2 3") == "3 2 1"
assert reverse_words("1 2 3 4") == "4 3 2 1"
assert reverse_words("1 2 3 4 5") == "5 4 3 2 1"
assert reverse_words("1 2 3 4 5 6") == "6 5 4 3 2 1"
assert reverse_words("1 2 3 4 5 6 7") == "7 6 5 4 3 2 1"
assert reverse_words("1 2 3 4 5 6 7 8") == "8 7 6 5 4 3 2 1"
assert reverse_words("1 2 3 4 5 6 7 8 9") == "9 8 7 6 5 4 3 2 1"
assert reverse_words("1 2 3 4 5 6 7 8 9 0") == "0 9 8 7 6 5 4 3 2 1"
assert reverse_words("1 2 3 4 5 6 7 8 9 0 1") == "1 0 9 8 7 6 5 4 3 2 1"
assert reverse_words("1 2 3 4 5 6 7 8 9 0 1 2") == "2 1 0 9 8 7 6 5 4 3 1 1"
assert reverse_words("1 2 3 4 5 6 7 8 9 0 1 2 3") == "3 2 1 1 0 9 8 7 6 5 4 3"
assert reverse_words("1 2 3 4 5 6 7 8 9 0 1 2 3 4") == "4 3 2 1 1 0 9 8 7 6 5 4"
assert reverse_words("1 2 3 4 5 6 7 8 9 0 1 2 3 4 5") == "5 4 3 2 1 1 0 9 8 7 6 5"
assert reverse_words("1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6") == "6 5 4 3 2 1 1 0 9 8 7 6"
assert reverse_words("1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7") == "7 6 5 4 3 2 1 1 0 9 8 7"
assert reverse_words("1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8") == "8 7 6 5 4 3 2 1 1 0 9 8"
assert reverse_words("1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9") == "9 8 7 6 5 4 3 2 1 1 0 9"
assert reverse_words("1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0