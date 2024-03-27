"""
Write a function to find the Eulerian number a(n, m).
assert eulerian_num(3, 1) == 4
"""

def eulerian_num(n, m):
    """
    :param n: int
    :param m: int
    :return: int
    """
    if n == 0:
        return 1
    if m == 0:
        return 0
    return eulerian_num(n - 1, m) + m * eulerian_num(n - 1, m - 1)


if __name__ == '__main__':
    print(eulerian_num(3, 1))
<file_sep>/leetcode/1001-1100/1021.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : <NAME> 
# @Created       : 2020-07-06 22:15:31
# @Last Modified : 2020-07-06 22:15:31
# @Mail          : <EMAIL>
# @Version       : alpha-1.0

"""
# 给出 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表空格的字符为 ''。 
# 
#  示例： 
#  
#  输入：S = "ab#c", T = "ad#c"
# 输出：true
# 解释：S 和 T 都会变成 “ac”。
#  
# 
#  输入：S = "ab##", T = "c#d#"
# 输出：true
# 解释：S 和 T 都会变成 “”。
#  
# 
#  输入：S = "a##c", T = "#a#c"
# 输出：true
# 解释：S 和 T 都会变成 “c”。
#  
# 
#  输入：S = "a#c", T = "b"
# 输出：false
# 解释：S 会变成 “c”，但 T 仍然是 “b”。
#  
# 
#  
# 
#  提示： 
# 
#  
# 1 <= S.length <= 200 
# 1 <= T.length <= 200 
# S 和 T 只含有小写字母以及字符 '#'。 
# 
#  
# 
#  进阶： 
# 
#  你可以用 O(N) 的时间复杂度和 O(1) 的空间复杂度解决该问题吗？ 
#  
#  Related Topics 栈 
#  👍 110 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        """
        栈
        """
        def get_str(s):
            stack = []
            for c in s:
                if c == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return ''.join(stack)

        return get_str(S) == get_str(T)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (["ab#c", "ad#c"], True),
    (["ab##", "c#d#"], True),
    (["a##c", "#a#c"], True),
    (["a#c", "b"], False),
])
def test_solutions(args, expected):
    assert Solution().backspaceCompare(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
<file_sep>/python/CrackingTheCodingInterview_6/16.01.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : <NAME> 
# @Created       : 2020-07-02 18:00:00
# @Last Modified : 2020-07-02 18:00:00
# @Mail