from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
/README.md
# Python 3.7.4

## Installation

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Run

```bash
$ python3 main.py
```

## Test

```bash
$ python3 -m unittest
```
/main.py
from typing import List

from src.concatenate import concatenate


def main() -> None:
    """ Main function
    """
    print(concatenate(['a', 'b', 'c']))


if __name__ == '__main__':
    main()