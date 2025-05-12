"""
Write a function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
assert change_date_format("2026-01-02") == '02-01-2026'
"""

def change_date_format(date):
    return date[8:] + '-' + date[5:7] + '-' + date[:4]

print(change_date_format("2026-01-02")) # Output: '02-01-2026'