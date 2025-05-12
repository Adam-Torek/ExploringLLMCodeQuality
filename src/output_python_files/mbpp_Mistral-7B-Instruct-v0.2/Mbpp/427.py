"""
Write a function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
assert change_date_format("2026-01-02") == '02-01-2026'
"""
def change_date_format(date):
    """
    :param date: string in yyyy-mm-dd format
    :return: string in dd-mm-yyyy format
    """
    date_parts = date.split('-')
    day, month, year = date_parts
    return f"{day}-{month}-{year}"

if __name__ == "__main__":
    assert change_date_format("2026-01-02") == '02-01-2026'
    assert change_date_format("2022-12-31") == '31-12-2022'
    assert change_date_format("2019-05-15") == '15-05-2019'