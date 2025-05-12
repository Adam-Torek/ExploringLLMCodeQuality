"""
Write a function to calculate a dog's age in dog's years.
assert dog_age(12)==61
"""

def dog_age(age):
    return age * 7

print(dog_age(12))

"""
Write a function to calculate the number of seconds in a given number of hours.
assert seconds_in_hours(1)==3600
"""

def seconds_in_hours(hours):
    return hours * 3600

print(seconds_in_hours(1))

"""
Write a function to calculate the number of seconds in a given number of minutes.
assert seconds_in_minutes(1)==60
"""

def seconds_in_minutes(minutes):
    return minutes * 60

print(seconds_in_minutes(1))

"""
Write a function to calculate the number of seconds in a given number of days.
assert seconds_in_days(1)==86400
"""

def seconds_in_days(days):
    return days * 86400

print(seconds_in_days(1))

"""
Write a function to calculate the number of seconds in a given number of weeks.
assert seconds_in_weeks(1)==604800
"""

def seconds_in_weeks(weeks):
    return weeks * 604800

print(seconds_in_weeks(1))

"""
Write a function to calculate the number of seconds in a given number of years.
assert seconds_in_years(1)==31536000
"""

def seconds_in_years(years):
    return years * 31536000

print(seconds_in_years(1))

"""
Write a function to calculate the number of seconds in a given number of months.
assert seconds_in_months(1)==2628000
"""

def seconds_in_months(months):
    return months * 2628000

print(seconds_in_months(1))

"""
Write a function to calculate the number of seconds in a given number of seconds.
assert seconds_in_seconds(1)==1
"""

def seconds_in_seconds(seconds):
    return seconds

print(seconds_in_seconds(1))

"""
Write a function to calculate the number of seconds in a given number of milliseconds.
assert seconds_in_milliseconds(1)==0.001
"""

def seconds_in_milliseconds(milliseconds):
    return milliseconds / 1000

print(seconds_in_milliseconds(1))

"""
Write a function to calculate the number of seconds in a given number of microseconds.
assert seconds_in_microseconds(1)==0.000001
"""

def seconds_in_microseconds(microseconds):
    return microseconds / 1000000

print(seconds_in_microseconds(1))

"""
Write a function to calculate the number of seconds in a given number of nanoseconds.
assert seconds_in_nanoseconds(1)==0.000000001
"""

def seconds_in_nanoseconds(nanoseconds):
    return nanoseconds / 1000000000

print(seconds_in_nanoseconds(1))

"""
Write a function to calculate the number of seconds in a given number of picoseconds.
assert seconds_in_picoseconds(1)==0.000000000001
"""

def seconds_in_picoseconds(picoseconds):
    return picoseconds / 1000000000000

print(seconds_in_picoseconds(1))

"""
Write a function to calculate the number of seconds in a given number of femtoseconds.
assert seconds_in_femtoseconds(1)==0.000000000000001
"""