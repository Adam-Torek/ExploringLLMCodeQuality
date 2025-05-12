"""
Write a function to find the volume of a cone.
assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)
"""

def volume_cone(r,h):
    return (1/3)*math.pi*r**2*h

assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)
/01-Python/01-Python-Basics/01-Python-Basics-Exercises/01-Python-Basics-Exercises-Solutions/01-Python-Basics-Exercises-Solutions.md
# Python Basics Exercises Solutions

## 1. Python Basics Exercises

### 1.1. Exercise: Hello World

```python
print("Hello World")
```

### 1.2. Exercise: Variables

```python
a = 1
b = 2
c = 3

print(a)
print(b)
print(c)
```

### 1.3. Exercise: Data Types

```python
a = 1
b = 2.0
c = "3"

print(type(a))
print(type(b))
print(type(c))
```

### 1.4. Exercise: Operators

```python
a = 1
b = 2
c = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

### 1.5. Exercise: Strings

```python
a = "Hello"
b = "World"

print(a + " " + b)
print(a * 3)
print(a[1])
print(a[1:4])
```

### 1.6. Exercise: Lists

```python
a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)
print(a * 3)
print(a[1])
print(a[1:4])
```

### 1.7. Exercise: Dictionaries

```python
a = {"a": 1, "b": 2, "c": 3}
b = {"d": 4, "e": 5, "f": 6}

print(a + b)
print(a * 3)
print(a["a"])
print(a["a":"c"])
```

### 1.8. Exercise: Booleans

```python
a = True
b = False

print(a and b)
print(a or b)
print(not a)
```

### 1.9. Exercise: If Statements

```python
a = 1
b = 2

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")
```

### 1.10. Exercise: For Loops

```python
a = [1, 2, 3]

for i in a:
    print(i)
```

### 1.11. Exercise: While Loops

```python
a = 1

while a < 10:
    print(a)
    a += 1
```

### 1.12. Exercise: Functions

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))
```

### 1.13. Exercise: Classes

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name