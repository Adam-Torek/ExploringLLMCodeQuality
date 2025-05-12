"""
Write a python function to find sum of products of all possible sublists of a given list. https://www.geeksforgeeks.org/sum-of-products-of-all-possible-subarrays/
assert sum_Of_Subarray_Prod([1,2,3]) == 20
"""

def sum_Of_Subarray_Prod(arr):
    sum = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            prod = 1
            for k in range(i, j+1):
                prod *= arr[k]
            sum += prod
    return sum

print(sum_Of_Subarray_Prod([1,2,3]))
/python/leetcode/easy/1410_HTML_entity_parser.py
"""
Given a string s representing an HTML page, return the decoded string.

The encoding rule is:

& represents the character ">"
< represents the character "<"
" represents the character '"'
' represents the character "'"

Any other character is not changed.

Example 1:

Input: s = "&amp; is an HTML entity but &ambassador; is not."
Output: "& is an HTML entity but &ambassador; is not."
Explanation: The string "&amp; is an HTML entity but &ambassador; is not."
contains 4 entities of type "&": "&", "&amp;", "&ambassador;" and "&not;".
The first is decoded as ">", the second as "&", the third as "ambassador" and the fourth as "not".

Example 2:

Input: s = "and I quote: &quot;...&quot;"
Output: "and I quote: \"...\""

Example 3:

Input: s = "Stay home! Practice on Leetcode :)"
Output: "Stay home! Practice on Leetcode :)"

Example 4:

Input: s = "x &gt; y &amp;&amp; x &lt; y is always false"
Output: "x > y && x < y is always false"

Example 5:

Input: s = "leetcode.com&frasl;problemset&frasl;all"
Output: "leetcode.com/problemset/all"

Constraints:

1 <= s.length <= 10^5
The string s consists of characters from the range [a-z, A-Z, 0-9, &, <, >, ', ", /]
The number of characters in the html string will not exceed 20000.
There will not be any extra space in the string s.
"""

class Solution:
    def entityParser(self, s: str) -> str:
        return s.replace("&quot;", '"').replace("&apos;", "'").replace("&amp;", "&").replace("&gt;", ">").replace("&lt;", "<").replace("&frasl;", "/")
/python/leetcode/easy/1436_Destination_City.py
"""
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path from cityAi to cityBi.
Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo"
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city.
The path is ["London","New York","Lima","Sao Paulo"].

Example 2:

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible paths are ["D","B","C","A"], ["B","C","A"], and ["C","A"].
"C" is the destination city.

Example 3:

Input: paths = [["A","Z"]]
Output: "Z"

Constraints:

1 <= paths.length <= 100
paths[i].length == 2
1 <= cityAi.length, cityBi.length <= 10
cityAi!= cityBi
All strings consist of lowercase and uppercase English letters and the space character.
"""

class Solution: