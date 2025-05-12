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