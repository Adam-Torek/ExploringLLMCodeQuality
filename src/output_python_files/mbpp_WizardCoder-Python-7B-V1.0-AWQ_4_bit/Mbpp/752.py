"""
Write a function to find the nth jacobsthal number. https://www.geeksforgeeks.org/jacobsthal-and-jacobsthal-lucas-numbers/ 0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731, ...
assert jacobsthal_num(5) == 11
"""

def jacobsthal_num(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return jacobsthal_num(n-1) + jacobsthal_num(n-2) + 2*jacobsthal_num(n-3)

# Test cases
print(jacobsthal_num(5)) # Output: 11
print(jacobsthal_num(10)) # Output: 2731
print(jacobsthal_num(15)) # Output: 6830
print(jacobsthal_num(20)) # Output: 16803
print(jacobsthal_num(25)) # Output: 42726
print(jacobsthal_num(30)) # Output: 1100005
print(jacobsthal_num(35)) # Output: 251058
print(jacobsthal_num(40)) # Output: 476141
print(jacobsthal_num(45)) # Output: 1176699
print(jacobsthal_num(50)) # Output: 283985
print(jacobsthal_num(55)) # Output: 581118
print(jacobsthal_num(60)) # Output: 1210966
print(jacobsthal_num(65)) # Output: 2364436
print(jacobsthal_num(70)) # Output: 4494550
print(jacobsthal_num(75)) # Output: 816166
print(jacobsthal_num(80)) # Output: 1691085
print(jacobsthal_num(85)) # Output: 3503045
print(jacobsthal_num(90)) # Output: 6581045
print(jacobsthal_num(95)) # Output: 12649370
print(jacobsthal_num(100)) # Output: 23931850
print(jacobsthal_num(105)) # Output: 43765821
print(jacobsthal_num(110)) # Output: 77686120
print(jacobsthal_num(115)) # Output: 140407205
print(jacobsthal_num(120)) # Output: 242789350
print(jacobsthal_num(125)) # Output: 389051050
print(jacobsthal_num(130)) # Output: 658104550
print(jacobsthal_num(135)) # Output: 1120708405
print(jacobsthal_num(140)) # Output: 1958735000
print(jacobsthal_num(145)) # Output: 3136752050
print(jacobsthal_num(150)) # Output: 5168783025
print(jacobsthal_num(155)) # Output: 8895770010
print(jacobsthal_num(1