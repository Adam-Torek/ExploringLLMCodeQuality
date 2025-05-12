"""
Write a function to create a new tuple from the given string and list.
assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
"""


def new_tuple(list_of_str, str_of_str):
    """
    Create a new tuple from the given string and list.
    :param list_of_str: list of strings
    :param str_of_str: string of strings
    :return: tuple
    """
    return tuple(list_of_str + [str_of_str])


if __name__ == '__main__':
    print("Example:")
    print(new_tuple(["WEB", "is"], "best"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
    assert new_tuple(["WEB", "is", "awesome"], "best") == ('WEB', 'is', 'awesome', 'best')
    assert new_tuple(["WEB", "is", "awesome", "and"], "simple") == ('WEB', 'is', 'awesome', 'and', 'simple')
    assert new_tuple(["WEB", "is", "awesome", "and", "simple"], "easy") == ('WEB', 'is', 'awesome', 'and', 'simple', 'easy')
    assert new_tuple(["WEB", "is", "awesome", "and", "simple", "to", "use"], "easy") == ('WEB', 'is', 'awesome', 'and', 'simple', 'to', 'use', 'easy')
    assert new_tuple(["WEB", "is", "awesome", "and", "simple", "to", "use", "and", "easy"], "too") == ('WEB', 'is', 'awesome', 'and', 'simple', 'to', 'use', 'and', 'easy', 'too')
    assert new_tuple(["WEB", "is", "awesome", "and", "simple", "to", "use", "and", "easy", "too"], "great") == ('WEB', 'is', 'awesome', 'and', 'simple', 'to', 'use', 'and', 'easy', 'too', 'great')
    assert new_tuple(["WEB", "is", "awesome", "and", "simple", "to", "use", "and", "easy", "too", "great"], "!") == ('WEB', 'is', 'awesome', 'and', 'simple', 'to', 'use', 'and', 'easy', 'too', 'great', '!')
    assert new_tuple(["WEB", "is", "awesome", "and", "simple", "to", "use", "and", "easy", "too", "great", "!"], "!") == ('WEB', 'is', 'awesome', 'and', 'simple', 'to', 'use', 'and', 'easy', 'too', 'great', '!', '!')
    assert new_tuple(["WEB", "is", "awesome", "and", "simple", "to", "use", "and", "easy", "too", "great", "!", "!"], "!") == ('WEB', 'is', 'awesome', 'and', 'simple', 'to', 'use', 'and', 'easy', 'too', 'great', '!', '!', '!')
    assert new_tuple(["WEB", "is", "awesome", "and", "simple", "to", "use", "and", "easy", "too", "great", "!", "!", "!"], "!") == ('WEB', 'is', 'awesome', 'and', 'simple', 'to', 'use', 'and', 'easy', 'too', 'great', '!', '!', '!', '!')
    assert new_tuple(["WEB", "is", "awesome", "and", "simple", "to", "use", "and", "easy", "too", "great", "!", "!", "