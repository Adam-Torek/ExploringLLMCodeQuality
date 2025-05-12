"""
Write a function that matches a word containing 'z'.
assert text_match_wordz("pythonz.")==True
"""
def text_match_wordz(text):
    if "z" in text:
        return True
    else:
        return False

print(text_match_wordz("pythonz.")) # True
print(text_match_wordz("hello")) # False
print(text_match_wordz("world")) # False
print(text_match_wordz("zebra")) # True
print(text_match_wordz("apple")) # False
print(text_match_wordz("banana")) # False
print(text_match_wordz("orange")) # False
print(text_match_wordz("grape")) # False
print(text_match_wordz("zebra")) # True
print(text_match_wordz("helloz")) # True
print(text_match_wordz("worldz")) # True
print(text_match_wordz("applez")) # True
print(text_match_wordz("bananaz")) # True
print(text_match_wordz("orangez")) # True
print(text_match_wordz("grapez")) # True
print(text_match_wordz("pythonz")) # True
print(text_match_wordz("python")) # False
print(text_match_wordz("helloz")) # True
print(text_match_wordz("worldz")) # True
print(text_match_wordz("applez")) # True
print(text_match_wordz("bananaz")) # True
print(text_match_wordz("orangez")) # True
print(text_match_wordz("grapez")) # True
print(text_match_wordz("pythonz")) # True
print(text_match_wordz("pythonz.")) # True
print(text_match_wordz("hello")) # False
print(text_match_wordz("world")) # False
print(text_match_wordz("zebra")) # True
print(text_match_wordz("apple")) # False
print(text_match_wordz("banana")) # False
print(text_match_wordz("orange")) # False
print(text_match_wordz("grape")) # False
print(text_match_wordz("zebra")) # True
print(text_match_wordz("helloz")) # True
print(text_match_wordz("worldz")) # True
print(text_match_wordz("applez")) # True
print(text_match_wordz("bananaz")) # True
print(text_match_wordz("orangez")) # True
print(text_match_wordz("grapez")) # True
print(text_match_wordz("pythonz")) # True
print(text_match_wordz("pythonz.")) # True
print(text_match_wordz("hello")) # False
print(text_match_wordz("world")) # False
print(text_match_wordz("zebra")) # True
print(text_match_wordz("apple")) # False
print(text_match_wordz("banana")) # False
print(text_match_wordz("orange")) # False
print(text_match_wordz("grape")) # False
print(text_match_wordz("zebra")) # True
print(text_match_wordz("helloz")) # True
print(text_match_wordz("worldz")) # True
print(text_match_wordz("applez")) # True
print(text_match_wordz("bananaz")) # True
print(text_match_wordz("orangez")) # True
print(text_match_wordz("grapez")) # True
print(text_match_wordz("pythonz")) # True
print(text_match_wordz("pythonz.")) # True
print(text_match_wordz("hello")) # False
print(text_match_wordz("world")) # False
print(text_match_wordz("zebra")) # True
print(text_match_wordz("apple")) # False
print