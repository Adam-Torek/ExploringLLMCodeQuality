def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """
    # 1. 将N转换为二进制数
    N_binary = bin(N)[2:]
    # 2. 将N_binary转换为字符串
    N_string = N_binary[::-1]
    # 3. 将N_string中的每个字符转换为数字
    N_num = int(N_string, 2)
    # 4. 将N_num转换为字符串
    N_str = str(N_num)
    # 5. 将N_str中的每个字符转换为数字
    N_num2 = int(N_str, 10)
    # 6. 将N_num2转换为二进制数
    N_binary2 = bin(N_num2)[2:]
    # 7. 将N_binary2转换为字符串
    N_string2 = N_binary2[::-1]
    # 8. 将N_string2中的每个字符转换为数字
    N_num3 = int(N_string2, 2)
    # 9. 将N_num3转换为字符串
    N_str3 = str(N_num3)
    # 10. 将N_str3中的每个字符转换为数字
    N_num4 = int(N_str3, 10)
    # 11. 将N_num4转换为二进制数
    N_binary4 = bin(N_num4)[2:]
    # 12. 将N_binary4转换为字符串
    N_string4 = N_binary4[::-1]
    # 13. 将N_string4中的每个字符转换为数字
    N_num5 = int(N_string4, 2)
    # 14. 将N_num5转换为字符串
    N_str5 = str(N_num5)
    # 15. 将N_str5中的每个字符转换为数字
    N_num6 = int(N_str5, 10)
    # 16. 将N_num6转换为二进制数
    N_binary6 = bin(N_num6)[2:]
    # 17. 将N_binary6转换为字符串
    N_string6 = N_binary6[::-1]
    # 18. 将N_string6中的每个字符转换为数字
    N_num7 = int(N_string6, 2)
    # 19. 将N_num7转换为字符串
    N_str7 = str(N_num7)
    # 20. 将N_str7中的每个字符转换为数字
    N_num8 = int(N_str7, 10)
    # 21. 将N_num8转换为二进制数
    N_binary8 = bin(N_num8)[2:]
    # 22. 将N_binary8转换为字符串
    N_string8 = N_binary8[::-1]
    # 23. 将N_string8中的每个字符转换为数字
    N_num9 = int(N_string8, 2)
    # 24. 将N_num9转换为字符串
    N