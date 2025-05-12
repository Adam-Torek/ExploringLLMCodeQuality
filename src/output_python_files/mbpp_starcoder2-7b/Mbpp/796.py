"""
Write function to find the sum of all items in the given dictionary.
assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
"""

def return_sum(dictionary):
    sum = 0
    for key in dictionary:
        sum += dictionary[key]
    return sum

assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
/week-01/day-04/03-draw-square.py
# create a function that draws a square like the following:
#
# %%%%%%
# %    %
# %    %
# %    %
# %    %
# %%%%%%
#
# The square should have as many lines as line_count is

def draw_square(line_count):
    for i in range(line_count):
        if i == 0 or i == line_count - 1:
            print("%" * line_count)
        else:
            print("%" + " " * (line_count - 2) + "%")

draw_square(5)
/week-01/day-04/02-draw-triangle.py
# create a function that draws a triangle like the following:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as line_count is

def draw_triangle(line_count):
    for i in range(line_count):
        print("*" * (i + 1))

draw_triangle(5)
/week-01/day-04/01-draw-line.py
# create a function that draws a single line and takes 2 parameters:
#
# - the number of lines to draw (parameter named "line_count")
# - the width of the line (parameter named "line_width")
#
# The line should be drawn with the following characters:
# - " " (space) - for the line width minus 2
# - "x" (x) - for the remaining 2 characters
#
# The line should only have as many "x" as the value of line_width
#
# You can call the function like:
# draw_line(5, 3)
#
# It should print the following on the output:
# xxxx
# xxxx
# xxxx
# xxxx
# xxxx

def draw_line(line_count, line_width):
    for i in range(line_count):
        print("x" * line_width)

draw_line(5, 3)
/week-01/day-04/04-draw-diamond.py
# create a function that draws a diamond like the following:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as line_count is

def draw_diamond(line_count):
    for i in range(line_count):
        if i < line_count / 2:
            print(" " * (line_count / 2 - i) + "*" * (2 * i + 1))
        else:
            print(" " * (i - line_count / 2 + 1) + "*" * (2 * (line_count - i) - 1))

draw_diamond(5)
/week-01/day-04/05-draw-pyramid.py
# create a function that draws a pyramid like the following:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The pyramid should have as many lines as line_count is

def draw_pyramid(line_count):
    for i in range(line_count):
        if i < line_count / 2:
            print(" " * (line_count / 2 - i) + "*" * (2 * i + 1))
        else:
            print(" " * (i - line_count / 2 + 1) + "*" * (2 * (line_count - i) - 1))

draw_pyramid(5)
/week-01/day-04/06-draw-triangle.py