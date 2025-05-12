"""
Write a function to compute the n-th power of each number in a list.
assert nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""

def nth_nums(nums,n):
    return [num**n for num in nums]

print nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)
/python/python_oop/animal.py
class Animal(object):
    def __init__(self,name):
        self.name = name
        self.health = 100
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print "Health: {}".format(self.health)

class Dog(Animal):
    def __init__(self,name):
        super(Dog,self).__init__(name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self,name):
        super(Dragon,self).__init__(name)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        print "This is a dragon!"
        super(Dragon,self).display_health()

dog = Dog("Dog")
dog.walk().walk().walk().run().run().pet().display_health()

dragon = Dragon("Dragon")
dragon.walk().walk().walk().run().run().fly().fly().display_health()
/python/python_fundamentals/coin_toss.py
"""
Create a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
"""

import random

def coin_toss():
    heads = 0
    tails = 0
    for i in range(1,5001):
        if random.randint(0,1) == 0:
            heads += 1
            print "Attempt #{}: Throwing a coin... It's a head!... Got {} head(s) so far and {} tail(s) so far".format(i,heads,tails)
        else:
            tails += 1
            print "Attempt #{}: Throwing a coin... It's a tail!... Got {} head(s) so far and {} tail(s) so far".format(i,heads,tails)

coin_toss()
/python/python_fundamentals/coin_toss_2.py
"""
Create another function that simulates tossing a coin 5,000 times. Your function should print the number of heads and tails and the percentage of heads.
"""

import random

def coin_toss():
    heads = 0
    tails = 0
    for i in range(1,5001):
        if random.randint(0,1) == 0:
            heads += 1
            print "Attempt #{}: Throwing a coin... It's a head!... Got {} head(s) so far and {} tail(s) so far".format(i,heads,tails)
        else:
            tails += 1
            print "Attempt #{}: Throwing a coin... It's a tail!... Got {} head(s) so far and {} tail(s) so far".format(i,heads,tails)
    print "Ending the program. Thank you!"
    print "Heads: {}".format(heads)
    print "Tails: {}".format(tails)
    print "Percentage of heads: {}".format(float(heads)/5000)

coin_toss()
/python/python_fundamentals/coin_toss_3.py
"""
Create a function that simulates tossing a coin 5,000 times. Your function should return the percentage of heads.
"""

import random

def coin_toss():
    heads = 0
    tails = 0
    for i in range(1,5001):
        if random.randint(0,1) ==