"""
Write a function to convert a given tuple of positive integers into a single integer.
assert tuple_to_int((1,2,3))==123
"""
def tuple_to_int(numbers):
    """
    Converts a given tuple of positive integers into a single integer
    :param numbers: tuple of positive integers
    :return: single integer
    """
    return int(''.join(map(str, numbers)))

assert tuple_to_int((1,2,3)) == 123
assert tuple_to_int((4,5,6)) == 456
assert tuple_to_int((7,8,9)) == 789
assert tuple_to_int((10,11,12)) == 101112
assert tuple_to_int((13,14,15)) == 131415
assert tuple_to_int((16,17,18)) == 161718
assert tuple_to_int((19,20,21)) == 192021
assert tuple_to_int((22,23,24)) == 222324
assert tuple_to_int((25,26,27)) == 252627
assert tuple_to_int((28,29,30)) == 282930
assert tuple_to_int((31,32,33)) == 313233
assert tuple_to_int((34,35,36)) == 343536
assert tuple_to_int((37,38,39)) == 373839
assert tuple_to_int((40,41,42)) == 404142
assert tuple_to_int((43,44,45)) == 434445
assert tuple_to_int((46,47,48)) == 464748
assert tuple_to_int((49,50,51)) == 495051
assert tuple_to_int((52,53,54)) == 525354
assert tuple_to_int((55,56,57)) == 555657
assert tuple_to_int((58,59,60)) == 585960
assert tuple_to_int((61,62,63)) == 616263
assert tuple_to_int((64,65,66)) == 646566
assert tuple_to_int((67,68,69)) == 676869
assert tuple_to_int((70,71,72)) == 707172
assert tuple_to_int((73,74,75)) == 737475
assert tuple_to_int((76,77,78)) == 767778
assert tuple_to_int((79,80,81)) == 798081
assert tuple_to_int((82,83,84)) == 828384
assert tuple_to_int((85,86,87)) == 858687
assert tuple_to_int((88,89,90)) == 888990
assert tuple_to_int((91,92,93)) == 919293
assert tuple_to_int((94,95,96)) == 949596
assert tuple_to_int((97,98,99)) == 979899
assert tuple_to_int((100,101,102)) == 100101102
assert tuple_to_int((103