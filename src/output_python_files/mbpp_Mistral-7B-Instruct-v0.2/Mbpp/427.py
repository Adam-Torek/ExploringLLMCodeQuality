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
    day = date_parts[0]
    month = date_parts[1]
    year = date_parts[2]
    return f"{day}-{month}-{year}"

if __name__ == "__main__":
    assert change_date_format("2026-01-02") == '02-01-2026'
    print("Test passed!")