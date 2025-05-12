"""
Write a function to find the common elements in given nested lists.
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
"""

def common_in_nested_lists(nested_lists):
    """
    :param nested_lists: list of lists
    :return: set of common elements
    """
    return set.intersection(*map(set, nested_lists))


if __name__ == '__main__':
    print(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))
/python/python_basics/00_python_basics/00_python_basics.py
"""
Python Basics
"""

# 1. Write a Python program to print the following string in a specific format (see the output).
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :
# Twinkle, twinkle, little star,
#     How I wonder what you are!
#         Up above the world so high,
#         Like a diamond in the sky.
# Twinkle, twinkle, little star,
#     How I wonder what you are

print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")

# 2. Write a Python program to get the Python version you are using.
import sys
print(sys.version)

# 3. Write a Python program to display the current date and time.
import datetime
print(datetime.datetime.now())

# 4. Write a Python program which accepts the radius of a circle from the user and compute the area.
import math
radius = float(input("Input the radius of the circle : "))
print("The area of the circle with radius " + str(radius) + " is: " + str(math.pi * radius**2))

# 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
first_name = input("Input your first name : ")
last_name = input("Input your last name : ")
print(last_name + " " + first_name)

# 6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ', list)
print('Tuple : ', tuple)

# 7. Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White","Black"]
print(color_list[0] + " " + color_list[-1])

# 8. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
print("The examination will start from : %i / %i / %i"%exam_st_date)

# 9. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
n = int(input("Input an integer : "))
print(n + (n*11) + (n*111))

# 10. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
import builtins
print(dir(builtins))

# 11. Write a Python program to print the calendar of a given month and year.
#