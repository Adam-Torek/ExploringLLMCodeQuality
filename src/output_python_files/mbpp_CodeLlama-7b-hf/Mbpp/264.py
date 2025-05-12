"""
Write a function to calculate a dog's age in dog's years.
assert dog_age(12)==61
"""


def dog_age(age):
    """
    Calculate a dog's age in dog's years.
    :param age: age of the dog
    :return: age of the dog in dog's years
    """
    return age * 7


def test_dog_age():
    assert dog_age(12) == 61


if __name__ == '__main__':
    test_dog_age()