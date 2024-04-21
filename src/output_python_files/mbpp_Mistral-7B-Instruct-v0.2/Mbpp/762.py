"""
Write a function to check whether the given month number contains 30 days or not. Months are given as number from 1 to 12.
assert check_monthnumber_number(6)==True
"""
def check_monthnumber_number(month):
    if month in [4, 6, 9, 11]:
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
        return False

# Test the function
assert check_monthnumber_number(6) == True
assert check_monthnumber_number(2) == True
assert check_monthnumber_number(12) == True
assert check_monthnumber_number(3) == False
assert check_monthnumber_number(29) == False
assert check_monthnumber_number(0) == False
assert check_monthnumber_number(13) == False</s>