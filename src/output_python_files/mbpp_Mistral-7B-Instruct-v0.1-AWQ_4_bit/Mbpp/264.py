"""
Write a function to calculate a dog's age in dog's years.
assert dog_age(12)==61
"""

def dog_age(human_age):
    """
    Calculate a dog's age in dog's years.
    """
    if human_age < 1:
        return 0
    elif human_age < 13:
        return human_age * 10 / 7
    else:
        return human_age * 10 / 6


if __name__ == '__main__':
    assert dog_age(12) == 61