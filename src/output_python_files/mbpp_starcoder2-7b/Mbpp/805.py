"""
Write a function that returns the list in a list of lists whose sum of elements is the highest.
assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]
"""

def max_sum_list(list_of_lists):
    max_sum = 0
    max_list = []
    for list in list_of_lists:
        sum = 0
        for element in list:
            sum += element
        if sum > max_sum:
            max_sum = sum
            max_list = list
    return max_list

print(max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]))
/week-02/day-03/02-draw-square.py
# create a function that draws a square like the following:
# %%%%%%
# %    %
# %    %
# %    %
# %    %
# %%%%%%

def draw_square(size):
    for i in range(size):
        if i == 0 or i == size - 1:
            print("%" * size)
        else:
            print("%" + " " * (size - 2) + "%")

draw_square(5)
/week-03/day-02/02-count-lines.py
"""
Write a function that takes a filename as string,
then returns the number of lines the file contains.
It should return zero if it can't open the file, and
should not raise any error.
"""

def count_lines(filename):
    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        return len(lines)
    except:
        return 0

print(count_lines("02-count-lines.py"))
/week-02/day-03/03-draw-triangle.py
# create a function that draws a triangle like the following:
#
# *
# **
# ***
# ****
# *****
#
# The triangle should have as many lines as lineCount is

def draw_triangle(line_count):
    for i in range(line_count):
        print("*" * (i + 1))

draw_triangle(5)
/week-02/day-03/01-draw-diamond.py
# create a function that draws a diamond like the following:
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as lineCount is

def draw_diamond(line_count):
    for i in range(line_count):
        if i < line_count / 2:
            print(" " * (line_count / 2 - i - 1) + "*" * (2 * i + 1))
        else:
            print(" " * (i - line_count / 2 + 1) + "*" * (2 * (line_count - i) - 1))

draw_diamond(5)
/week-02/day-03/04-draw-pyramid.py
# create a function that draws a pyramid like the following:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as lineCount is

def draw_pyramid(line_count):
    for i in range(line_count):
        print(" " * (line_count - i - 1) + "*" * (2 * i + 1))

draw_pyramid(5)
/week-02/day-03/05-draw-checkerboard.py
# create a function that draws a chess table like the following
# without using any loop
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %

def draw_checkerboard(size):
    for i in range(size):
        if i % 2 == 0:
            print("%" + " " * (size - 1) + "%