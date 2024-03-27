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
        return max(map(dict_depth, d.values())) + 1
    elif isinstance(d, list):
        return max(map(dict_depth, d)) + 1
    else:
        return 0

assert dict_depth({'a':1, 'b': {'c': {'d': {}}}}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}, 'e': 1}) == 4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}, 'e': [1, {'f': {'g': {}}}]}) == 5
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}, 'e': [1, {'f': {'g': {}}}, {'h': {'i': {'j': {}}}]}}) == 6
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}, 'e': [1, {'f': {'g': {}}}, {'h': {'i': {'j': {}}}, 'k': {'l': {'m': {'n': {'o': {'p': {'q': {'r': {'s': {'t': {'u': {'v': {'w': {'x': {'y': {'z': {'aa': {'bb': {'cc': {'dd': {'ee': {'ff': {'gg': {'hh': {'ii': {'jj': {'kk': {'ll': {'mm': {'nn': {'oo': {'pp': {'qq': {'rr': {'ss': {'tt': {'uu': {'vv': {'ww': {'xx': {'yy': {'zz': {'aaa': {'bbb': {'ccc': {'ddd': {'eee': {'fff': {'ggg': {'hhh': {'iii': {'jjj': {'kkk': {'lll': {'mmm': {'nnn': {'ooo': {'ppp': {'qqq': {'rrr': {'sss': {'ttt': {'uuu': {'vvv': {'www': {'xxx': {'yyy': {'zzz': {'aaa': {'bbb': {'ccc': {'ddd': {'eee': {'fff': {'ggg': {'hhh': {'iii': {'jjj': {'kkk': {'lll': {'mmm': {'nnn': {'ooo': {'ppp': {'qqq': {'rrr': {'sss': {'ttt': {'uuu': {'vvv': {'www': {'xxx': {'yyy': {'zzz': {'aaa': {'bbb': {'ccc': {'ddd': {'eee': {'fff': {'ggg': {'hhh': {'iii': {'jjj': {'kkk': {'lll': {'mmm': {'nnn': {'ooo': {'ppp': {'qqq': {'rrr': {'sss': {'ttt': {'uuu': {'vvv': {'www': {'xxx': {'yyy': {'zzz': {'aaa': {'bbb': {'ccc': {'ddd': {'eee': {'fff': {'ggg': {'hhh': {'iii': {'jjj': {'kkk': {'lll': {'mmm': {'nnn': {'ooo': {'ppp': {'qqq': {'rrr': {'sss': {'ttt': {'uuu': {'vvv': {'www': {'xxx': {'yyy': {'zzz': {'aaa': {'bbb': {'ccc': {'ddd': {'eee': {'fff': {'ggg': {'hhh': {'iii': {'jjj': {'kkk': {'lll': {'mmm': {'nnn': {'ooo': {'ppp': {'qqq': {'rrr': {'sss': {'ttt': {'uuu': {'vvv': {'www': {'xxx': {'yyy': {'zzz': {'aaa': {'bbb': {'ccc': {'ddd': {'eee': {'fff': {'ggg': {'hhh': {'iii': {'jjj': {'kkk': {'lll': {'mmm': {'nnn':