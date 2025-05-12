"""
Write a function to replace whitespaces with an underscore and vice versa in a given string.
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
"""


def replace_spaces(string):
    """
    Replace whitespaces with an underscore and vice versa in a given string.
    """
    return string.replace(' ', '_').replace('_', ' ')


if __name__ == '__main__':
    print(replace_spaces('Jumanji The Jungle'))
    print(replace_spaces('Jumanji_The_Jungle'))
    print(replace_spaces('Jumanji_The_Jungle_'))
    print(replace_spaces('Jumanji_The_Jungle_ '))
    print(replace_spaces('Jumanji_The_Jungle_  '))
    print(replace_spaces('Jumanji_The_Jungle_  _'))
    print(replace_spaces('Jumanji_The_Jungle_  _ '))
    print(replace_spaces('Jumanji_The_Jungle_  _  '))
    print(replace_spaces('Jumanji_The_Jungle_  _  _'))
    print(replace_spaces('Jumanji_The_Jungle_  _  _ '))
    print(replace_spaces('Jumanji_The_Jungle_  _  _  '))
    print(replace_spaces('Jumanji_The_Jungle_  _  _  _'))
    print(replace_spaces('Jumanji_The_Jungle_  _  _  _ '))
    print(replace_spaces('Jumanji_The_Jungle_  _  _  _  '))
    print(replace_spaces('Jumanji_The_Jungle_  _  _  _  _'))
    print(replace_spaces('Jumanji_The_Jungle_  _  _  _  _ '))
    print(replace_spaces('Jumanji_The_Jungle_  _  _  _  _  '))
    print(replace_spaces('Jumanji_The_Jungle_  _  _  _  _  _'))
    print(replace_spaces('Jumanji_The_Jungle_  _  _  _  _  _ '))
    print(replace_spaces('Jumanji_The_Jungle_  _  _  _  _  _  '))
    print(replace_spaces('Jumanji_The_Jungle_  _  _  _  _  _  _'))
    print(replace_spaces('Jumanji_The_Jungle_  _  _  _  _  _  _ '))
    print(replace_spaces('Jumanji_The_Jungle_  _  _  _  _  _  _  '))
    print(replace_spaces('Jumanji_The_Jungle_  _  _  _  _  _  _  _'))
    print(replace_spaces('Jumanji_The_Jungle_  _  _  _  _  _  _  _ '))
    print(replace_spaces('Jumanji_The_Jungle_  _  _  _  _  _  _  _  '))
    print(replace_spaces('Jumanji_The_Jungle_  _  _  _  _  _  _  _  _'))
    print(replace_spaces('Jumanji_The_Jungle_  _  _  _  _  _  _  _  _ '))
    print(replace_spaces('Jumanji_The_Jungle_  _  _  _  _  _  _  _  _  '))
    print(replace_spaces('Jumanji_The_Jungle_  _  _  _  _  _  _  _  _  _'))
    print(replace_spaces('Jumanji_The_Jungle_  _  _  _  _  _  _  _  _  _ '))
    print(replace_spaces('J