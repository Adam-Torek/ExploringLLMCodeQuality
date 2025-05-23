"""
Write a function to get the frequency of all the elements in a list, returned as a dictionary.
assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30])==({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})
"""

def freq_count(lst):
    d = {}
    for i in lst:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

print(freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]))
/python/python_basics/001_python_basics/001_python_basics.py
"""
Python Basics
"""

# 1. Write a Python program to print the following string in a specific format (see the output).
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")

# 2. Write a Python program to get the Python version you are using.
import sys
print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)

# 3. Write a Python program to display the current date and time.
import datetime
now = datetime.datetime.now()
print("Current date and time: ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# 4. Write a Python program which accepts the radius of a circle from the user and compute the area.
from math import pi
r = float(input("Input the radius of the circle : "))
print("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

# 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
first_name = input("Input your First Name : ")
last_name = input("Input your Last Name : ")
print (last_name + " " + first_name)

# 6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)

# 7. Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White","Black"]
print(color_list[0],color_list[-1])

# 8. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
print("The examination will start from : %i / %i / %i"%exam_st_date)

# 9. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
a = int(input("Input an integer : "))
n1 = int("%s" % a)
n2 = int("%s%s" % (a,a))
n3 = int("%s%s%s" % (a,a,a))
print(n1+n2+n3)

# 10. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
print(abs.__doc__)

# 11. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.
import calendar
yy = int(input("Input the year : "))
mm = int(input("Input the month : "))
print(calendar.month(yy,mm))

# 12. Write a Python program to print the following here document.
print("""a string