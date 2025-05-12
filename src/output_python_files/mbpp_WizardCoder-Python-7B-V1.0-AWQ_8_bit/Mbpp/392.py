"""
Write a function to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n).
assert get_max_sum(60) == 106
"""

def get_max_sum(n):
    memo = {}
    def helper(x):
        if x in memo:
            return memo[x]
        if x == 1:
            return 1
        if x % 10 == 0:
            return 0
        if x % 3 == 0:
            return 0
        if x % 2 == 0:
            memo[x] = max(helper(x//2), helper(x//3), helper(x//4), helper(x//5)) + x
        else:
            memo[x] = max(helper(x//2), helper(x//3), helper(x//4), helper(x//5)) + x
        return memo[x]
    return helper(n)

print(get_max_sum(60)) # 106
print(get_max_sum(10)) # 10
print(get_max_sum(1)) # 1
print(get_max_sum(2)) # 2
print(get_max_sum(3)) # 3
print(get_max_sum(4)) # 4
print(get_max_sum(5)) # 5
print(get_max_sum(6)) # 6
print(get_max_sum(7)) # 7
print(get_max_sum(8)) # 8
print(get_max_sum(9)) # 9
print(get_max_sum(10)) # 10
print(get_max_sum(11)) # 11
print(get_max_sum(12)) # 12
print(get_max_sum(13)) # 13
print(get_max_sum(14)) # 14
print(get_max_sum(15)) # 15
print(get_max_sum(16)) # 16
print(get_max_sum(17)) # 17
print(get_max_sum(18)) # 18
print(get_max_sum(19)) # 19
print(get_max_sum(20)) # 20
print(get_max_sum(21)) # 21
print(get_max_sum(22)) # 22
print(get_max_sum(23)) # 23
print(get_max_sum(24)) # 24
print(get_max_sum(25)) # 25
print(get_max_sum(26)) # 26
print(get_max_sum(27)) # 27
print(get_max_sum(28)) # 28
print(get_max_sum(29)) # 29
print(get_max_sum(30)) # 30
print(get_max_sum(31)) # 31
print(get_max_sum(32)) # 32
print(get_max_sum(33)) # 33
print(get_max_sum(34)) # 34
print(get_max_sum(35)) # 35
print(get_max_sum(36)) # 36
print(get_max_sum(37)) # 37
print(get_max_sum(38)) # 38
print(get_max_sum(39)) # 39
print(get_max_sum(40)) # 40
print(get_max_sum(41)) # 41
print(get_max_sum(42)) # 42
print(get_max_sum(43)) # 43
print(get_max_sum(44)) # 44
print(get_max_sum(45)) # 45
print(get_max_sum(46)) # 46
print(get_max_sum(47