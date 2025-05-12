"""
Write a python function to find the first repeated character in a given string.
assert first_repeated_char("abcabc") == "a"
"""
def first_repeated_char(string):
    """
    This function takes a string as an input and returns the first character that is repeated in the string.
    """
    #Creating a dictionary to store the characters and their count
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    #Iterating through the dictionary to find the first character that is repeated
    for k,v in char_count.items():
        if v > 1:
            return k

    #If no repeated character is found, returning None
    return None