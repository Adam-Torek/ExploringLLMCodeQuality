"""
The input is defined as two lists of the same length. Write a function to count indices where the lists have the same values.
assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])==4
"""

def count_same_pair(list1, list2):
    count = 0
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            count += 1
    return count

print(count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9]))
<file_sep>/python/python_basics/python_basics_1.py
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
<file_sep>/python/python_basics/python_basics_10.py
"""
Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
assert sum_three(1,2,3)==6
assert sum_three(3,3,3)==9
"""

def sum_three(a,b,c):
    if a == b == c:
        return 3*(a+b+c)
    else:
        return a+b+c

print(sum_three(1,2,3))
print(sum_three(3,3,3))
<file_sep>/python/python_basics/python_basics_11.py
"""
Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
assert new_string("Is")=="Is"
assert new_string("Array")=="Is Array"
"""

def new_string(string):
    if string[:2] == "Is":
        return string
    else:
        return "Is " + string

print(new_string("Is"))
print(new_string("Array"))
<file_sep>/python/python_basics/python_basics_12.py
"""
Write a Python program to get a string which is n (non-negative integer) copies of a given string.
assert string_copies("Hi", 2)=="HiHi"
assert string_copies("Hi", 3)=="HiHiHi"
"""

def string_copies(string, n):
    return string*n

print(string_copies("Hi", 2))
print(string_copies("Hi", 3))
<file_sep>/python/python_basics/python_basics_13.py
"""
Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
assert even_odd(2)=="Even"
assert even_odd(3)=="Odd"
"""

def even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_odd(2))
print(even_odd(3))
<file_sep>/python/python_basics/python_basics_14.py
"""
Write a Python program to test whether a passed letter is a vowel or not.
assert vowel_test("a")==True
assert vowel_test("b")==False
"""

def vowel_test(letter):
    if letter in "aeiou":