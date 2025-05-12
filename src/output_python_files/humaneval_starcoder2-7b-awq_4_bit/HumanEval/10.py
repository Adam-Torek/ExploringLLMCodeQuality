def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
#    print(string)
    if is_palindrome(string):
        return string
    else:
        # Find the longest palindromic suffix of the string
        suffix = find_longest_palindromic_suffix(string)
        # Find the prefix of the string that comes before the palindromic suffix
        prefix = string[:len(string) - len(suffix)]
        # Reverse the prefix
        prefix = prefix[::-1]
        # Append the prefix to the suffix
        return prefix + suffix


def find_longest_palindromic_suffix(string: str) -> str:
    """ Find the longest palindromic suffix of a string.
    >>> find_longest_palindromic_suffix('')
    ''
    >>> find_longest_palindromic_suffix('cat')
    'at'
    >>> find_longest_palindromic_suffix('cata')
    'ta'
    """
    # Find the longest palindromic suffix of the string
    longest_suffix = ''
    for i in range(len(string)):
        for j in range(i, len(string)):
            if is_palindrome(string[i:j+1]):
                if len(string[i:j+1]) > len(longest_suffix):
                    longest_suffix = string[i:j+1]
    return longest_suffix


def main():
    """ Main function """
    # Read the input from the file
    with open('input.txt', 'r') as input_file:
        input_string = input_file.read()
    # Find the shortest palindrome that begins with the input string
    palindrome = make_palindrome(input_string)
    # Write the result to the output file
    with open('output.txt', 'w') as output_file:
        output_file.write(palindrome)


if __name__ == '__main__':
    main()
/README.md
# Palindromes

This is a solution to the [Palindromes](https://www.hackerrank.com/challenges/palindromes) problem on HackerRank.

## Problem

Given a string, find the shortest palindrome that begins with the string.

## Solution

The solution is implemented in Python 3.

The algorithm is based on the following idea:

- Find the longest palindromic suffix of the string.
- Find the prefix of the string that comes before the palindromic suffix.
- Reverse the prefix.
- Append the prefix to the suffix.

## Usage

The solution can be run with the following command:

```
python3 palindromes.py
```

The input and output files are located in the `data` directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.