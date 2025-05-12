"""
Write a function to remove lowercase substrings from a given string.
assert remove_lowercase("PYTHon")==('PYTH')
"""

def remove_lowercase(s):
    return ''.join([c for c in s if c.isupper()])

print(remove_lowercase("PYTHon"))
/python/leetcode/easy/1410.html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>1410. HTML Entity Parser</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="main.css" />
    <script src="main.js"></script>
</head>
<body>
    <h1>1410. HTML Entity Parser</h1>
    <p>HTML entity parser is the parser that takes a string and replaces all the entities of the string with the characters that they represent. The entities that need to be replaced are (&amp;, &lt;, &gt;, and &quot;). Write a function that takes in a string and returns the string after the entities have been replaced.</p>
    <p>For example, if the string that is passed in is &quot;&amp;amp; is an HTML entity but &amp; is not an HTML entity, then the complete string will be returned &quot;&amp; is an HTML entity but &amp; is not an HTML entity.&quot;.</p>
    <p>Constraints:</p>
    <ul>
        <li>n &lt;= 1000</li>
        <li>Time and space complexity should be O(n).</li>
    </ul>
    <p>Example 1:</p>
    <pre><code>Input: s = &quot;&amp;amp; is an HTML entity but &amp; is not an HTML entity&quot;
Output: &quot;&amp; is an HTML entity but &amp; is not an HTML entity&quot;
Explanation: The parser will replace the &amp; entity by &quot;&amp;&quot;.</code></pre>
    <p>Example 2:</p>
    <pre><code>Input: s = &quot;and I quote: &quot; &amp;quot;... and I&quot; &amp;quot;...&quot; &amp;quot;!&quot; &amp;quot;&quot;
Output: &quot;and I quote: &quot;... and I&quot;...&quot;!&quot;&quot;</code></pre>
    <p>Example 3:</p>
    <pre><code>Input: s = &quot;Stay home&amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt; &amp;lt;