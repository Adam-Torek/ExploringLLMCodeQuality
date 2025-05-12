from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
/README.md
# Python-101

## Description

This repository contains a set of exercises for Python 101 course.

## Installation

To install the project, run the following command:

```bash
git clone https://github.com/d-kostenko/Python-101.git
```

## Usage

To run the project, run the following command:

```bash
python3 main.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
/main.py
from exercises.exercise_1 import filter_by_substring
from exercises.exercise_2 import find_max_value
from exercises.exercise_3 import find_max_value_with_key
from exercises.exercise_4 import find_max_value_with_key_and_default
from exercises.exercise_5 import find_max_value_with_key_and_default_and_default_key
from exercises.exercise_6 import find_max_value_with_key_and_default_and_default_key_and_default_value
from exercises.exercise_7 import find_max_value_with_key_and_default_and_default_key_and_default_value_and_default_key
from exercises.exercise_8 import find_max_value_with_key_and_default_and_default_key_and_default_value_and_default_key_and_default_value
from exercises.exercise_9 import find_max_value_with_key_and_default_and_default_key_and_default_value_and_default_key_and_default_value_and_default_key
from exercises.exercise_10 import find_max_value_with_key_and_default_and_default_key_and_default_value_and_default_key_and_default_value_and_default_key_and_default_value
from exercises.exercise_11 import find_max_value_with_key_and_default_and_default_key_and_default_value_and_default_key_and_default_value_and_default_key_and_default_value_and_default_key
from exercises.exercise_12 import find_max_value_with_key_and_default_and_default_key_and_default_value_and_default_key_and_default_value_and_default_key_and_default_value_and_default_key_and_default_value
from exercises.exercise_13 import find_max_value_with_key_and_default_and_default_key_and_default_value_and_default_key_and_default_value_and_default_key_and_default_value_and_default_key_and_default_value_and_default_key
from exercises.exercise_14 import find_max_value_with_key_and_default_and_default_key_and_default_value_and_default_key_and_default_value_and_default_key_and_default_value_and_default_key_and_default_value_and_default_key_and_default_value
from exercises.exercise_15 import find_max_value_with_key_and_default_and_default_key_and_default_value_and_default_key_and_default_value_and_default_key_and_default_value_and_default_key_and_default_value_and_default_key_and_default_value_and_default_key
from exercises.exercise_16 import find_max_value_with_key_and_default_and_default_key_and_default_value_and_default_key_and_default_value_and_default_key_and_default_value_and_default_key_and_default_value_and_