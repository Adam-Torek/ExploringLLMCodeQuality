def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # Your code here
    return s.split(',')
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    # Your code here
    return s.split(r'\s*,\s*')

# Test cases
print(words_string("Hi, my name is John"))
print(words_string("One, two, three, four, five, six"))
print(words_string("Hi my name is John"))
print(words_string("One two three four five six"))
print(words_string(""))
print(words_string("Hi"))
print(words_string(""))
print(words_string("Hi,  my name is John"))
print(words_string("One, two, three, four, five, six, seven"))
print(words_string("Hi, my name is John, I'm from London"))
print(words_string("One, two, three, four, five, six, seven, eight"))
print(words_string("Hi, my name is John, I'm from London, England"))
print(words_string("One, two, three, four, five, six, seven, eight, nine"))
print(words_string("Hi, my name is John, I'm from London, England, United Kingdom"))
print(words_string("One, two, three, four, five, six, seven, eight, nine, ten"))
print(words_string("Hi, my name is John, I'm from London, England, United Kingdom, Europe"))
print(words_string("One, two, three, four, five, six, seven, eight, nine, ten, eleven"))
print(words_string("Hi, my name is John, I'm from London, England, United Kingdom, Europe, World"))
print(words_string("One, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve"))
print(words_string("Hi, my name is John, I'm from London, England, United Kingdom, Europe, World, Universe"))
print(words_string("One, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen"))
print(words_string("Hi, my name is John, I'm from London, England, United Kingdom, Europe, World, Universe, Multiverse"))
print(words_string("One, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen"))
print(words_string("Hi, my name is John, I'm from London, England, United Kingdom, Europe, World, Universe, Multiverse, Infinity"))
print(words_string("One, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen"))
print(words_string("Hi, my name is John, I'm from London, England, United Kingdom, Europe, World, Universe, Multiverse, Infinity, Eternity"))
print(words_string("One, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen"))
print(words_string("Hi, my name is John, I'm from London, England, United Kingdom, Europe, World, Universe,