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
    i = 0
    while i < len(string):
        if string[i].isdigit():
            numbers.append(string[i])
            i += 1
        else:
            if numbers:
                string = string[:i] + ''.join(numbers) + string[i:]
                numbers = []
            i += 1
    if numbers:
        string = string[:i] + ''.join(numbers) + string[i:]
    return string

if __name__ == "__main__":
    assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
    assert move_num('I love 12345 number 67890') == 'I lovenumber6789012345'
    assert move_num('I love 12345 number 67890.123') == 'I lovenumber67890.12312345'
    assert move_num('I love 12345 number 67890.123.456') == 'I lovenumber67890.123.45612345'
    assert move_num('I love 12345 number 67890.123.456.789') == 'I lovenumber67890.123.456.78912345'
    assert move_num('I love 12345 number 67890.123.456.789.123') == 'I lovenumber67890.123.456.789.12312345'
    assert move_num('I love 12345 number 67890.123.456.789.123.456') == 'I lovenumber67890.123.456.789.123.45612345'
    assert move_num('I love 12345 number 67890.123.456.789.123.456.789') == 'I lovenumber67890.123.456.789.123.456.78912345'
    assert move_num('I love 12345 number 67890.123.456.789.123.456.789.123') == 'I lovenumber67890.123.456.789.123.456.789.12312345'
    assert move_num('I love 12345 number 67890.123.456.789.123.456.789.123.123') == 'I lovenumber67890.123.456.789.123.456.789.123.12312345'
    assert move_num('I love 12345 number 67890.123.456.789.123.456.789.123.123.123') == 'I lovenumber67890.123.456.789.123.456.789.123.123.1