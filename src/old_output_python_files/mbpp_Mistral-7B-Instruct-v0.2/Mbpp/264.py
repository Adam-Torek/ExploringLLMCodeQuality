"""
Write a function to calculate a dog's age in dog's years.
assert dog_age(12)==61
"""
def dog_age(human_years):
    """
    Calculate a dog's age in dog years
    :param human_years: int, number of human years
    :return: int, number of dog years
    """
    dog_years = human_years * 7
    return dog_years

assert dog_age(12) == 61
assert dog_age(5) == 35
assert dog_age(1) == 7
assert dog_age(3) == 21
assert dog_age(8) == 56
assert dog_age(10) == 70
assert dog_age(15) == 105
assert dog_age(2) == 14
assert dog_age(7) == 49
assert dog_age(0) == 0