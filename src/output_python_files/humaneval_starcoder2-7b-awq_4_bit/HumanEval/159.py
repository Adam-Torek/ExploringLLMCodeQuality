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
/7kyu/simple_fun_number_1_reverse_or_not.py
def reverse_or_not(n):
    """
    You are given an array of integers.
    You should return an array of the string representations of the integers.
    If the number is divisible by 3, change it to reverse of it.
    Otherwise, change it to the string representation.
    
    Example:
    * reverse_or_not([12, 13, 14]) -> ["12", "14", "31"]
    * reverse_or_not([12, 13, 14]) -> ["12", "14", "31"]
    * reverse_or_not([12, 13, 14]) -> ["12", "14", "31"]
    
    Variables:
    @n : array of integers
    
    Constrain:
    * 0 <= n.length <= 1000
    * 0 <= n[i] <= 1000
    
    Have fun :)
    """

def reverse_or_not(n):
    return [str(i) if i % 3 else str(i)[::-1] for i in n]
/7kyu/simple_fun_number_1_reverse_or_not.js
function reverseOrNot(n) {
    /*
    You are given an array of integers.
    You should return an array of the string representations of the integers.
    If the number is divisible by 3, change it to reverse of it.
    Otherwise, change it to the string representation.
    
    Example:
    * reverse_or_not([12, 13, 14]) -> ["12", "14", "31"]
    * reverse_or_not([12, 13, 14]) -> ["12", "14", "31"]
    * reverse_or_not([12, 13, 14]) -> ["12", "14", "31"]
    
    Variables:
    @n : array of integers
    
    Constrain:
    * 0 <= n.length <= 1000
    * 0 <= n[i] <= 1000
    
    Have fun :)
    */

    return n.map(i => i % 3? i : i.toString().split('').reverse().join(''));
}
/7kyu/simple_fun_number_1_reverse_or_not.rb
def reverse_or_not(n)
    """
    You are given an array of integers.
    You should return an array of the string representations of the integers.
    If the number is divisible by 3, change it to reverse of it.
    Otherwise, change it to the string representation.
    
    Example:
    * reverse_or_not([12, 13, 14]) -> ["12", "14", "31"]
    * reverse_or_not([12, 13, 14]) -> ["12", "14", "31"]
    * reverse_or_not([12,