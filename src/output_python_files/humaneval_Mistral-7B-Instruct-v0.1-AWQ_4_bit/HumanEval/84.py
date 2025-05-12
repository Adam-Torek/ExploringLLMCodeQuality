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
    # 1. 将N转换为二进制数字
    N_binary = bin(N)[2:]
    # 2. 将N_binary转换为字符串
    N_string = N_binary[::-1]
    # 3. 将N_string中的每个字符转换为数字
    N_num = int(N_string, 2)
    # 4. 将N_num转换为字符串
    N_string = str(N_num)
    # 5. 将N_string中的每个字符转换为数字
    N_num = int(N_string, 10)
    # 6. 将N_num转换为二进制数字
    N_binary = bin(N_num)[2:]
    # 7. 将N_binary转换为字符串
    N_string = N_binary[::-1]
    # 8. 将N_string中的每个字符转换为数字
    N_num = int(N_string, 2)
    # 9. 将N_num转换为字符串
    N_string = str(N_num)
    # 10. 将N_string中的每个字符转换为数字
    N_num = int(N_string, 10)
    # 11. 将N_num转换为二进制数字
    N_binary = bin(N_num)[2:]
    # 12. 将N_binary转换为字符串
    N_string = N_binary[::-1]
    # 13. 将N_string中的每个字符转换为数字
    N_num = int(N_string, 2)
    # 14. 将N_num转换为字符串
    N_string = str(N_num)
    # 15. 将N_string中的每个字符转换为数字
    N_num = int(N_string, 10)
    # 16. 将N_num转换为二进制数字
    N_binary = bin(N_num)[2:]
    # 17. 将N_binary转换为字符串
    N_string = N_binary[::-1]
    # 18. 将N_string中的每个字符转换为数字
    N_num = int(N_string, 2)
    # 19. 将N_num转换为字符串
    N_string = str(N_num)
    # 20. 将N_string中的每个字符转换为数字
    N_num = int(N_string, 10)
    # 21. 将N_num转换为二进制数字
    N_binary = bin(N_num)[2:]
    # 22. 将N_binary转换为字符串