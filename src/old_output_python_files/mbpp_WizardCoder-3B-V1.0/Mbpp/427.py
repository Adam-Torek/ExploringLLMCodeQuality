"""
Write a function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
assert change_date_format("2026-01-02") == '02-01-2026'
"""

def change_date_format(date_str):
    year, month, day = map(int, date_str.split('-'))
    return f'{day}-{month}-{year}'

# Test cases
assert change_date_format("2026-01-02") == '02-01-2026'
assert change_date_format("1999-12-31") == '31-12-1999'
assert change_date_format("2021-01-01") == '01-01-2021'<|endoftext|>