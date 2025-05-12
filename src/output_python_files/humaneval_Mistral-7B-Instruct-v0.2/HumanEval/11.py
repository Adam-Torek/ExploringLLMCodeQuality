from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join(map(lambda x, y: bin(ord(x) ^ ord(y))[2:][::-1], a, b))


def find_single_bit(data: List[str]) -> str:
    """ Given a list of strings, each consisting of 1s and 0s, find the single bit
    that differs between all strings except one.
    >>> find_single_bit(['01101111', '01101110', '01101101'])
    '1'
    """
    xor_bits = string_xor(*data)
    return '0' if xor_bits[0] == '1' else '1'


def find_gamma_rate(data: List[str]) -> str:
    """ Given a list of strings, each consisting of 1s and 0s, find the gamma rate
    by performing most common bit count on each position.
    >>> find_gamma_rate(['01101111', '01101110', '01101101'])
    '11101101'
    """
    gamma_rate = ''
    for bit in data[0]:
        gamma_rate += str(int('1' * data.count(bit) > len(data) // 2))
    return gamma_rate


def find_epsilon_rate(gamma_rate: str) -> str:
    """ Given a gamma rate string, find the epsilon rate by performing least
    common bit count on each position.
    >>> find_epsilon_rate('11101101')
    '00010010'
    """
    epsilon_rate = ''
    for bit in gamma_rate:
        epsilon_rate += str(int(bit) ^ 1)
    return epsilon_rate


def calculate_power_consumption(data: List[str]) -> int:
    """ Given a list of strings, each consisting of 1s and 0s, calculate the power
    consumption by converting gamma and epsilon rates to decimal and multiplying.
    >>> calculate_power_consumption(['01101111', '01101110', '01101101'])
    198
    """
    gamma_rate = find_gamma_rate(data)
    epsilon_rate = find_epsilon_rate(gamma_rate)
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def find_oxygen_generator_rating(data: List[str]) -> str:
    """ Given a list of strings, each consisting of 1s and 0s, find the oxygen generator
    rating by performing most common bit count on each position, but only keep the
    strings that have that bit in common.
    >>> find_oxygen_generator_rating(['01101111', '01101110', '01101101'])
    '11101101'
    """
    oxygen_generator_rating = ''
    while len(data) > 1:
        most_common_bit = data[0][0]
        data = [bit for bit in data if bit[0] == most_common_bit]
        oxygen_generator_rating += most_common_bit
    return oxygen_generator_rating


def find_co2_scrubber_rating(data: List[str], oxygen