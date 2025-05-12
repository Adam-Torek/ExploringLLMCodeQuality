def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    '''

# Write your code here

# Test your code
print(triangle_area(3, 4, 5))
print(triangle_area(1, 2, 10))

# + [markdown] id="79612410"
# ## Exercise 3:
#
# Write a function that takes a list of numbers and returns the largest number in the list.
#
# Example:
#
# ```
# largest_number([1, 2, 3, 4, 5]) == 5
# largest_number([5, 4, 3, 2, 1]) == 5
# largest_number([100, 1000, 10000]) == 10000
# ```

# + id="18567087"
# Write your code here

# Test your code
print(largest_number([1, 2, 3, 4, 5]))
print(largest_number([5, 4, 3, 2, 1]))
print(largest_number([100, 1000, 10000]))


# + [markdown] id="18567087"
# ## Exercise 4:
#
# Write a function that takes a list of numbers and returns the smallest number in the list.
#
# Example:
#
# ```
# smallest_number([1, 2, 3, 4, 5]) == 1
# smallest_number([5, 4, 3, 2, 1]) == 1
# smallest_number([100, 1000, 10000]) == 100
# ```

# + id="18567087"
# Write your code here

# Test your code
print(smallest_number([1, 2, 3, 4, 5]))
print(smallest_number([5, 4, 3, 2, 1]))
print(smallest_number([100, 1000, 10000]))


# + [markdown] id="18567087"
# ## Exercise 5:
#
# Write a function that takes a list of numbers and returns the average of the numbers in the list.
#
# Example:
#
# ```
# average([1, 2, 3, 4, 5]) == 3.0
# average([5, 4, 3, 2, 1]) == 3.0
# average([100, 1000, 10000]) == 4000.0
# ```

# + id="18567087"
# Write your code here

# Test your code
print(average([1, 2, 3, 4, 5]))
print(average([5, 4, 3, 2, 1]))
print