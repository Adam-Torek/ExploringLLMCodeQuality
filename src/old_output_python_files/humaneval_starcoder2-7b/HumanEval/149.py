def sorted_list_sum(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """

def is_prime(num):
    """Write a function that accepts a number as a parameter and
    returns True if the number is prime, False otherwise.
    A prime number is a number that is only divisible by 1 and itself.
    For example:
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(7) == True
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False
    assert is_prime(11) == True
    assert is_prime(12) == False
    assert is_prime(13) == True
    assert is_prime(14) == False
    assert is_prime(15) == False
    assert is_prime(16) == False
    assert is_prime(17) == True
    assert is_prime(18) == False
    assert is_prime(19) == True
    assert is_prime(20) == False
    assert is_prime(21) == False
    assert is_prime(22) == False
    assert is_prime(23) == True
    assert is_prime(24) == False
    assert is_prime(25) == False
    assert is_prime(26) == False
    assert is_prime(27) == False
    assert is_prime(28) == False
    assert is_prime(29) == True
    assert is_prime(30) == False
    assert is_prime(31) == True
    assert is_prime(32) == False
    assert is_prime(33) == False
    assert is_prime(34) == False
    assert is_prime(35) == False
    assert is_prime(36) == False
    assert is_prime(37) == True
    assert is_prime(38) == False
    assert is_prime(39) == False
    assert is_prime(40) == False
    assert is_prime(41) == True
    assert is_prime(42) == False
    assert is_prime(43) == True
    assert is_prime(44) == False
    assert is_prime(45) == False
    assert is_prime(46) == False
    assert is_prime(47) == True
    assert is_prime(48) == False
    assert is_prime(49) == False
    assert is_prime(50) == False
    assert is_prime(51) == False
    assert is_prime(52) == False
    assert is_prime(53) == True
    assert is_prime(54) == False
    assert is_prime(55) == False
    assert is_prime(56) == False
    assert is_prime(57) == False
    assert is_prime(58) == False
    assert is_prime(59) == True
    assert is_prime(60) == False
    assert is_prime(61) == True
    assert is_prime(62) == False
    assert is_prime(63) == False
    assert is_prime(64) == False
    assert is_prime(65) == False
    assert is_prime(66) == False
    assert is_prime(67) == True
    assert is_prime(68) == False
    assert is_prime(69) == False
    assert is_prime(70) == False
    assert is_prime(71) == True
    assert is_prime(72) ==