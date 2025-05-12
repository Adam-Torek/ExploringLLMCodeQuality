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
print(words_string("Hi, my name is John"))  # ["Hi", "my", "name", "is", "John"]
print(words_string("One, two, three, four, five, six"))  # ["One", "two", "three", "four", "five", "six"]
print(words_string("This is a test"))  # ["This", "is", "a", "test"]
print(words_string("Hello world"))  # ["Hello", "world"]
print(words_string("A, long, list, of, words, in, this, format"))  # ["A", "long", "of", "words", "in", "this", "format"]
print(words_string("One, two, three, four, five, six, seven, eight, nine, ten"))  # ["One", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
print(words_string("One two three four five six"))  # ["One", "two", "three", "four", "five", "six"]
print(words_string("One two three four five, six"))  # ["One", "two", "three", "four", "five", "six"]
print(words_string("One two three four, five six"))  # ["One", "two", "three", "four", "five", "six"]
print(words_string("One two three four five six"))  # ["One", "two", "three", "four", "five", "six"]
print(words_string("One two three four five, six"))  # ["One", "two", "three", "four", "five", "six"]
print(words_string("One two three four five six"))  # ["One", "two", "three", "four", "five", "six"]
print(words_string("One two three four five, six"))  # ["One", "two", "three", "four", "five", "six"]
print(words_string("One two three four five, six"))  # ["One", "two", "three", "four", "five", "six"]
print(words_string("One two three four five, six"))  # ["One", "two", "three", "four", "five", "six"]
print(words_string("One two three four five, six"))  # ["One", "two", "three", "four", "five", "six"]
print(words_string("One two three four five, six"))  # ["One", "two", "three", "four", "five", "six"]
print(words_string("One two three four five, six"))  # ["One", "two", "three", "four", "five", "six"]
print(words_string("One two three four five, six"))  # ["One", "two", "three", "four", "five", "six"]
print(words_string("One two three four five, six"))  # ["One", "two", "three", "four", "five", "six"]
print(words_string("One two three four five, six"))  # ["One", "two", "three", "four", "five", "six"]
print(words_string("One two three four five, six"))  # ["One", "two", "three", "four", "five", "six"]
print(words_string("One two three four five, six"))  # ["One", "two", "three", "four", "five", "six"]
print(words_string("One two three four five, six"))  # ["One", "two", "three", "four", "