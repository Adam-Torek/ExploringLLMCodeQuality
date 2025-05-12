def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

def is_palindrome(num):
    """Given an integer. return True if the integer is a palindrome, False otherwise.

    A palindrome is a number that is the same forwards and backwards.

     Example:
        is_palindrome(123) ==> False
        is_palindrome(121) ==> True
    """

def is_prime(num):
    """Given an integer. return True if the integer is a prime number, False otherwise.

    A prime number is a number that is only divisible by 1 and itself.

     Example:
        is_prime(121) ==> False
        is_prime(127) ==> True
    """

def is_armstrong(num):
    """Given an integer. return True if the integer is an Armstrong number, False otherwise.

    An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.

     Example:
        is_armstrong(153) ==> True
        is_armstrong(123) ==> False
    """

def is_perfect(num):
    """Given an integer. return True if the integer is a perfect number, False otherwise.

    A perfect number is a number that is equal to the sum of its proper divisors.

     Example:
        is_perfect(6) ==> True
        is_perfect(12) ==> False
    """

def is_abundant(num):
    """Given an integer. return True if the integer is an abundant number, False otherwise.

    An abundant number is a number that is greater than the sum of its proper divisors.

     Example:
        is_abundant(6) ==> False
        is_abundant(12) ==> True
    """

def is_deficient(num):
    """Given an integer. return True if the integer is a deficient number, False otherwise.

    A deficient number is a number that is less than the sum of its proper divisors.

     Example:
        is_deficient(6) ==> True
        is_deficient(12) ==> False
    """

def is_harshad(num):
    """Given an integer. return True if the integer is a Harshad number, False otherwise.

    A Harshad number is a number that is divisible by the sum of its digits.

     Example:
        is_harshad(18) ==> True
        is_harshad(12) ==> False
    """

def is_strong(num):
    """Given an integer. return True if the integer is a strong number, False otherwise.

    A strong number is a number that is equal to the sum of the factorial of its digits.

     Example:
        is_strong(145) ==> True
        is_strong(12) ==> False
    """

def is_emirp(num):
    """Given an integer. return True if the integer is an emirp number, False otherwise.

    An emirp number is a number that is prime and the reverse of itself is also prime.

     Example:
        is_emirp(121) ==> True
        is_emirp(123) ==> False
    """

def is_happy(num):
    """Given an integer. return True if the integer is a happy number, False otherwise.

    A happy number is a number that is equal to the sum of the squares of its digits.

     Example:
        is_happy(121) ==> True
        is_happy(123) ==> False
    """

def is_lucky(num):
    """Given an integer. return True if the integer is a lucky number, False otherwise.

    A lucky number is a number that is equal to the sum of the digits.

     Example:
        is_lucky(121) ==> True
        is_lucky(123) ==> False
    """

def is_happy_lucky(num):
    """Given an integer. return True if the integer is a happy number or a lucky number, False otherwise.

    A happy number or a lucky number is a number that is equal to the sum of the digits.

     Example:
        is_happy_lucky(121) ==> True
        is_happy_lucky(123) ==> False
    """

def is_happy_lucky_prime(num