"""
Write a function to remove odd characters in a string.
assert remove_odd("python")==("yhn")
"""

def remove_odd(s):
    return "".join([c for i,c in enumerate(s) if i%2==0])

print(remove_odd("python"))
/python/leetcode/easy/1410.html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>1410. HTML Entity Parser</title>
    <link rel="stylesheet" href="http://yui.yahooapis.com/3.18.1/build/cssgrids/cssgrids-min.css">
    <link rel="stylesheet" href="../assets/vendor/prettify/prettify-min.css">
    <link rel="stylesheet" href="../assets/css/main.css" id="site_styles">
    <link rel="stylesheet" href="../assets/css/question.css">
    <link rel="stylesheet" href="../assets/css/answer.css">
</head>
<body>

<div class="goal_prompt">
    <div class="nav">
        <a href="../index.html">LeetCode</a>
        <a href="index.html">Easy</a>
        <a href="1410.html">1410. HTML Entity Parser</a>
    </div>
</div>

<div class="question">
    <h2>1410. HTML Entity Parser</h2>

    <div class="question-description">
        <p>Given a string representing an HTML entity, return the entity's corresponding character.</p>

        <p>The valid HTML entities are <code>&quot;amp&quot;</code>, <code>&quot;lt&quot;</code>, <code>&quot;gt&quot;</code>, <code>&quot;quot&quot;</code>, <code>&quot;apos&quot;</code>, <code>&quot;AElig&quot;</code>, <code>&quot;Aacute&quot;</code>, <code>&quot;Acirc&quot;</code>, <code>&quot;Agrave&quot;</code>, <code>&quot;Aring&quot;</code>, <code>&quot;Atilde&quot;</code>, <code>&quot;Auml&quot;</code>, <code>&quot;Ccedil&quot;</code>, <code>&quot;ETH&quot;</code>, <code>&quot;Eacute&quot;</code>, <code>&quot;Ecirc&quot;</code>, <code>&quot;Egrave&quot;</code>, <code>&quot;Euml&quot;</code>, <code>&quot;Iacute&quot;</code>, <code>&quot;Icirc&quot;</code>, <code>&quot;Igrave&quot;</code>, <code>&quot;Iuml&quot;</code>, <code>&quot;Ntilde&quot;</code>, <code>&quot;Oacute&quot;</code>, <code>&quot;Ocirc&quot;</code>, <code>&quot;Ograve&quot;</code>, <code>&quot;Oslash&quot;</code>, <code>&quot;Otilde&quot;</code>, <code>&quot;Ouml&quot;</code>, <code>&quot;THORN&quot;</code>, <code>&quot;Uacute&quot;</code>, <code>&quot;Ucirc&quot;</code>, <code>&quot;Ugrave&quot;</code>, <code>&quot;Uuml&quot;</code>, <code>&quot;Yacute&quot;</code>, <code>&quot;Yuml&quot;</code>, <code>&quot;aacute&quot;</code>, <code>&quot;acirc&quot;</code>, <code>&quot;aelig&quot;</code>, <code>&quot;agrave&quot;</code>, <code>&quot;aring&quot;</code>, <code>&quot;atilde&quot;</code>, <code>&quot;auml&quot;</code>, <code>&quot;ccedil&quot;</code>, <code>&quot;eacute&quot;</code>, <code>&quot;ecirc&quot;</code>, <code>&quot;egrave&quot;</code>, <code>&quot;euml&quot;</code>, <code>&quot;eth&quot;</code>, <code>&quot;iacute&quot;</code>, <code>&quot;icirc&quot;</code>, <code>&quot;igrave&quot;</code>, <code