from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
<file_sep>/python/leetcode/2020/07/07.py
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
        """
        if not points:
            return 0

        points.sort(key=lambda x: x[1])
        arrow_count = 1
        prev_end = points[0][1]
        for start, end in points[1:]:
            if start > prev_end:
                arrow_count += 1
                prev_end = end

        return arrow_count
<file_sep>/python/leetcode/2020/07/07.py
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
        """
        if not points:
            return 0

        points.sort(key=lambda x: x[1])
        arrow_count = 1
        prev_end = points[0][1]
        for start, end in points[1:]:
            if start > prev_end:
                arrow_count += 1
                prev_end = end

        return arrow_count
<file_sep>/python/leetcode/2020/07/07.py
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
        """
        if not points:
            return 0

        points.sort(key=lambda x: x[1])
        arrow_count = 1
        prev_end = points[0][1]
        for start, end in points[1:]:
            if start > prev_end:
                arrow_count += 1
                prev_end = end

        return arrow_count
<file_sep>/python/leetcode/2020/07/07.py
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
        """
        if not points:
            return 0

        points.sort(key=lambda x: x[1])
        arrow_count = 1
        prev_end = points[0][1]
        for start, end in points[1:]:
            if start > prev_end:
                arrow_count += 1
                prev_end = end

        return arrow_count
<file_sep>/python/leetcode/2020/07/07.py
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
        """
        if not points:
            return 0

        points.sort(key=lambda x: x[1])
        arrow_count = 1
        prev_end = points[0][1]
        for start, end in points[1:]:
            if start > prev_end:
                arrow_count += 1
                prev_end = end

        return arrow_count
<file_sep>/python/leetcode/2020/07/07.py
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
        """
        if not points:
            return 0

        points.sort(key=lambda x: x[1])
        arrow_count = 1
        prev_end = points[0][1]
        for start,