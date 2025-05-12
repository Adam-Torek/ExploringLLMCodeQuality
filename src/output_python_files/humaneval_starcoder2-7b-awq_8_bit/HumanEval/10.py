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
        # Find the longest palindromic suffix of string
        suffix = find_longest_palindromic_suffix(string)
        # Find the prefix of string that comes before the palindromic suffix
        prefix = string[:len(string) - len(suffix)]
        # Reverse the prefix
        prefix = prefix[::-1]
        # Append the reversed prefix to the end of the string
        return string + prefix


def find_longest_palindromic_suffix(string: str) -> str:
    """ Find the longest palindromic suffix of a string """
    # Find the longest palindromic suffix of string
    longest_palindromic_suffix = ''
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            if is_palindrome(substring):
                if len(substring) > len(longest_palindromic_suffix):
                    longest_palindromic_suffix = substring
    return longest_palindromic_suffix


def main():
    """ Main function """
    # Read input from stdin
    input_lines = sys.stdin.readlines()
    # Remove whitespace characters like `\n` at the end of each line
    input_lines = [x.strip() for x in input_lines]
    # Iterate over the input
    for line in input_lines:
        # Print the result to stdout
        print(make_palindrome(line))


if __name__ == '__main__':
    main()
/README.md
# Palindrome

This is a simple Python 3 script that finds the shortest palindrome that begins with a supplied string.

## Usage

```
$ python3 palindrome.py < input.txt > output.txt
```

## Example

```
$ cat input.txt
cat
cata
$ python3 palindrome.py < input.txt
catac
catac
```