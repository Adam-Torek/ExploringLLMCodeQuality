def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

def is_prime(n: int) -> bool:
    """Return True if n is prime, False otherwise.
    >>> is_prime(13195)
    True
    >>> is_prime(2048)
    False
    """

def prime_factors(n: int) -> List[int]:
    """Return a list of prime factors of n. Assume n > 1 and is not a prime.
    >>> prime_factors(13195)
    [2, 3, 5, 7]
    >>> prime_factors(2048)
    [2]
    """

def prime_factorization(n: int) -> Dict[int, int]:
    """Return a dictionary of prime factors and their multiplicities of n.
    >>> prime_factorization(13195)
    {2: 2, 3: 1, 5: 1, 7: 1}
    >>> prime_factorization(2048)
    {2: 1}
    """

def prime_factorization_string(n: int) -> str:
    """Return a string representation of the prime factorization of n.
    >>> prime_factorization_string(13195)
    '2^2 * 3^1 * 5^1 * 7^1'
    >>> prime_factorization_string(2048)
    '2^1'
    """

def prime_factorization_list(n: int) -> List[Tuple[int, int]]:
    """Return a list of tuples representing the prime factorization of n.
    >>> prime_factorization_list(13195)
    [(2, 2), (3, 1), (5, 1), (7, 1)]
    >>> prime_factorization_list(2048)
    [(2, 1)]
    """

def prime_factorization_dict(n: int) -> Dict[int, int]:
    """Return a dictionary of prime factors and their multiplicities of n.
    >>> prime_factorization_dict(13195)
    {2: 2, 3: 1, 5: 1, 7: 1}
    >>> prime_factorization_dict(2048)
    {2: 1}
    """

def prime_factorization_dict_string(n: int) -> str:
    """Return a string representation of the prime factorization of n.
    >>> prime_factorization_dict_string(13195)
    '2^2 * 3^1 * 5^1 * 7^1'
    >>> prime_factorization_dict_string(2048)
    '2^1'
    """

def prime_factorization_dict_list(n: int) -> List[Tuple[int, int]]:
    """Return a list of tuples representing the prime factorization of n.
    >>> prime_factorization_dict_list(13195)
    [(2, 2), (3, 1), (5, 1), (7, 1)]
    >>> prime_factorization_dict_list(2048)
    [(2, 1)]
    """

def prime_factorization_dict_list_string(n: int) -> str:
    """Return a string representation of the prime factorization of n.
    >>> prime_factorization_dict_list_string(13195)
    '2^2 * 3^1 * 5^1 * 7^1'
    >>> prime_factorization_dict_list_string(2048)
    '2^1'
    """

def prime_factorization_dict_list_string_sorted(n: int) -> str:
    """Return a string representation of the prime factorization of n, sorted by prime factor.
    >>> prime_factorization_dict_list_string_sorted(13195)
    '2^2 * 3^1 * 5^1 * 7^1'
    >>> prime_factorization_dict_list_string_sorted(2048)
    '2^1'
    """

def prime_factorization_dict_list_string_sorted_reverse(n: int)