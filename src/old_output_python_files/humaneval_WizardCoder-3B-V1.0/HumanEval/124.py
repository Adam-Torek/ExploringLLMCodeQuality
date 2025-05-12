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

# Solution:
def valid_date(date):
    if not date:
        return False

    date_list = date.split('-')
    if len(date_list)!= 3:
        return False

    month, day, year = int(date_list[0]), int(date_list[1]), int(date_list[2])

    if month < 1 or month > 12:
        return False

    if day < 1 or day > 31:
        if month in [4, 6, 9, 11]:
            return day >= 1 and day <= 30
        elif month == 2:
            return day >= 1 and day <= 29
        else:
            return False

    if year < 1000 or year > 9999:
        return False

    return True

# Test cases
print(valid_date('03-11-2000'))  # True
print(valid_date('15-01-2012'))  # False
print(valid_date('04-0-2040'))   # False
print(valid_date('06-04-2020'))  # True
print(valid_date('06/04/2020'))  # False<|endoftext|>