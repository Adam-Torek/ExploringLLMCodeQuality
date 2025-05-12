"""
Write a function to reverse words seperated by spaces in a given string.
assert reverse_words("python program")==("program python")
"""

def reverse_words(string):
    words = string.split()
    words.reverse()
    return " ".join(words)

# Test cases
print(reverse_words("python program")) # Output: program python
print(reverse_words("hello world")) # Output: world hello
print(reverse_words("i am a student")) # Output: student a am i
print(reverse_words("reverse words")) # Output: words reverse
print(reverse_words("reverse this string")) # Output: string this reverse
print(reverse_words("i am a student and a teacher")) # Output: teacher a am i a student
print(reverse_words("i am a student and a teacher and a friend")) # Output: friend a teacher and a am i a student
print(reverse_words("i am a student and a teacher and a friend and a colleague")) # Output: colleague a friend and a teacher and a am i a student

# Time Complexity: O(n)
# Space Complexity: O(n)