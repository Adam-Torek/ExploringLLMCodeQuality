"""
Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.
assert odd_Equivalent("011001",6) == 3
"""
def odd_Equivalent(binary_string:str, rotation:int)->int:
    """
    This function takes a binary string and the number of rotations as input and returns the number of odd values in the binary string after the given number of rotations.

    Parameters:
    binary_string: str - A binary string to be rotated.
    rotation: int - The number of rotations to be applied to the binary string.

    Returns:
    int - The number of odd values in the binary string after the given number of rotations.
    """
    # Convert the binary string to a list of integers
    binary_list = list(map(int, list(binary_string)))

    # Rotate the list by the given number of positions
    for _ in range(rotation):
        first = binary_list.pop()
        binary_list.append(first)

    # Count the number of odd values in the list
    odd_count = sum(1 for num in binary_list if num % 2 != 0)

    return odd_count