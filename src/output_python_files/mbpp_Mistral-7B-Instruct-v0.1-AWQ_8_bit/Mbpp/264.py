"""
Write a function to calculate a dog's age in dog's years.
assert dog_age(12)==61
"""

def dog_age(human_age):
    """
    Calculate a dog's age in dog's years.
    """
    return human_age // 2


if __name__ == '__main__':
    assert dog_age(12) == 61