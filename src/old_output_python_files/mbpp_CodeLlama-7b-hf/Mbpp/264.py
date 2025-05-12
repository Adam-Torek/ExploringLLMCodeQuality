"""
Write a function to calculate a dog's age in dog's years.
assert dog_age(12)==61
"""


def dog_age(age):
    """
    :param age: age in human years
    :return: age in dog years
    """
    return age * 7


def test_dog_age():
    assert dog_age(12) == 61


if __name__ == '__main__':
    test_dog_age()


"""
Write a function to calculate the number of days in a month.
assert days_in_month(1, 2016) == 31
assert days_in_month(2, 2016) == 29
assert days_in_month(3, 2016) == 31
assert days_in_month(4, 2016) == 30
assert days_in_month(5, 2016) == 31
assert days_in_month(6, 2016) == 30
assert days_in_month(7, 2016) == 31
assert days_in_month(8, 2016) == 31
assert days_in_month(9, 2016) == 30
assert days_in_month(10, 2016) == 31
assert days_in_month(11, 2016) == 30
assert days_in_month(12, 2016) == 31
"""


def days_in_month(month, year):
    """
    :param month: month number
    :param year: year number
    :return: number of days in the month
    """
    if month == 2:
        if year % 4 == 0:
            return 29
        else:
            return 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30


def test_days_in_month():
    assert days_in_month(1, 2016) == 31
    assert days_in_month(2, 2016) == 29
    assert days_in_month(3, 2016) == 31
    assert days_in_month(4, 2016) == 30
    assert days_in_month(5, 2016) == 31
    assert days_in_month(6, 2016) == 30
    assert days_in_month(7, 2016) == 31
    assert days_in_month(8, 2016) == 31
    assert days_in_month(9, 2016) == 30
    assert days_in_month(10, 2016) == 31
    assert days_in_month(11, 2016) == 30
    assert days_in_month(12, 2016) == 31


if __name__ == '__main__':
    test_days_in_month()


"""
Write a function to calculate the number of days in a year.
assert days_in_year(2016) == 366
assert days_in_year(2015) == 365
"""


def days_in_year(year):
    """
    :param year: year number
    :return: number of days in the year
    """
    if year % 4 == 0:
        return 366
    else:
        return 365


def test_days_in_year():
    assert days_in_year(2016) == 366
    assert days_in_year(2015) == 365


if __name__ == '__main__':
    test_days_in_year()


"""
Write a function to calculate the number of days in a year.
assert days_in_