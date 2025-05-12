"""
Write a function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
assert change_date_format("2026-01-02") == '02-01-2026'
"""


def change_date_format(date):
    """
    >>> change_date_format("2026-01-02")
    '02-01-2026'
    """
    return "-".join(reversed(date.split("-")))


if __name__ == "__main__":
    import doctest

    doctest.testmod()