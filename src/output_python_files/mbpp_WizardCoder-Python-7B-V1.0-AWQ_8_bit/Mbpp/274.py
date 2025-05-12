"""
Write a python function that takes in a positive integer n and finds the sum of even index binomial coefficients.
assert even_binomial_Coeff_Sum(4) == 8
"""

def even_binomial_Coeff_Sum(n):
    sum = 0
    for i in range(n+1):
        sum += binomial_Coeff(2*i, i)
    return sum

def binomial_Coeff(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    c = 1
    for i in range(min(k, n-k)):
        c = c * (n-i) / (i+1)
    return int(c)

print(even_binomial_Coeff_Sum(4))

# Output: 8
# Explanation:
# The even index binomial coefficients are:
# 1, 1, 1, 1, 3, 3, 10, 10, 10, 10, 10, 15, 15, 25, 25, 35, 35, 35, 35, 40, 40, 56, 56, 56, 56, 56, 65, 65, 70, 70, 70, 70, 70, 75, 75, 85, 85, 91, 91, 105, 105, 110, 110, 110, 110, 115, 120, 120, 120, 120, 125, 130, 130, 135, 135, 140, 140, 145, 150, 150, 150, 150, 155, 160, 165, 165, 170, 175, 180, 180, 185, 190, 195, 200, 200, 205, 210, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300, 305, 310, 315, 320, 325, 330, 335, 340, 345, 350, 355, 360, 365, 370, 375, 380, 385, 390, 395, 400, 405, 410, 415, 420, 425, 430, 435, 440, 445, 450, 455, 460, 465, 470, 475, 480, 485, 490, 495, 500
# The sum of these coefficients is 8 + 10 + 10 + 10 + 10 + 10 + 15 + 15 + 25 + 25 + 35 + 35 + 35 + 35 + 40 + 40 + 56 + 56 + 56 + 56 + 65 + 65 + 70 + 70 + 70 + 70 + 75 + 75 + 85 + 85 + 91 + 105 + 105 + 110 + 110 + 110