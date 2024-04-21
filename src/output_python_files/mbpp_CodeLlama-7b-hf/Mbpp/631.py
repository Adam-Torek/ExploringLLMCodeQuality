"""
Write a function to replace whitespaces with an underscore and vice versa in a given string.
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
"""


def replace_spaces(string):
    """
    Replace spaces with underscores and vice versa
    :param string: string to replace spaces
    :return: string with replaced spaces
    """
    return string.replace(' ', '_').replace('_', ' ')


if __name__ == '__main__':
    print(replace_spaces('Jumanji The Jungle'))
    print(replace_spaces('Jumanji The Jungle '))
    print(replace_spaces('Jumanji The Jungle _'))
    print(replace_spaces('Jumanji The Jungle _ '))
    print(replace_spaces('Jumanji The Jungle _ _'))
    print(replace_spaces('Jumanji The Jungle _ _ '))
    print(replace_spaces('Jumanji The Jungle _ _ _'))
    print(replace_spaces('Jumanji The Jungle _ _ _ '))
    print(replace_spaces('Jumanji The Jungle _ _ _ _'))
    print(replace_spaces('Jumanji The Jungle _ _ _ _ '))
    print(replace_spaces('Jumanji The Jungle _ _ _ _ _'))
    print(replace_spaces('Jumanji The Jungle _ _ _ _ _ '))
    print(replace_spaces('Jumanji The Jungle _ _ _ _ _ _'))
    print(replace_spaces('Jumanji The Jungle _ _ _ _ _ _ '))
    print(replace_spaces('Jumanji The Jungle _ _ _ _ _ _ _'))
    print(replace_spaces('Jumanji The Jungle _ _ _ _ _ _ _ '))
    print(replace_spaces('Jumanji The Jungle _ _ _ _ _ _ _ _'))
    print(replace_spaces('Jumanji The Jungle _ _ _ _ _ _ _ _ '))
    print(replace_spaces('Jumanji The Jungle _ _ _ _ _ _ _ _ _'))
    print(replace_spaces('Jumanji The Jungle _ _ _ _ _ _ _ _ _ '))
    print(replace_spaces('Jumanji The Jungle _ _ _ _ _ _ _ _ _ _'))
    print(replace_spaces('Jumanji The Jungle _ _ _ _ _ _ _ _ _ _ '))
    print(replace_spaces('Jumanji The Jungle _ _ _ _ _ _ _ _ _ _ _'))
    print(replace_spaces('Jumanji The Jungle _ _ _ _ _ _ _ _ _ _ _ '))
    print(replace_spaces('Jumanji The Jungle _ _ _ _ _ _ _ _ _ _ _ _'))
    print(replace_spaces('Jumanji The Jungle _ _ _ _ _ _ _ _ _ _ _ _ '))
    print(replace_spaces('Jumanji The Jungle _ _ _ _ _ _ _ _ _ _ _ _ _'))
    print(replace_spaces('Jumanji The Jungle _ _ _ _ _ _ _ _ _ _ _ _ _ '))
    print(replace_spaces('Jumanji The Jungle _ _ _ _ _ _ _ _ _ _ _ _ _ _'))
    print(replace_spaces('Jumanji The Jungle _ _ _ _ _ _ _ _ _ _ _ _ _ _ '))
    print(replace_spaces('Jumanji The Jungle _ _ _ _ _ _ _ _ _ _ _ _ _ _ _'))
    print(replace_spaces('Jumanji The Jungle _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ '))
    print(replace_spaces('Jumanji The Jungle _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _'))
    print(replace_spaces('Jumanji The Jungle _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ '))
    print(replace_spaces('Jumanji The Jungle _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _'))
    print(replace_spaces('Jumanji The Jungle _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ '))
    print(replace_spaces('Jumanji The Jungle _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _'))