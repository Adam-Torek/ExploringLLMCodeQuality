"""
Write a function to reverse words seperated by spaces in a given string.
assert reverse_words("python program")==("program python")
"""

def reverse_words(string):
    words = string.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

print(reverse_words("python program")) # Output: "program python"
print(reverse_words("hello world")) # Output: "world hello"
print(reverse_words("i am a student")) # Output: "student a am i"
print(reverse_words("reverse words in a string")) # Output: "string in a words reverse"

# Time Complexity: O(n)
# Space Complexity: O(n)
# where n is the length of the input string.
# We are using the split() method which has a time complexity of O(n) and join() method which has a time complexity of O(n)
# The space complexity is also O(n) as we are creating a new list to store the reversed words.