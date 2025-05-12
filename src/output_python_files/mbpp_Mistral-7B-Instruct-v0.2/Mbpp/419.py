"""
Write a function to round every number of a given list of numbers and print the total sum multiplied by the length of the list.
assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])==243
"""
def round_and_sum(numbers):
    total = 0
    for number in numbers:
        number = round(number, 2)
        total += number
    return total * len(numbers)

assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]) == 243