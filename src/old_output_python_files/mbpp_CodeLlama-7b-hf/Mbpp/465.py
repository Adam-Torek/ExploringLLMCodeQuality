"""
Write a function to drop empty items from a given dictionary.
assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
"""


def drop_empty(d):
    return {k: v for k, v in d.items() if v is not None}


if __name__ == '__main__':
    print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': None}))
    print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': 'Blue'}))
    print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': 'Blue', 'c4': None}))
    print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': 'Blue', 'c4': None, 'c5': None}))
    print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': 'Blue', 'c4': None, 'c5': None, 'c6': None}))
    print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': 'Blue', 'c4': None, 'c5': None, 'c6': None, 'c7': None}))
    print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': 'Blue', 'c4': None, 'c5': None, 'c6': None, 'c7': None, 'c8': None}))
    print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': 'Blue', 'c4': None, 'c5': None, 'c6': None, 'c7': None, 'c8': None, 'c9': None}))
    print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': 'Blue', 'c4': None, 'c5': None, 'c6': None, 'c7': None, 'c8': None, 'c9': None, 'c10': None}))
    print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': 'Blue', 'c4': None, 'c5': None, 'c6': None, 'c7': None, 'c8': None, 'c9': None, 'c10': None, 'c11': None}))
    print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': 'Blue', 'c4': None, 'c5': None, 'c6': None, 'c7': None, 'c8': None, 'c9': None, 'c10': None, 'c11': None, 'c12': None}))
    print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': 'Blue', 'c4': None, 'c5': None, 'c6': None, 'c7': None, 'c8': None, 'c9': None, 'c10': None, 'c11': None, 'c12': None, 'c13': None}))
    print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': 'Blue', 'c4': None, 'c5': None, 'c6': None, 'c7': None, 'c8': None, 'c9': None, 'c10': None, 'c11': None, 'c12': None, 'c13': None, 'c14': None}))
    print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': 'Blue', 'c4': None, 'c5': None, 'c6': None, 'c7': None, 'c8': None, 'c9': None, 'c10': None, 'c11': None, 'c12': None, 'c13': None, 'c14': None, 'c15': None}))
    print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3