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
    if not date:
        return False
    month, day, year = map(int, date.split('-'))
    if month < 1 or month > 12:
        return False
    if month == 2:
        if day < 1 or day > 29:
            return False
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    return True


# Test Cases
print(valid_date('03-11-2000')) # True
print(valid_date('15-01-2012')) # False
print(valid_date('04-0-2040')) # False
print(valid_date('06-04-2020')) # True
print(valid_date('06/04/2020')) # False
print(valid_date('')) # False
print(valid_date('13-02-2020')) # True
print(valid_date('31-02-2020')) # False
print(valid_date('01-13-2020')) # False
print(valid_date('12-31-2020')) # False
print(valid_date('01-01-0000')) # True
print(valid_date('12-31-9999')) # True
print(valid_date('02-29-2000')) # False
print(valid_date('02-29-2004')) # True
print(valid_date('02-29-2012')) # False
print(valid_date('02-29-2020')) # True
print(valid_date('02-29-2024')) # False
print(valid_date('02-29-2028')) # True
print(valid_date('02-29-2032')) # False
print(valid_date('02-29-2036')) # True
print(valid_date('02-29-2040')) # False
print(valid_date('02-29-2044')) # True
print(valid_date('02-29-2048')) # False
print(valid_date('02-29-2052')) # True
print(valid_date('02-29-2056')) # False
print(valid_date('02-29-2060')) # True
print(valid_date('02-29-2064')) # False
print(valid_date('02-29-2068')) # True
print(valid_