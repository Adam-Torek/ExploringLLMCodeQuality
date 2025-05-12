def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    return s.replace(",", " ").split()


# Test cases
print(words_string("Hi, my name is John")) # ["Hi", "my", "name", "is", "John"]
print(words_string("One, two, three, four, five, six")) # ["One", "two", "three", "four", "five", "six"]
print(words_string("Hello world")) # ["Hello", "world"]
print(words_string("A, B, C, D, E, F")) # ["A", "B", "C", "D", "E", "F"]
print(words_string("A B C D E F")) # ["A", "B", "C", "D", "E", "F"]
print(words_string("1, 2, 3, 4, 5, 6, 7, 8, 9, 10")) # ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
print(words_string("1 2 3 4 5 6 7 8 9 10")) # ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
print(words_string("")) # []
print(words_string("1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10")) # ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
print(words_string("1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10")) # ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
print(words_string("1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10")) # ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "1", "2", "3", "4", "5", "6", "7", "8", "9",