"""
Write a function to check whether the given month number contains 31 days or not.
assert check_monthnumb_number(5)==True
"""
def check_monthnumb_number(month):
    if month in [4,6,9,11]:
        return True
    elif month == 2:
        return (isinstance(year, int) and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0))
    else:
        return True

assert check_monthnumb_number(5)==True
assert check_monthnumb_number(2)==True
assert check_monthnumb_number(12)==True
assert check_monthnumb_number(3)==False
assert check_monthnumb_number(30)==False
assert check_monthnumb_number(2020)==False