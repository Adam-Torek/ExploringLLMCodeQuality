from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
/README.md
# Python Data Science

This repository contains my notes and exercises from the book [Python Data Science Cookbook](https://www.packtpub.com/application-development/python-data-science-cookbook) by.

## Chapter 1: Introduction to Python

### 1.1.1. Hello World

```python
print("Hello World!")
```

### 1.1.2. Variables

```python
x = 10
y = 20
z = x + y
print(z)
```

### 1.1.3. Data Types

```python
x = 10
y = 20
z = x + y
print(z)
```

### 1.1.4. Operators

```python
x = 10
y = 20
z = x + y
print(z)
```

### 1.1.5. Control Flow

```python
x = 10
y = 20
z = x + y
print(z)
```

### 1.1.6. Functions

```python
def add(x, y):
    return x + y

x = 10
y = 20
z = add(x, y)
print(z)
```

### 1.1.7. Modules

```python
import math

x = 10
y = 20
z = math.sqrt(x) + math.sqrt(y)
print(z)
```

### 1.1.8. Classes

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(10, 20)
print(p)
```

## Chapter 2: Data Structures

### 2.2.1. Lists

```python
x = [1, 2, 3, 4, 5]
print(x)
```

### 2.2.2. Tuples

```python
x = (1, 2, 3, 4, 5)
print(x)
```

### 2.2.3. Sets

```python
x = {1, 2, 3, 4, 5}
print(x)
```

### 2.2.4. Dictionaries

```python
x = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print(x)
```

### 2.2.5. Comprehensions

```python
x = [i for i in range(1, 6)]
print(x)
```

### 2.2.6. Iterators

```python
x = [i for i in range(1, 6)]
for i in x:
    print(i)
```

### 2.2.7. Generators

```python
x = (i for i in range(1, 6))
for i in x:
    print(i)
```

### 2.2.8. Itertools

```python
import itertools

x = [1, 2, 3, 4, 5]
y = itertools.cycle(x)
for i in y:
    print(i)
```

### 2.2.9. Collections

```python
import collections

x = [1, 2, 3, 4, 5]
y = collections.Counter(x)
print(y)
```

## Chapter 3: Data Manipulation

### 3.3.1. Sorting

```python
x = [1, 2