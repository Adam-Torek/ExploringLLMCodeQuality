"""
Write a function to check whether the given month number contains 31 days or not.
assert check_monthnumb_number(5)==True
"""
def check_monthnumb_number(month):
    if month in [4,6,9,11]:
        return True
    elif month == 2:
        is_leap_year = False
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            is_leap_year = True
        if is_leap_year:
            return True
        else:
            return False
    else:
        return 31 in [31,len(calendar.month(year,month)) for year in range(2000,2050)]

# test case
assert check_monthnumb_number(5)==True
assert check_monthnumb_number(2)==True
assert check_monthnumb_number(12)==True
assert check_monthnumb_number(3)==False
assert check_monthnumb_number(13)==False
assert check_monthnumb_number(100)==False
assert check_monthnumb_number(2000)==False
assert check_monthnumb_number(2004)==True
assert check_monthnumb_number(2012)==True
assert check_monthnumb_number(2020)==True