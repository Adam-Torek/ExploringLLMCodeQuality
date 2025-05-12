"""
Write a function to check whether the given month number contains 30 days or not. Months are given as number from 1 to 12.
assert check_monthnumber_number(6)==True
"""
def check_monthnumber_number(month):
    if month in [4, 6, 9, 11]:
        return True
    elif month == 2:
        return (isinstance(year, int) and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0))
    else:
        return False

# Testing the function
assert check_monthnumber_number(6) == True
assert check_monthnumber_number(2) == True
assert check_monthnumber_number(13) == False
assert check_monthnumber_number(2000) == True
assert check_monthnumber_number(2001) == False