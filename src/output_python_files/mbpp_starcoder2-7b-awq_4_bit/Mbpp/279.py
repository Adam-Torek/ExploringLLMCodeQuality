"""
Write a function to find the nth decagonal number.
assert is_num_decagonal(3) == 27
"""

def is_num_decagonal(n):
    return (10*n + 1)**0.5 == int((10*n + 1)**0.5)

def nth_decagonal(n):
    if n == 0:
        return 0
    else:
        i = 1
        while True:
            if is_num_decagonal(i):
                if i == n:
                    return (10*i + 1)**0.5
                else:
                    i += 1
            else:
                i += 1

def test_nth_decagonal():
    assert nth_decagonal(0) == 0
    assert nth_decagonal(1) == 1
    assert nth_decagonal(2) == 10
    assert nth_decagonal(3) == 27
    assert nth_decagonal(4) == 58
    assert nth_decagonal(5) == 122
    assert nth_decagonal(6) == 243
    assert nth_decagonal(7) == 486
    assert nth_decagonal(8) == 970
    assert nth_decagonal(9) == 1940
    assert nth_decagonal(10) == 3880
    assert nth_decagonal(11) == 7759
    assert nth_decagonal(12) == 15517
    assert nth_decagonal(13) == 31034
    assert nth_decagonal(14) == 62068
    assert nth_decagonal(15) == 124135
    assert nth_decagonal(16) == 248270
    assert nth_decagonal(17) == 496540
    assert nth_decagonal(18) == 993080
    assert nth_decagonal(19) == 1986160
    assert nth_decagonal(20) == 3972320
    assert nth_decagonal(21) == 7944640
    assert nth_decagonal(22) == 15889280
    assert nth_decagonal(23) == 31778560
    assert nth_decagonal(24) == 63557120
    assert nth_decagonal(25) == 127114240
    assert nth_decagonal(26) == 254228480
    assert nth_decagonal(27) == 508456960
    assert nth_decagonal(28) == 1016913920
    assert nth_decagonal(29) == 2033827840
    assert nth_decagonal(30) == 4067655680
    assert nth_decagonal(31) == 8135311360
    assert nth_decagonal(32) == 16270622720
    assert nth_decagonal(33) == 32541245440
    assert nth_decagonal(34) == 65082490880
    assert nth_decagonal(35) == 130164981760
    assert nth_decagonal(36) == 260329963520
    assert nth_decagonal(37) == 520659927040
    assert nth_decagonal(38) == 1041319854080