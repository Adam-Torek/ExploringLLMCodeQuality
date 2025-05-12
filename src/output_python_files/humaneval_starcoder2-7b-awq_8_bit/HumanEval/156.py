def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """

def mini_roman_to_int(roman):
    """
    Given a roman numeral string, return its integer equivalent.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> mini_roman_to_int('xix') == 19
    >>> mini_roman_to_int('clii') == 152
    >>> mini_roman_to_int('cdxxvi') == 426
    """

def main():
    """
    The main function for the program.
    """
    pass

if __name__ == '__main__':
    main()
/README.md
# Python-Practice

This repository contains my solutions to various problems in Python.

## Problems

### 1. Roman Numerals

Given a positive integer, obtain its roman numeral equivalent as a string,
and return it in lowercase.

Restrictions: 1 <= num <= 1000

Examples:

```
>>> int_to_mini_roman(19) == 'xix'
>>> int_to_mini_roman(152) == 'clii'
>>> int_to_mini_roman(426) == 'cdxxvi'
```

### 2. Mini Roman Numerals

Given a roman numeral string, return its integer equivalent.

Restrictions: 1 <= num <= 1000

Examples:

```
>>> mini_roman_to_int('xix') == 19
>>> mini_roman_to_int('clii') == 152
>>> mini_roman_to_int('cdxxvi') == 426
```

### 3. FizzBuzz

Write a program that prints the numbers from 1 to 100. But for multiples of
three print "Fizz" instead of the number and for the multiples of five print
"Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

Examples:

```
>>> fizzbuzz()
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
Fizz
52
53
Fizz
Buzz
56
Fizz
58
59
FizzBuzz
61
62
Fizz
64
Buzz
Fizz
67
68
Fizz
Buzz
71
Fizz
73
74
FizzBuzz
76
77
Fizz
79
Buzz
Fizz
82
83
Fizz
Buzz
86
Fizz
88
89
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
Buzz
```

### 4. Palindromes

Write a program that prints all the palindromes in a given range.

Examples:

```
>>> palindromes(1, 100)
1
2
3
4
5
6
7
8
9
11
22
101
```

### 5. Fibonacci

Write a program that prints the Fibonacci sequence up to a given number.

Examples:

```
>>> fibonacci(10)
1
1
2
3
5
8