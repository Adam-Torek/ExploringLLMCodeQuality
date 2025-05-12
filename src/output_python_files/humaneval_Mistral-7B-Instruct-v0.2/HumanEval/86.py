def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    words = s.split()
    result = ""
    for word in words:
        result += word + " "
        for char in word:
            result = result[:-1]
            result += chr(ord(char) - ord('a') if char.isalpha() else char)
    return result.strip()

# Test Cases
print(anti_shuffle("Hi"))
print(anti_shuffle("hello"))
print(anti_shuffle("Hello World!!!"))
print(anti_shuffle("This is a test"))
print(anti_shuffle("The quick brown fox jumps over the lazy dog"))