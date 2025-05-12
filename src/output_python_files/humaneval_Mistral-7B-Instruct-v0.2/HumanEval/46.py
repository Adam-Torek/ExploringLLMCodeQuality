def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    a, b, c, d = 0, 0, 2, 0
    for _ in range(n):
        a, b, c, d = b, c, d, a + b + c
    return d

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(fib4(10)) # 32
    print(fib4(15)) # 100
    print(fib4(20)) # 258
    print(fib4(25)) # 704
    print(fib4(30)) # 1771
    print(fib4(35)) # 4807
    print(fib4(40)) # 13462
    print(fib4(45)) # 38742
    print(fib4(50)) # 109461
    print(fib4(55)) # 308061
    print(fib4(60)) # 832040
    print(fib4(65)) # 2258514
    print(fib4(70)) # 5912867
    print(fib4(75)) # 15746400
    print(fib4(80)) # 41612945
    print(fib4(85)) # 111764580
    print(fib4(90)) # 300393702
    print(fib4(95)) # 832040390
    print(fib4(100)) # 225851433
    print(fib4(105)) # 591286722
    print(fib4(110)) # 1574640077
    print(fib4(115)) # 4161294595
    print(fib4(120)) # 11176458570
    print(fib4(125)) # 30039370562
    print(fib4(130)) # 83204039453
    print(fib4(135)) # 225851436450
    print(fib4(140)) # 591286729879
    print(fib4(145)) # 1574640083204
    print(fib4(150)) # 4161294601496
    print(fib4(155)) # 11176458842758
    print(fib4(160)) # 30039371088475
    print(fib4(165)) # 832040431655766
    print(fib4(170)) # 2258514464227370
    print(fib4(175)) # 5912867429114817