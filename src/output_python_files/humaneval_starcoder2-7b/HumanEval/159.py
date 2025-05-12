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
    * digital_root(16)
    => 1 + 6
    => 7

    * digital_root(942)
    => 9 + 4 + 2
    => 15...
    => 1 + 5
    => 6

    * digital_root(132189)
    => 1 + 3 + 2 + 1 + 8 + 9
    => 24...
    => 2 + 4
    => 6

    * digital_root(493193)
    => 4 + 9 + 3 + 1 + 9 + 3
    => 29...
    => 2 + 9
    => 11...
    => 1 + 1
    => 2

    Variables:
    @n : integer
        the number that you want to calculate the digital root.

    Constrain:
    * 0 <= n <= 10^10000

    Have fun :)
    """

def digital_root(n):
    if n < 10:
        return n
    else:
        return digital_root(sum([int(i) for i in str(n)]))
/7kyu/sum_of_odd_numbers.py
def row_sum_odd_numbers(n):
    """
    Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
   19    21    23    25    27
   29    31    33    35    37    39
   39    41    43    45    47    49    51
   49    51    53    55    57    59    61    63
   59    61    63    65    67    69    71    73    75
   75    77    79    81    83    85    87    89    91    93
   93    95    97    99    101    103    105    107    109    111    113
   113    115    117    119    121    123    125    127    129    131    133    135
   135    137    139    141    143    145    147    149    151    153    155    157    159
   159    16