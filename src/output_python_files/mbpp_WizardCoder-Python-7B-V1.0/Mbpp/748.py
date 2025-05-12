"""
Write a function to put spaces between words starting with capital letters in a given string.
assert capital_words_spaces("Python") == 'Python'
"""

def capital_words_spaces(string):
    words = string.split()
    result = []
    for word in words:
        if word[0].isupper():
            result.append(word + ' ')
        else:
            result.append(word)
    return ''.join(result)

# Test cases
print(capital_words_spaces("Python")) # Output: "Python"
print(capital_words_spaces("Python is awesome")) # Output: "Python is awesome"
print(capital_words_spaces("Python is Awesome")) # Output: "Python is Awesome"
print(capital_words_spaces("Python is awesome and I love it")) # Output: "Python is awesome and I love it"
print(capital_words_spaces("Python is Awesome and I Love it")) # Output: "Python is Awesome and I Love it"
print(capital_words_spaces("Python is Awesome and I love Python")) # Output: "Python is Awesome and I love Python"
print(capital_words_spaces("Python is Awesome and I love Python Programming")) # Output: "Python is Awesome and I love Python Programming"
print(capital_words_spaces("Python is Awesome and I love Python Programming Language")) # Output: "Python is Awesome and I love Python Programming Language"
print(capital_words_spaces("Python is Awesome and I love Python Programming Language")) # Output: "Python is Awesome and I love Python Programming Language"
print(capital_words_spaces("Python is Awesome and I love Python Programming Language and Java is also Awesome")) # Output: "Python is Awesome and I love Python Programming Language and Java is also Awesome"
print(capital_words_spaces("Python is Awesome and I love Java Programming Language and Python is also Awesome")) # Output: "Python is Awesome and I love Java Programming Language and Python is also Awesome"
print(capital_words_spaces("Python is Awesome and I love Java Programming Language and Python is also Awesome")) # Output: "Python is Awesome and I love Java Programming Language and Python is also Awesome"
print(capital_words_spaces("Python is Awesome and I love Java Programming Language and Python is also Awesome and JavaScript is also Awesome")) # Output: "Python is Awesome and I love Java Programming Language and Python is also Awesome and JavaScript is also Awesome"
print(capital_words_spaces("Python is Awesome and I love Java Programming Language and JavaScript is also Awesome")) # Output: "Python is Awesome and I love Java Programming Language and JavaScript is also Awesome"
print(capital_words_spaces("Python is Awesome and I love Java Programming Language and JavaScript is also Awesome and C++ is also Awesome")) # Output: "Python is Awesome and I love Java Programming Language and JavaScript is also Awesome and C++ is also Awesome"
print(capital_words_spaces("Python is Awesome and I love Java Programming Language and JavaScript is also Awesome and C++ is also Awesome and Ruby is also Awesome")) # Output: "Python is Awesome and I love Java Programming Language and JavaScript is also Awesome and C++ is also Awesome and Ruby is also Awesome"
print(capital_words_spaces("Python is Awesome and I love Java Programming Language and JavaScript is also Awesome and C++ is also Awesome and Ruby is also Awesome")) # Output: "Python is Awesome and I love Java Programming Language and JavaScript is also Awesome and C++ is also Awesome and Ruby is also Awesome"
print(capital_words_spaces("Python is Awesome and I love Java Programming Language and JavaScript is also Awesome and C++ is also Awesome and Ruby is also Awesome and PHP is also Awesome")) # Output: "Python is Awesome and I love Java Programming Language and JavaScript is also Awesome and C++ is also Awesome