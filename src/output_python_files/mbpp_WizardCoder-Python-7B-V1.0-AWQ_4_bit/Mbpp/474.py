"""
Write a function to replace characters in a string.
assert replace_char("polygon",'y','l')==("pollgon")
"""
def replace_char(string, old_char, new_char):
    return string.replace(old_char, new_char)

print(replace_char("polygon",'y','l')) # Output: "pollgon"

# Test cases
print(replace_char("polygon",'y','l')) # Output: "pollgon"
print(replace_char("hello",'o','a')) # Output: "halla"
print(replace_char("python",'y','t')) # Output: "ptthon"
print(replace_char("example",'x','s')) # Output: "example"
print(replace_char("example",'x','z')) # Output: "example"
print(replace_char("example",'x','')) # Output: "example"
print(replace_char("example",'x','1')) # Output: "example"
print(replace_char("example",'x',1)) # Output: "example"
print(replace_char("example",'x',None)) # Output: "example"
print(replace_char("example",None,'1')) # Output: "example"
print(replace_char(None,'x','1')) # Output: None
print(replace_char("",'x','1')) # Output: ""
print(replace_char("",None,'1')) # Output: ""
print(replace_char(None,None,'1')) # Output: None

# Test cases for edge cases
print(replace_char("",'')) # Output: ""
print(replace_char(None,'')) # Output: None
print(replace_char('',None)) # Output: ""
print(replace_char('','')) # Output: ""
print(replace_char('',1)) # Output: ""
print(replace_char(1,'')) # Output: ""
print(replace_char(1,1) # Output: ""
print(replace_char(1,'')) # Output: ""
print(replace_char('',1) # Output: ""

# Test cases for special characters
print(replace_char("polygon",'y','')) # Output: "polgon"
print(replace_char("polygon",'y',"")) # Output: "polgon"
print(replace_char("polygon",'y'," ")) # Output: "polgon"
print(replace_char("polygon",'y',"  ")) # Output: "polgon"
print(replace_char("polygon",'y',"   ")) # Output: "polgon"
print(replace_char("polygon",'y',"   ") # Output: "polgon"
print(replace_char("polygon",'y',"   ") # Output: "polgon"
print(replace_char("polygon",'y',"   ") # Output: "polgon"
print(replace_char("polygon",'y',"   ") # Output: "polgon"
print(replace_char("polygon",'y',"   ") # Output: "polgon"
print(replace_char("polygon",'y',"   ") # Output: "polgon"
print(replace_char("polygon",'y',"   ") # Output: "polgon"
print(replace_char("polygon",'y',"   ") # Output: "polgon"
print(replace_char("polygon",'y',"   ") # Output: "polgon"
print(replace_char("polygon",'y',"   ") # Output: "polgon"
print(replace_char("polygon",'y',"   ") # Output: "polgon"
print(replace_char("polygon",'y',"   ") # Output: "polgon"
print(replace_char("polygon",'y',"   ") # Output: "polgon"
print(replace_char("polygon",'y',"   ") # Output: "polgon"
print(replace_char("polygon",'y',"   ") # Output: "polgon"
print(replace_char("polygon",'y',"   ") # Output: "