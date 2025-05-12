from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)


def main():
    """ Testing """
    print(concatenate([]))
    print(concatenate(['a', 'b', 'c']))
    print(concatenate(['1', '2', '3'])))
    print(concatenate(['', 'a', 'b', 'c'])))


if __name__ == '__main__':
    main()