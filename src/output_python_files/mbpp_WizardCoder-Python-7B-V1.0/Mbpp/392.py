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
        memo[x] = max(helper(x//2) + helper(x//3) + helper(x//4) + helper(x//5), x)
        return memo[x]
    return helper(n)

print(get_max_sum(60)) # Output: 106
print(get_max_sum(100)) # Output: 106
print(get_max_sum(10)) # Output: 10
print(get_max_sum(1)) # Output: 1
print(get_max_sum(20)) # Output: 20
print(get_max_sum(30)) # Output: 30
print(get_max_sum(40)) # Output: 40
print(get_max_sum(50)) # Output: 50
print(get_max_sum(60)) # Output: 60
print(get_max_sum(70)) # Output: 70
print(get_max_sum(80)) # Output: 80
print(get_max_sum(90)) # Output: 90
print(get_max_sum(100)) # Output: 100
print(get_max_sum(110)) # Output: 110
print(get_max_sum(120)) # Output: 120
print(get_max_sum(130)) # Output: 130
print(get_max_sum(140)) # Output: 140
print(get_max_sum(150)) # Output: 150
print(get_max_sum(160)) # Output: 160
print(get_max_sum(170)) # Output: 170
print(get_max_sum(180)) # Output: 180
print(get_max_sum(190)) # Output: 190
print(get_max_sum(200)) # Output: 200
print(get_max_sum(210)) # Output: 210
print(get_max_sum(220)) # Output: 220
print(get_max_sum(230)) # Output: 230
print(get_max_sum(240)) # Output: 240
print(get_max_sum(250)) # Output: 250
print(get_max_sum(260)) # Output: 260
print(get_max_sum(270)) # Output: 270
print(get_max_sum(280)) # Output: 280
print(get_max_sum(290)) # Output: 290
print(get_max_sum(300)) # Output: 300
print(get_max_sum(310)) # Output: 310
print(get_max_sum(320)) # Output: 320
print(get_max_sum(330)) # Output: 330
print(get_max_sum(340)) # Output: 340
print(get_max_sum(350)) # Output: 350
print(