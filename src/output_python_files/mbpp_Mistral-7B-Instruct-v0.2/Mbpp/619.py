"""
Write a function to move all the numbers to the end of the given string.
assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
"""
def move_num(string):
    """
    :param string: string
    :return: string
    """
    numbers = []
    for char in string:
        if char.isdigit():
            numbers.append(char)
        else:
            if numbers:
                string = string[:string.index(numbers[0])] + string[string.index(numbers[0]):]
                string = string[:string.index(numbers[0])] + ''.join(numbers) + string[string.index(numbers[0]):]
                numbers = []
    if numbers:
        string = string[:string.index(numbers[0])] + ''.join(numbers) + string[string.index(numbers[0]):]
    return string

assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
assert move_num('I love 12345 you 67890') == 'I love you 6789012345'
assert move_num('I love 123 you 456') == 'I love you 456123'
assert move_num('I love you') == 'I love you'
assert move_num('') == ''
assert move_num('123') == '123'
assert move_num('1234567890') == '1234567890'
assert move_num('12345678901234567890') == '12345678901234567890'
assert move_num('123456789012345678901234567890') == '123456789012345678901234567890'
assert move_num('1234567890123456789012345678901234567890') == '1234567890123456789012345678901234567890'
assert move_num('12345678901234567890123456789012345678901234567890') == '12345678901234567890123456789012345678901234567890'
assert move_num('12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234