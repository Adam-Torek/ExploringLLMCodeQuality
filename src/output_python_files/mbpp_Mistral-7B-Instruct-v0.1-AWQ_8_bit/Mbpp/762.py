"""
Write a function to check whether the given month number contains 30 days or not. Months are given as number from 1 to 12.
assert check_monthnumber_number(6)==True
"""

def check_monthnumber_number(month):
    if month in [1,3,5,7,8,10,12]:
        return True
    else:
        return False