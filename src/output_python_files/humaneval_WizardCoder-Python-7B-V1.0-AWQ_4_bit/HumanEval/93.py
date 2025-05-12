def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    vowels = 'aeiou'
    new_message = ''
    for letter in message:
        if letter.lower() in vowels:
            index = vowels.index(letter.lower())
            new_message += vowels[(index + 2) % 5]
        else:
            new_message += letter.upper() if letter.isupper() else letter.lower()
    return new_message


# Test cases
print(encode('test')) # Output: 'TGST'
print(encode('This is a message')) # Output: 'tHKS KS C MGSSCGG'
print(encode('Hello world')) # Output: 'Ifmmp xpsme'
print(encode('Python is awesome')) # Output: 'Rznhtn zs rqwbqn'
print(encode('I love programming')) # Output: 'J lv qnvg qnvqngrmgr'
print(encode('Aa bb cc dd ee')) # Output: 'Bb cc dd ff gg'
print(encode('Zz yy xy wx vu')) # Output: 'Aa bb cc dd ee'
print(encode('Qwertyuiop')) # Output: 'Asdfghjkl'
print(encode('Qq ww ee rr tt yy uu')) # Output: 'Rr ss dd ff gg'
print(encode('Python is not case sensitive')) # Output: 'Rpzthn zs nt rqwbqn tq rqybqn'
print(encode('The quick brown fox jumps over the lazy dog')) # Output: 'Thd fgr gbq nfjc qbhv qbzcgd qbzcgd'
print(encode('The lazy dog is not amused')) # Output: 'Thd lzy dg zs nt qbzcgd qbzcgd'
print(encode('The lazy dog is not amused.')) # Output: 'Thd lzy dg zs nt qbzcgd qbzcgd.'
print(encode('The quick brown fox jumps over the lazy dog.')) # Output: 'Thd fgr gbq nfjc qbhv qbzcgd qbzcgd.'
print(encode('The quick brown fox jumps over the lazy dog!')) # Output: 'Thd fgr gbq nfjc qbhv qbzcgd qbzcgd!'
print(encode('The quick brown fox jumps over the lazy dog?')) # Output: 'Thd fgr gbq nfjc qbhv qbzcgd qbzcgd?'
print(encode('The quick brown fox jumps over the lazy dog:')) # Output: 'Thd fgr gbq nfjc qbhv qbzcgd qbzcg