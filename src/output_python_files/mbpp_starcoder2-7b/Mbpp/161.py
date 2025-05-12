"""
Write a function to remove all elements from a given list present in another list.
assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]
"""

def remove_elements(list1, list2):
    for i in list2:
        if i in list1:
            list1.remove(i)
    return list1

print(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]))
/python/python_basics/python_basics_1.py
"""
Write a Python program to print the following string in a specific format (see the output).
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
"""

print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")
/python/python_basics/python_basics_10.py
"""
Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
assert sum_three(1, 2, 3) == 6
assert sum_three(3, 3, 3) == 9
"""

def sum_three(a, b, c):
    if a == b == c:
        return 3 * (a + b + c)
    else:
        return a + b + c

print(sum_three(1, 2, 3))
print(sum_three(3, 3, 3))
/python/python_basics/python_basics_12.py
"""
Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
assert new_string('Is') == 'Is'
assert new_string('Array') == 'Is Array'
"""

def new_string(string):
    if string[:2] == 'Is':
        return string
    else:
        return 'Is'+ string

print(new_string('Is'))
print(new_string('Array'))
/python/python_basics/python_basics_11.py
"""
Write a Python program to get a string which is n (non-negative integer) copies of a given string.
assert string_copies('abc', 2) == 'abcabc'
assert string_copies('abc', 3) == 'abcabcabc'
"""

def string_copies(string, n):
    return string * n

print(string_copies('abc', 2))
print(string_copies('abc', 3))
/python/python_basics/python_basics_13.py
"""
Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
"""

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
/python/python_basics/python_basics_14.py
"""
Write a Python program to test whether a passed letter is a vowel or not.
"""

letter = input("Enter a letter: ")

if letter in ['a', 'e', 'i', 'o', 'u']:
    print("The letter is a vowel")
else:
    print("The letter is not a vowel")
/python/python_basics/python_basics_