"""
Write a function that takes in a string and character, replaces blank spaces in the string with the character, and returns the string.
assert replace_blank("hello people",'@')==("hello@people")
"""
def replace_blank(string, character):
    return string.replace(" ", character)

print(replace_blank("hello people",'@')) # Output: "hello@people"

# Test cases
print(replace_blank("hello world",'@')) # Output: "hello@world"
print(replace_blank("  ",'*') # Output: "**"
print(replace_blank("much ado about nothing",'!') # Output: "much!ado!about!nothing"
print(replace_blank("a b c",'#') # Output: "a#b#c"
print(replace_blank("This is a test",'*') # Output: "This*is*a*test"
print(replace_blank("The quick brown fox jumps over the lazy dog",'#') # Output: "The#quick#brown#fox#jumps#over#the#lazy#dog"

# Test case for empty string
print(replace_blank("",'*') # Output: ""

# Test case for single character string
print(replace_blank("a",'*') # Output: "a"

# Test case for string with no spaces
print(replace_blank("abcdefghij",'*') # Output: "abcdefghij"

# Test case for string with multiple spaces
print(replace_blank("a     b     c",'*') # Output: "a*b*c"