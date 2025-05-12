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
    def is_consonant(c):
        return c.lower() not in "aeiou"
    
    def count_consonants(word):
        return sum(1 for c in word if is_consonant(c))
    
    words = s.split()
    return [word for word in words if count_consonants(word) == n]

# Test cases
print(select_words("Mary had a little lamb", 4)) # ["little"]
print(select_words("Mary had a little lamb", 3)) # ["Mary", "lamb"]
print(select_words("simple white space", 2)) # []
print(select_words("Hello world", 4)) # ["world"]
print(select_words("Uncle sam", 3)) # ["Uncle"]
print(select_words("", 4)) # []
print(select_words("a b c d e f g h i j k l m n o p q r s t u v w x y z", 10)) # []
print(select_words("a b c d e f g h i j k l m n o p q r s t u v w x y z", 1)) # ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(select_words("a b c d e f g h i j k l m n o p q r s t u v w x y z", 0)) # []
print(select_words("a b c d e f g h i j k l m n o p q r s t u v w x y z", 2)) # ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(select_words("a b c d e f g h i j k l m n o p q r s t u v w x y z", 1)) # ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(select_words("a b c d e f g h i j k l m n o p q r s t u v w x y z", 3)) # ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(select_words("a b c d e f g h i j k l m n o p q r s t u v w x y z", 4)) # []
print(select_words("a b c d e f g h i j k l m n o p q r s t