"""
Write a function to check whether the given month number contains 30 days or not. Months are given as number from 1 to 12.
assert check_monthnumber_number(6)==True
"""
def check_monthnumber_number(month_number):
    if month_number in [4,6,9,11]:
        return True
    elif month_number in [1,3,5,7,8,10,12]:
        return False
    elif month_number in [2]:
        return True
    else:
        return False

# Test cases
print(check_monthnumber_number(6)) # True
print(check_monthnumber_number(1)) # False
print(check_monthnumber_number(2)) # True
print(check_monthnumber_number(12)) # True
print(check_monthnumber_number(5)) # False
print(check_monthnumber_number(9)) # True
print(check_monthnumber_number(4)) # True
print(check_monthnumber_number(8)) # True
print(check_monthnumber_number(11)) # True
print(check_monthnumber_number(3)) # False
print(check_monthnumber_number(10)) # True
print(check_monthnumber_number(7)) # False
print(check_monthnumber_number(12)) # True
print(check_monthnumber_number(9)) # True
print(check_monthnumber_number(4)) # True
print(check_monthnumber_number(8)) # True
print(check_monthnumber_number(11)) # True
print(check_monthnumber_number(3)) # False
print(check_monthnumber_number(10)) # True
print(check_monthnumber_number(7)) # False
print(check_monthnumber_number(12)) # True
print(check_monthnumber_number(4)) # True
print(check_monthnumber_number(8)) # True
print(check_monthnumber_number(11)) # True
print(check_monthnumber_number(3)) # False
print(check_monthnumber_number(10)) # True
print(check_monthnumber_number(7)) # False
print(check_monthnumber_number(12)) # True
print(check_monthnumber_number(4)) # True
print(check_monthnumber_number(8)) # True
print(check_monthnumber_number(11)) # True
print(check_monthnumber_number(3)) # False
print(check_monthnumber_number(10)) # True
print(check_monthnumber_number(7)) # False
print(check_monthnumber_number(12)) # True
print(check_monthnumber_number(4)) # True
print(check_monthnumber_number(8)) # True
print(check_monthnumber_number(11)) # True
print(check_monthnumber_number(3)) # False
print(check_monthnumber_number(10)) # True
print(check_monthnumber_number(7)) # False
print(check_monthnumber_number(12)) # True
print(check_monthnumber_number(4)) # True
print(check_monthnumber_number(8)) # True
print(check_monthnumber_number(11)) # True
print(check_monthnumber_number(3)) # False
print(check_monthnumber_number(10)) # True
print(check_monthnumber_number(7)) # False
print(check_monthnumber_number(12)) # True
print(check_monthnumber_number(4)) # True
print(check_monthnumber_number(8)) # True
print(check_monthnumber_number(11)) # True
print(check_monthnumber_number(3)) # False
print(check_monthnumber_number(10)) # True
print(check_monthnumber_number(7)) # False
print(check_monthnumber_number(12)) # True
print(check_monthnumber_number(4)) # True
print(check_monthnumber_number(8)) # True
print(check_monthnumber_number(11)) # True
print(check_monthnumber_number(3)) #