"""
Write a python function to find the first digit of a given number.
assert first_Digit(123) == 1
"""

def first_Digit(num):
    """
    This function takes a number as an input and returns the first digit of the number.
    """
    num = abs(num)
    while num >= 10:
        num = num // 10
    return num


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(first_Digit(num))