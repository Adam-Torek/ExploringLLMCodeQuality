"""
Write a function to remove odd characters in a string.
assert remove_odd("python")==("yhn")
"""
def remove_odd(string):
    """
    This function removes all odd characters from a string.
    """
    # define a set of odd characters
    odd_chars = set("!@#$%^&*()_+-{}[]|;:'\",<.>/?`~")
    # define an empty string to hold the result
    result = ""
    # iterate over each character in the string
    for char in string:
        # check if the character is not in the set of odd characters
        if char not in odd_chars:
            # append the character to the result
            result += char
    # return the result
    return result

# test the function
assert remove_odd("python")==("yhn")