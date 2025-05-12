def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    words = s.split()
    result = []
    for word in words:
        if word.isalpha():
            result.append(''.join(sorted(word)))
        else:
            result.append(word)
    return ' '.join(result)



def test_anti_shuffle():
    assert anti_shuffle('Hi') == 'Hi'
    assert anti_shuffle('hello') == 'ehllo'
    assert anti_shuffle('Hello World!!!') == 'Hello !!!Wdlor'
    assert anti_shuffle('Python is awesome') == 'Python aei ssw'
    assert anti_shuffle('This is a test') == 'This a ehts si'
    assert anti_shuffle('The quick brown fox jumps over the lazy dog') == 'The aecb fijwkxo nopr stv'
    assert anti_shuffle('The quick brown fox jumps over the lazy dog') == 'The aecb fijwkxo nopr stv'
    assert anti_shuffle('The quick brown fox jumps over the lazy dog') == 'The aecb fijwkxo nopr stv'
    assert anti_shuffle('The quick brown fox jumps over the lazy dog') == 'The aecb fijwkxo nopr stv'
    assert anti_shuffle('The quick brown fox jumps over the lazy dog') == 'The aecb fijwkxo nopr stv'
    assert anti_shuffle('The quick brown fox jumps over the lazy dog') == 'The aecb fijwkxo nopr stv'
    assert anti_shuffle('The quick brown fox jumps over the lazy dog') == 'The aecb fijwkxo nopr stv'
    assert anti_shuffle('The quick brown fox jumps over the lazy dog') == 'The aecb fijwkxo nopr stv'
    assert anti_shuffle('The quick brown fox jumps over the lazy dog') == 'The aecb fijwkxo nopr stv'
    assert anti_shuffle('The quick brown fox jumps over the lazy dog') == 'The aecb fijwkxo nopr stv'
    assert anti_shuffle('The quick brown fox jumps over the lazy dog') == 'The aecb fijwkxo nopr stv'
    assert anti_shuffle('The quick brown fox jumps over the lazy dog') == 'The aecb fijwkxo nopr stv'
    assert anti_shuffle('The quick brown fox jumps over the lazy dog') == 'The aecb fijwkxo nopr stv'
    assert anti_shuffle('The quick brown fox jumps over the lazy dog') == 'The aecb fijwkxo nopr stv'
    assert anti_shuffle('The quick brown fox jumps over the lazy dog') == 'The aecb fijwkxo nopr stv'
    assert anti_shuffle('The quick brown fox jumps over the lazy dog') == 'The aecb fijwkxo nopr stv'
    assert anti_shuffle('The quick brown fox jumps over the lazy dog') == 'The aecb fijwkxo nopr stv'
    assert anti_shuffle('The quick brown fox jumps over the lazy dog') == 'The aecb fijwkxo nopr stv'
    assert anti_shuffle('The quick brown fox jumps over the lazy dog') == '