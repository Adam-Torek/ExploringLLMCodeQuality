"""
Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.
assert odd_Equivalent("011001",6) == 3
"""
def odd_Equivalent(binary_string:str, rotation:int)->int:
    """
    Function to find the number of odd values when rotating a binary string the given number of times.
    :param binary_string: str, binary string to rotate
    :param rotation: int, number of times to rotate the binary string
    :return: int, number of odd values in the binary string after rotation
    """
    binary_string = binary_string.zfill(len(binary_string) + rotation) # Pad the binary string with zeros to the left to make the length equal to the length after rotation
    binary_list = list(map(int, binary_string)) # Convert binary string to list of integers
    odd_count = 0 # Initialize odd count to zero
    for i in binary_list: # Iterate through each integer in the list
        if i % 2 != 0: # If the integer is odd
            odd_count += 1 # Increment odd count
    return odd_count # Return the odd count

assert odd_Equivalent("011001",6) == 3 # Test case passes