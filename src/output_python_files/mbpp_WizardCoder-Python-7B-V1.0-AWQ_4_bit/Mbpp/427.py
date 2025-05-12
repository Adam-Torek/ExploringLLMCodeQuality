"""
Write a function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
assert change_date_format("2026-01-02") == '02-01-2026'
"""

def change_date_format(date):
    year, month, day = date.split('-')
    return f"{day}-{month}-{year}"

print(change_date_format("2026-01-02")) # Output: 02-01-2026