"""
Write a function to find the combinations of sums with tuples in the given tuple list. https://www.geeksforgeeks.org/python-combinations-of-sum-with-tuples-in-tuple-list/
assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
"""

def find_combinations(tuples):
    result = []
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            result.append((tuples[i][0] + tuples[j][0], tuples[i][1] + tuples[j][1]))
    return result

print(find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]))
/python/leetcode/easy/1410_html_entity_parser.py
"""
Given a string s representing an encoded string, return its decoded string.

The encoding rule is:

-   For each tag, add one open tag '<' and one close tag '>'.
-   If the content of a tag is empty, add a single character '>'.
-   If start and end tags are not matched, add two characters '>' to match the missing start and end tags.

Input: s = "&amp;is&amp;not&amp;a&amp;good&amp;day"
Output: "is not a good day"
Explanation: "&amp;" is converted to "&", "is" and "not" are converted to "<b>", "a" and "good" are converted to "<i>", "day" is converted to "<b>" not "<i>", so the string is "is not a good day".

Input: s = "&amp;amp;is&amp;amp;not&amp;amp;a&amp;amp;good&amp;amp;day"
Output: "&amp;is&amp;not&amp;a&amp;good&amp;day"

Input: s = "and&gt;tag"
Output: "and>tag"
Explanation: "&gt;" is converted to ">", so the string becomes "and>tag".

Input: s = "h&amp;ell&amp;o"
Output: "hello"
Explanation: "&amp;" is converted to "&", "e" and "o" are converted to "<b>", so the string becomes "hello".

Input: s = "&#60;a href='http://google.com'&#62;link&#60;/a&#62;"
Output: "<a href='http://google.com'>link</a>"
Explanation: "&#60;" is converted to "<", "&#62;" is converted to ">", "href" is converted to "href", "google.com" is converted to "google.com", "link" is converted to "<b>link</b>", so the string becomes "<a href='http://google.com'>link</a>".

Input: s = "&#60;a href='http://google.com' target='_blank'&#62;link&#60;/a&#62;"
Output: "<a href='http://google.com' target='_blank'>link</a>"
Explanation: "&#60;" is converted to "<", "&#62;" is converted to ">", "href" is converted to "href", "google.com" is converted to "google.com", "target" is converted to "target", "_blank" is converted to "_blank", "link" is converted to "<b>link</b>", so the string becomes "<a href='http://google.com' target='_blank'>link</a>".

Input: s = "&#60;img src='https://leetcode.com/problems/images/question_1410.png' alt='&#60;b&#62;html&#60;/b&#62; entity'&#62;"
Output: "<img src='https://leetcode.com/problems/images/question_1410.png' alt='<b>html</b> entity'>"
Explanation: "&#60;" is converted to "<", "&#62;" is converted to ">", "src" is converted to "src", "https://leetcode.com/problems/images/question_1410.