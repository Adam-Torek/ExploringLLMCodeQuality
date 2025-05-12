def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    """
    try:
        month, day, year = map(int, date.split('-'))
    except ValueError:
        return False

    if len(date) != 10 or not date.endswith('-') or not date.startswith('-'):
        return False

    if not (1 <= month <= 12) or not (1 <= day <= 31):
        return False

    if month in [1, 3, 5, 7, 8, 10, 12] and not (1 <= day <= 31):
        return False
    elif month in [4, 6, 9, 11] and not (1 <= day <= 30):
        return False
    elif month == 2 and not (1 <= day <= 29):
        return False
    elif month == 2 and year % 4 == 0 and (year % 100 == 0 and year % 400 != 0) or year % 4 != 0:
        return False
    elif month == 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) and not (1 <= day <= 29):
        return False

    return True



# Test cases
print(valid_date('03-11-2000'))  # True
print(valid_date('15-01-2012'))  # False
print(valid_date('06-04-2020'))  # True
print(valid_date('06/04/2020'))  # False
print(valid_date('03-11-20000'))  # False
print(valid_date('02-29-2020'))  # True
print(valid_date('02-29-2021'))  # False
print(valid_date('02-29-2024'))  # False
print(valid_date('02-29-2024'))  # False
print(valid_date('02-29-2024'))  # False
print(valid_date('02-29-2024'))  # False
print(valid_date('02-29-2024'))  # False
print(valid_date('02-29-2024'))  # False
print(valid_date('02-29-2024'))  # False
print(valid_date('02-29-2024'))  # False
print(valid_date('02-29-2024'))  # False
print(valid_date('02-29-2024'))  # False
print(valid_date('02-29-2024'))  # False
print(valid_date('02-29-2024'))  # False
print(valid_date('02-29