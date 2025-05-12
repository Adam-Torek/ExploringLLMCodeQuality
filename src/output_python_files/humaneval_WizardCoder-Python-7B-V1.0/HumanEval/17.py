from typing import List


def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    music_string = music_string.replace(' ', '')
    music_list = music_string.split('|')
    result = []
    for note in music_list:
        if note == 'o':
            result.append(4)
        elif note == '.':
            result.append(1)
        else:
            result.append(2)
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()