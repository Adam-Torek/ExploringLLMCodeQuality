"""
Write a function to reverse words seperated by spaces in a given string.
assert reverse_words("python program")==("program python")
"""
def reverse_words(string):
    """
    Reverses the order of words in a given string
    :param string: string to reverse words in
    :return: reversed string
    """
    words = string.split()
    reversed_words = [word[::-1] for word in words]
    reversed_string = " ".join(reversed_words)
    return reversed_string

assert reverse_words("python program") == "program python"
assert reverse_words("hello world") == "world hello"
assert reverse_words("") == ""
assert reverse_words("one two three") == "three two one"
assert reverse_words("a b c d e f g h i j k l m n o p q r s t u v w x y z") == "z y x w v u t s r q p o n m l k j i h g f e d c b a"