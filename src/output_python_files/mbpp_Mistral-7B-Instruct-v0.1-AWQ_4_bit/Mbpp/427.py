"""
Write a function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
assert change_date_format("2026-01-02") == '02-01-2026'
"""

def change_date_format(date):
    """
    Converts a date of yyyy-mm-dd format to dd-mm-yyyy format.
    """
    date_list = date.split('-')
    date_list.reverse()
    date_string = '-'.join(date_list)
    return date_string