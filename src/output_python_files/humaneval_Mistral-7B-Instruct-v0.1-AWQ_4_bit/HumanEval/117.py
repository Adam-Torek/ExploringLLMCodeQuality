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
    # split the string into a list of words
    words = s.split()
    # create an empty list to store the selected words
    selected_words = []
    # iterate over each word in the list of words
    for word in words:
        # count the number of consonants in the word
        count = 0
        for letter in word:
            if letter.isalpha() and letter != 'a' and letter != 'e' and letter != 'i' and letter != 'o' and letter != 'u':
                count += 1
        # if the count of consonants is equal to n, add the word to the list of selected words
        if count == n:
            selected_words.append(word)
    # return the list of selected words
    return selected_words