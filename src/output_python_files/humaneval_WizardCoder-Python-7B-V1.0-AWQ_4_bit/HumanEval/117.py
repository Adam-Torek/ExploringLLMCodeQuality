def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    # split the string into words
    words = s.split()
    # initialize an empty list to store the words with n consonants
    result = []
    # iterate through each word in the list
    for word in words:
        # count the number of consonants in the word
        consonants = sum(1 for letter in word if letter.lower() not in 'aeiou')
        # if the word has exactly n consonants, add it to the result list
        if consonants == n:
            result.append(word)
    return result

# test the function with the given examples
print(select_words("Mary had a little lamb", 4)) # should return ["little"]
print(select_words("Mary had a little lamb", 3)) # should return ["Mary", "lamb"]
print(select_words("simple white space", 2)) # should return []
print(select_words("Hello world", 4)) # should return ["world"]
print(select_words("Uncle sam", 3)) # should return ["Uncle"]

# test the function with some additional examples
print(select_words("This is a test string", 5)) # should return ["This", "string"]
print(select_words("This is a test string", 1)) # should return ["a", "is", "test"]
print(select_words("This is a test string", 0)) # should return []
print(select_words("", 10)) # should return []
print(select_words("a b c d e f g h i j k l m n o p q r s t u v w x y z", 10)) # should return []
print(select_words("a b c d e f g h i j k l m n o p q r s t u v w x y z", 0)) # should return []
print(select_words("a b c d e f g h i j k l m n o p q r s t u v w x y z", 1)) # should return ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(select_words("a b c d e f g h i j k l m n o p q r s t u v w x y z", 2)) # should return ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(select_words("a b c d e f g h i j k l m n o p q r s t u v w x y z", 3)) # should return ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(select_words("a b c d e f g h i j k l m n o p q r s t u v w