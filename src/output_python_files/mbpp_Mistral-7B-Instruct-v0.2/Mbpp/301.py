"""
Write a function to find the depth of a dictionary.
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
"""
def dict_depth(d):
    """
    :param d: dictionary
    :return: int, depth of the dictionary
    """
    if isinstance(d, dict):
        return 1 + max(map(dict_depth, d.values()))
    elif isinstance(d, list):
        return 1 + max(map(dict_depth, d))
    else:
        return 0

assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}, 'e': 1}) == 4
assert dict_depth({'a':1, 'b': [1, {'c': {'d': {}}}]}) == 4
assert dict_depth({'a':1, 'b': [1, {'c': {'d': {}}}, 2]}) == 5
assert dict_depth({'a':1, 'b': [1, {'c': {'d': {}}}, {'e': 1}]}) == 5
assert dict_depth({'a':1, 'b': [1, {'c': {'d': {}}}, {'e': [1, {'f': {'g': {}}}]}]}) == 6
assert dict_depth({'a':1, 'b': [1, {'c': {'d': {}}}, {'e': [1, {'f': {'g': {}}}, {'h': {'i': {'j': {'k': {'l': {'m': {'n': {'o': {'p': {'q': {'r': {'s': {'t': {'u': {'v': {'w': {'x': {'y': {'z': {'aa': {'bb': {'cc': {'dd': {'ee': {'ff': {'gg': {'hh': {'ii': {'jj': {'kk': {'ll': {'mm': {'nn': {'oo': {'pp': {'qq': {'rr': {'ss': {'tt': {'uu': {'vv': {'ww': {'xx': {'yy': {'zz': {'aaa': {'bbb': {'ccc': {'ddd': {'eee': {'fff': {'ggg': {'hhh': {'iii': {'jjj': {'kkk': {'lll': {'mmm': {'nnn': {'ooo': {'ppp': {'qqq': {'rrr': {'sss': {'ttt': {'uuu': {'vvv': {'www': {'xxx': {'yyy': {'zzz': {'aaaa': {'bbbb': {'cccc': {'dddd': {'eeee': {'ffff': {'gggg': {'hhhh': {'iiii': {'jjjj': {'kkkk': {'llll': {'mmmm': {'nnnn': {'oooo': {'pppp': {'qqqq': {'rrrr': {'ssss': {'tttt': {'uuuu': {'vvvv': {'wwww': {'xxxx': {'yyyy': {'zzzz': {'aaaaa': {'bbbbb': {'ccccc': {'ddddd': {'eeeee': {'fffff': {'ggggg': {'hhhhh': {'iiiii': {'jjjjj': {'kkkkk': {'lllll': {'mmmmm': {'nnnnn': {'ooooo': {'ppppp': {'qqqqq': {'rrrrr': {'sssss': {'ttttt': {'uuuuu': {'vvvvv': {'wwwww': {'xxxxx': {'yyyyy': {'zzzzz': {'aaaaaa': {'bbbbbb': {'cccccc': {'dddddd': {'eeeeee': {'ffffff': {'gggggg': {'hhhhhh': {'iiiiii': {'jjjjjj': {'kkkkkk': {'llllll': {'mmmmmm': {'nnnnnn': {'oooooo': {'pppppp': {'qqqqqq': {'rrrrrr': {'ssssss': {'tttttt': {'uuuuuu': {'vvvvvv': {'wwwwww': {'xxxxxx': {'yyyyyy': {'zzzzzz': {'aaaaaaa': {'