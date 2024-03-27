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
    music_list = []
    for i in music_string:
        if i == 'o':
            music_list.append(4)
        elif i == 'o|':
            music_list.append(2)
        elif i == '.|':
            music_list.append(1)
    return music_list


def beat_to_time(beat: int) -> float:
    """ Input to this function is a number of beats.
    Your task is to return the time in seconds that this number of beats lasts.

    >>> beat_to_time(4)
    1.0
    >>> beat_to_time(2)
    0.5
    >>> beat_to_time(1)
    0.25
    """
    if beat == 4:
        return 1
    elif beat == 2:
        return 0.5
    elif beat == 1:
        return 0.25


def time_to_beat(time: float) -> int:
    """ Input to this function is a time in seconds.
    Your task is to return the number of beats that this time lasts.

    >>> time_to_beat(1)
    4
    >>> time_to_beat(0.5)
    2
    >>> time_to_beat(0.25)
    1
    """
    if time == 1:
        return 4
    elif time == 0.5:
        return 2
    elif time == 0.25:
        return 1


def beat_to_time_list(beat_list: List[int]) -> List[float]:
    """ Input to this function is a list of beats.
    Your task is to return a list of times that each beat lasts.

    >>> beat_to_time_list([4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])
    [1.0, 0.5, 0.25, 0.5, 0.5, 0.25, 0.25, 0.25, 0.25, 1.0, 1.0]
    """
    time_list = []
    for i in beat_list:
        time_list.append(beat_to_time(i))
    return time_list


def time_to_beat_list(time_list: List[float]) -> List[int]:
    """ Input to this function is a list of times.
    Your task is to return a list of beats that each time lasts.

    >>> time_to_beat_list([1.0, 0.5, 0.25, 0.5, 0.5, 0.25, 0.25, 0.25, 0.25, 1.0, 1.0])
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    beat_list = []
    for i in time_list:
        beat_list.append(time_to_beat(i))
    return beat_list


def beat_to_time_string(beat_list: List[int]) -> str:
    """ Input to this function is a list of beats.
    Your task is to return a string representing the time that each beat