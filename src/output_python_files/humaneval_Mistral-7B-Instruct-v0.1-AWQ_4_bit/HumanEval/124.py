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
    date_list = date.split('-')
    if len(date_list) != 3:
        return False
    month = int(date_list[0])
    day = int(date_list[1])
    year = int(date_list[2])
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        if month in [1,3,5,7,8,10,12]:
            return False
        elif month in [4,6,9,11]:
            return False
        else:
            return False
    if year < 1900 or year > 2100:
        return False
    if month == 2:
        if day > 29:
            return False
    return True


def main():
    date_list = ['03-11-2000', '15-01-2012', '04-0-2040', '06-04-2020', '06/04/2020', '01-01-2000', '02-29-2000', '02-28-2000', '02-27-2000']
    for date in date_list:
        print(f"{date}: {valid_date(date)}")


if __name__ == "__main__":
    main()