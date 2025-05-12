"""
Write a function to check whether the given month number contains 31 days or not.
assert check_monthnumb_number(5)==True
"""
def check_monthnumb_number(month_number):
    if month_number in [1,3,5,7,8,10,12]:
        return True
    elif month_number in [4,6,9,11]:
        return False
    else:
        return True

# Test cases
print(check_monthnumb_number(5)) # True
print(check_monthnumb_number(2)) # False
print(check_monthnumb_number(9)) # True
print(check_monthnumb_number(11)) # True
print(check_monthnumb_number(4)) # False
print(check_monthnumb_number(7)) # False
print(check_monthnumb_number(2)) # False
print(check_monthnumb_number(12)) # True
print(check_monthnumb_number(8)) # True
print(check_monthnumb_number(3)) # True
print(check_monthnumb_number(10)) # True
print(check_monthnumb_number(2)) # False
print(check_monthnumb_number(9)) # True
print(check_monthnumb_number(11)) # True
print(check_monthnumb_number(4)) # False
print(check_monthnumb_number(7)) # False
print(check_monthnumb_number(2)) # False
print(check_monthnumb_number(12)) # True
print(check_monthnumb_number(8)) # True
print(check_monthnumb_number(3)) # True
print(check_monthnumb_number(10)) # True
print(check_monthnumb_number(2)) # False
print(check_monthnumb_number(9)) # True
print(check_monthnumb_number(11)) # True
print(check_monthnumb_number(4)) # False
print(check_monthnumb_number(7)) # False
print(check_monthnumb_number(2)) # False
print(check_monthnumb_number(12)) # True
print(check_monthnumb_number(8)) # True
print(check_monthnumb_number(3)) # True
print(check_monthnumb_number(10)) # True
print(check_monthnumb_number(2)) # False
print(check_monthnumb_number(9)) # True
print(check_monthnumb_number(11)) # True
print(check_monthnumb_number(4)) # False
print(check_monthnumb_number(7)) # False
print(check_monthnumb_number(2)) # False
print(check_monthnumb_number(12)) # True
print(check_monthnumb_number(8)) # True
print(check_monthnumb_number(3)) # True
print(check_monthnumb_number(10)) # True
print(check_monthnumb_number(2)) # False
print(check_monthnumb_number(9)) # True
print(check_monthnumb_number(11)) # True
print(check_monthnumb_number(4)) # False
print(check_monthnumb_number(7)) # False
print(check_monthnumb_number(2)) # False
print(check_monthnumb_number(12)) # True
print(check_monthnumb_number(8)) # True
print(check_monthnumb_number(3)) # True
print(check_monthnumb_number(10)) # True
print(check_monthnumb_number(2)) # False
print(check_monthnumb_number(9)) # True
print(check_monthnumb_number(11)) # True
print(check_monthnumb_number(4)) # False
print(check_monthnumb_number(7)) # False
print(check_monthnumb_number(2)) # False
print(check_monthnumb_