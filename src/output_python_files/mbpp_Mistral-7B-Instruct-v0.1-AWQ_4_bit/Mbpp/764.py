"""
Write a python function to count number of digits in a given string.
assert number_ctr('program2bedone') == 1
"""

def number_ctr(string):
    count = 0
    for i in string:
        if i.isdigit():
            count += 1
    return count

#assert number_ctr('program2bedone') == 1
#print(number_ctr('program2bedone'))