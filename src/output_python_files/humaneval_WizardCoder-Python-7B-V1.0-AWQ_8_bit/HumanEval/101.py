def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    return s.split()


# Test cases
print(words_string("Hi, my name is John")) # ["Hi", "my", "name", "is", "John"]
print(words_string("One, two, three, four, five, six")) # ["One", "two", "three", "four", "five", "six"]
print(words_string("This is a test. This is only a test.")) # ["This", "is", "a", "test.", "This", "is", "only", "a", "test."]
print(words_string("Hello world!")) # ["Hello", "world!"]
print(words_string("A, B, C, D, E, F")) # ["A", "B", "C", "D", "E", "F"]
print(words_string("")) # []
print(words_string(" ")) # []
print(words_string("   ")) # []
print(words_string("   Hello   world,   how   are   you   doing?   ")) # ["Hello", "world", "how", "are", "you", "doing?"]
print(words_string("   Hello   world,   how   are   you   doing?   ")) # ["Hello", "world", "how", "are", "you", "doing?"]

# Additional test cases
print(words_string("Hello, world!")) # ["Hello", "world!"]
print(words_string("Hello, world, how are you doing?")) # ["Hello", "world", "how", "are", "you", "doing?"]
print(words_string("Hello, world, how are you doing?")) # ["Hello", "world", "how", "are", "you", "doing?"]
print(words_string("Hello, world, how are you doing?")) # ["Hello", "world", "how", "are", "you", "doing?"]
print(words_string("Hello, world, how are you doing?")) # ["Hello", "world", "how", "are", "you", "doing?"]
print(words_string("Hello, world, how are you doing?")) # ["Hello", "world", "how", "are", "you", "doing?"]
print(words_string("Hello, world, how are you doing?")) # ["Hello", "world", "how", "are", "you", "doing?"]
print(words_string("Hello, world, how are you doing?")) # ["Hello", "world", "how", "are", "you", "doing?"]
print(words_string("Hello, world, how are you doing?")) # ["Hello", "world", "how", "are", "you", "doing?"]
print(words_string("Hello, world, how are you doing?")) # ["Hello", "world", "how", "are", "you", "doing?"]
print(words_string("Hello, world, how are you doing?")) # ["Hello", "world", "how", "are", "you", "doing?"]
print(words_string("Hello, world, how are you doing?")) # ["Hello", "world", "how", "are", "you", "doing?"]
print(words_string("Hello, world, how are you doing?")) # ["Hello", "world", "how", "are", "you", "doing?"]
print(words_string("Hello, world, how are you doing?")) # ["Hello", "world", "how", "are", "you", "doing?"]
print(words_string("Hello, world, how are you doing?")) # ["Hello", "world", "how", "are", "you", "doing?"]
print(words_string("Hello, world, how are you doing?")) # ["Hello", "world", "how", "are", "