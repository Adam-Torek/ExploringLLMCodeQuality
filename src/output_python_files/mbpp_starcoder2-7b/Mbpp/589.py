"""
Write a function to find perfect squares between two given numbers.
assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
"""

def perfect_squares(start, end):
    return [i**2 for i in range(start, end+1) if i**0.5 == int(i**0.5)]

print(perfect_squares(1,30))
/python/00001-05000/00011-00500/00111-01600/00511-06600/00551-06600/00554-00600/00555-00600/00556-00600/00557-00600/00558-00600/00559-00600/00560-00600/00561-00600/00562-00600/00563-00600/00564-00600/00565-00600/00566-00600/00567-00600/00568-00600/00569-00600/00570-00600/00571-00600/00572-00600/00573-00600/00574-00600/00575-00600/00576-00600/00577-00600/00578-00600/00579-00600/00580-00600/00581-00600/00582-00600/00583-00600/00584-00600/00585-00600/00586-00600/00587-00600/00588-00600/00589-00600/00590-00600/00591-00600/00592-00600/00593-00600/00594-00600/00595-00600/00596-00600/00597-00600/00598-00600/00599-00600.py
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix)!= 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

print(Solution().longestCommonPrefix(["flower","flow","flight"]))
print(Solution().longestCommonPrefix(["dog","racecar","car"]))
/python/00001-05000/