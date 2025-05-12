def eat(number, need, remaining):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    you should return an array of [ total number of eaten carrots after your meals,
                                    the number of carrots left after your meals ]
    if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.
    
    Example:
    * eat(5, 6, 10) -> [11, 4]
    * eat(4, 8, 9) -> [12, 1]
    * eat(1, 10, 10) -> [11, 0]
    * eat(2, 11, 5) -> [7, 0]
    
    Variables:
    @number : integer
        the number of carrots that you have eaten.
    @need : integer
        the number of carrots that you need to eat.
    @remaining : integer
        the number of remaining carrots thet exist in stock
    
    Constrain:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000

    Have fun :)
    """

def eat(number, need, remaining):
    return [number + need, remaining - need]
/7kyu/sum_of_digits_digital_root.py
def digital_root(n):
    """
    A digital root is the recursive sum of all the digits in a number.
    Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
    This is only applicable to the natural numbers.
    Example:
    digital_root(942)
    9 + 4 + 2
    15...
    1 + 5
    6
    digital_root(16)
    1 + 6
    7
    digital_root(999)
    9 + 9 + 9
    27...
    2 + 7
    9
    digital_root(456)
    4 + 5 + 6
    15...
    1 + 5
    6
    digital_root(132189)
    1 + 3 + 2 + 1 + 8 + 9
    24...
    2 + 4
    6
    digital_root(32189)
    3 + 2 + 1 + 8 + 9
    24...
    2 + 4
    6
    digital_root(123456789)
    1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
    45...
    4 + 5
    9
    digital_root(65536)
    6 + 5 + 5 + 3 + 6
    22...
    2 + 2
    4
    digital_root(0)
    0
    digital_root(1)
    1
    digital_root(16)
    1 + 6
    7
    digital_root(942)
    9 + 4 + 2
    15...
    1 + 5
    6
    digital_root(132189)
    1 + 3 + 2 + 1 + 8 + 9
    24...
    2 + 4
    6
    digital_root(32189)
    3 + 2 + 1 + 8 + 9
    24...
    2 + 4
    6
    digital_root(123456789)
    1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
    45...
    4 + 5
    9
    digital_root(65536)
    6 + 5 + 5 + 3 + 6
    22...
    2 + 2
    4
    digital_root(0)
    0
    digital_root(1)
    1
    digital_root(16)
    1 + 6
    7
    digital_root(942)
    9 + 4 + 2
    15...
    1 + 5
    6
    digital_root(132189)
    1 + 3 + 2 + 1 + 8 + 9
    24...
    2 + 4
    6
    digital_root(32189)
    3 +