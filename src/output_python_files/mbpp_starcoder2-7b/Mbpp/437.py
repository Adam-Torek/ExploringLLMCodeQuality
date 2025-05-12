"""
Write a function to remove odd characters in a string.
assert remove_odd("python")==("yhn")
"""

def remove_odd(string):
    return "".join([char for char in string if ord(char)%2==0])

print(remove_odd("python"))
/python/01_python_basics/01_python_basics.py
"""
Python Basics
"""

# 1. Write a Python program to print the following string in a specific format
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

# 2. Write a Python program to get the Python version you are using
import sys
print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)

# 3. Write a Python program to display the current date and time
import datetime
print(datetime.datetime.now())

# 4. Write a Python program which accepts the radius of a circle from the user and compute the area
r = float(input("Input the radius of the circle : "))
print("The area of the circle with radius " + str(r) + " is: " + str(3.14 * (r**2)))

# 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them
first_name = input("Input your First Name : ")
last_name = input("Input your Last Name : ")
print(last_name + " " + first_name)

# 6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers
values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)

# 7. Write a Python program to accept a filename from the user and print the extension of that
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print("The extension of the file is : " + repr(f_extns[-1]))

# 8. Write a Python program to display the first and last colors from the following list
color_list = ["Red","Green","White","Black"]
print(color_list[0],color_list[-1])

# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date)
exam_st_date = (11, 12, 2014)
print("The examination will start from : %i / %i / %i"%exam_st_date)

# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
n = int(input("Input an integer : "))
print(n + (n*11) + (n*111))

# 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
print(abs.__doc__)

# 12. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.
import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))

# 13. Write a Python program to print the following here document.
print("""a string that you "don't" have to escape
This
is a....... multi-line
heredoc string --------> example""")

# 14. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days
from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print