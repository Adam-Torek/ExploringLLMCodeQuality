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
    s = s.split()
    result = []
    for word in s:
        if count_consonants(word) == n:
            result.append(word)
    return result

def count_consonants(s):
    """Given a string s, you have been tasked to implement a function that returns 
    the number of consonants in the string s.
    Note: you may assume the input string contains only letters.
    Examples:
    count_consonants("Mary had a little lamb") ==> 10
    count_consonants("simple white space") ==> 0
    count_consonants("Hello world") ==> 8
    count_consonants("Uncle sam") ==> 6
    """
    consonants = "bcdfghjklmnpqrstvwxz"
    count = 0
    for letter in s:
        if letter.lower() in consonants:
            count += 1
    return count

def count_consonants(s):
    """Given a string s, you have been tasked to implement a function that returns 
    the number of consonants in the string s.
    Note: you may assume the input string contains only letters.
    Examples:
    count_consonants("Mary had a little lamb") ==> 10
    count_consonants("simple white space") ==> 0
    count_consonants("Hello world") ==> 8
    count_consonants("Uncle sam") ==> 6
    """
    consonants = "bcdfghjklmnpqrstvwxz"
    count = 0
    for letter in s:
        if letter.lower() in consonants:
            count += 1
    return count

def count_consonants(s):
    """Given a string s, you have been tasked to implement a function that returns 
    the number of consonants in the string s.
    Note: you may assume the input string contains only letters.
    Examples:
    count_consonants("Mary had a little lamb") ==> 10
    count_consonants("simple white space") ==> 0
    count_consonants("Hello world") ==> 8
    count_consonants("Uncle sam") ==> 6
    """
    consonants = "bcdfghjklmnpqrstvwxz"
    count = 0
    for letter in s:
        if letter.lower() in consonants:
            count += 1
    return count

def count_consonants(s):
    """Given a string s, you have been tasked to implement a function that returns 
    the number of consonants in the string s.
    Note: you may assume the input string contains only letters.
    Examples:
    count_consonants("Mary had a little lamb") ==> 10
    count_consonants("simple white space") ==> 0
    count_consonants("Hello world") ==> 8
    count_consonants("Uncle sam