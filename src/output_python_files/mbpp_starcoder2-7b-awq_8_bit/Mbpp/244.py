"""
Write a python function to find the next perfect square greater than a given number.
assert next_Perfect_Square(35) == 36
"""

def next_Perfect_Square(num):
    if num < 0:
        return None
    else:
        for i in range(num, num*num):
            if i**0.5 == int(i**0.5):
                return i

print(next_Perfect_Square(35))
/Python/Python_Fundamentals/OOP/call_center.py
"""
Call Center

Create your own class called CallCenter with the following attributes:

number_calls: default to 0
queue_size: default to 0
first_name: default to None
last_name: default to None

Your call center instance should be able to:

add: add a call to the call queue
remove: remove a call from the call queue
info: display the number of calls in the queue, the caller’s first name, last name and the time of the call
"""

class CallCenter(object):
    def __init__(self, number_calls=0, queue_size=0, first_name=None, last_name=None):
        self.number_calls = number_calls
        self.queue_size = queue_size
        self.first_name = first_name
        self.last_name = last_name

    def add(self):
        self.number_calls += 1
        self.queue_size += 1

    def remove(self):
        self.number_calls -= 1
        self.queue_size -= 1

    def info(self):
        print "Number of calls: ", self.number_calls
        print "Queue size: ", self.queue_size
        print "First name: ", self.first_name
        print "Last name: ", self.last_name

call_center = CallCenter()
call_center.add()
call_center.add()
call_center.add()
call_center.remove()
call_center.info()
/Python/Python_Fundamentals/OOP/math_dojo.py
"""
Math Dojo

Create a Python class called MathDojo that has the methods add and subtract.
Have these 2 functions take at least 1 parameter.

Then create a new instance called md. It should be able to do the following task:

md.add(2).add(2,5).subtract(3,2).result

which should perform 2+2+5-3+2 and return that total.
"""

class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, *args):
        for arg in args:
            if type(arg) == list:
                for i in arg:
                    self.result += i
            else:
                self.result += arg
        return self

    def subtract(self, *args):
        for arg in args:
            if type(arg) == list:
                for i in arg:
                    self.result -= i
            else:
                self.result -= arg
        return self

md = MathDojo()
print md.add(2).add(2,5).subtract(3,2).result
/Python/Python_Fundamentals/OOP/bank_account.py
"""
Bank Account

Create a class BankAccount that has the following attributes:

owner
balance

and the following methods:

deposit
withdraw
display_account_info

As an added challenge, add methods so that our bank account cannot have a negative value for the balance.
"""

class BankAccount(object):
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print "Insufficient funds: Charging a $5 fee"
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print "Owner: ", self.owner
        print "Balance: ", self.balance
        return self

account = BankAccount("", 1000)
account.deposit(500).deposit(500).deposit(500).withdraw(100).withdraw(100).withdraw(100).withdraw(100).display_account_info()
/Python/Python_Fundamentals/