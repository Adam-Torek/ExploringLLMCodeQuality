"""
Write a function to check if the given integer is a prime number.
assert prime_num(13)==True
"""
def prime_num(n):
    """
    :param n: an integer
    :return: True if n is a prime number, False otherwise
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Test the function
assert prime_num(13) == True
assert prime_num(12) == False
assert prime_num(17) == True
assert prime_num(11) == True
assert prime_num(15) == False
assert prime_num(2) == True
assert prime_num(3) == True
assert prime_num(5) == True
assert prime_num(7) == True
assert prime_num(11) == True
assert prime_num(19) == True
assert prime_num(23) == True
assert prime_num(29) == True
assert prime_num(31) == True
assert prime_num(37) == True
assert prime_num(41) == True
assert prime_num(43) == True
assert prime_num(47) == True
assert prime_num(53) == True
assert prime_num(59) == True
assert prime_num(61) == True
assert prime_num(67) == True
assert prime_num(71) == True
assert prime_num(73) == True
assert prime_num(79) == True
assert prime_num(83) == True
assert prime_num(89) == True
assert prime_num(97) == True
assert prime_num(101) == True
assert prime_num(103) == True
assert prime_num(107) == True
assert prime_num(109) == True
assert prime_num(113) == True
assert prime_num(127) == True
assert prime_num(131) == True
assert prime_num(137) == True
assert prime_num(139) == True
assert prime_num(149) == True
assert prime_num(151) == True
assert prime_num(157) == True
assert prime_num(163) == True
assert prime_num(167) == True
assert prime_num(173) == True
assert prime_num(179) == True
assert prime_num(181) == True
assert prime_num(191) == True
assert prime_num(193) == True
assert prime_num(197) == True
assert prime_num(199) == True
assert prime_num(211) == True
assert prime_num(223) == True
assert prime_num(227) == True
assert prime_num(229) == True
assert prime_num(233) == True
assert prime_num(239) == True
assert prime_num(241) == True
assert prime_num(251) == True
assert prime_num(257) == True
assert prime_num(263) == True
assert prime_num(269) == True
assert prime_num(271) == True
assert prime_num(277) == True
assert prime_num(281) == True
assert prime_num(283) == True
assert prime_num(293) == True
assert prime_num(307) == True
assert prime_num(311) == True
assert prime_num(313) == True
assert prime_num(317) == True
assert prime_num(331) == True
assert prime_num(337) == True
assert prime_num(347) == True
assert prime_num(349) == True
assert prime_num(353) == True
assert prime_num(359) == True
assert prime_num(367) == True
assert prime_num(373) == True
assert prime_num(379)