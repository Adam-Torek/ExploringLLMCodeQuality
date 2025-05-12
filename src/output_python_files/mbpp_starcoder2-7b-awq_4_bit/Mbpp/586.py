"""
Write a python function to split a list at the nth eelment and add the first part to the end.
assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
"""

def split_Arr(arr,n):
    return arr[n:] + arr[:n]

print(split_Arr([12,10,5,6,52,36],2))/Python/Python_Fundamentals/OOP/call_center.py
"""
Call Center

Create your own class called CallCenter with the following attributes:

Make three methods:

call(): makes a new call object
answer(): answers a call
reject(): rejects a call
Have your CallCenter class also have the following attributes:

calls: the number of unanswered calls
queue_size: the number of calls in the queue
If someone calls and there are no available agents to answer the call, the call should be placed in the queue.

If an agent answers a call, remove them from the queue and the call is no longer in the queue.

"""

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = 0

    def call(self):
        self.calls.append(self.queue_size)
        self.queue_size += 1
        return self

    def answer(self):
        if self.queue_size > 0:
            self.queue_size -= 1
            return self
        else:
            return "No calls in queue"

    def reject(self):
        if self.queue_size > 0:
            self.queue_size -= 1
            return self
        else:
            return "No calls in queue"

call_center = CallCenter()
call_center.call().call().call().answer().reject().answer().reject()
print(call_center.calls)
print(call_center.queue_size)/Python/Python_Fundamentals/OOP/math_dojo.py
"""
Math Dojo

Create a Python class that does the following:

has data members called "integers" and "sum" that are both initially set to zero
has an instance method called "add" that takes any number of arguments.
"add" should increase "sum" by the sum of all its arguments; it should also increase "integers" by the number of its arguments.
has an instance method called "subtract" that takes at least one argument. "subtract" should decrease "sum" by the sum of all its arguments; it should also decrease "integers" by the number of its arguments.
If there is no "subtract" method, your class should print out the "sum" and "integers" data members.

"""

class MathDojo(object):
    def __init__(self):
        self.integers = 0
        self.sum = 0

    def add(self, *args):
        for arg in args:
            if isinstance(arg, list):
                for i in arg:
                    self.sum += i
                    self.integers += 1
            else:
                self.sum += arg
                self.integers += 1
        return self

    def subtract(self, *args):
        for arg in args:
            if isinstance(arg, list):
                for i in arg:
                    self.sum -= i
                    self.integers -= 1
            else:
                self.sum -= arg
                self.integers -= 1
        return self

math = MathDojo()
print(math.add(2).add(2,5).subtract(3,2).sum)
print(math.integers)/Python/Python_Fundamentals/OOP/bank_account.py
"""
Bank Account

Create a class BankAccount that has the following attributes:

owner
balance

and the following methods:

deposit(amount) - increases the account balance by the given amount and returns the new balance
withdraw(amount) - decreases the account balance by the given amount if there are sufficient funds and returns the new balance
display_account_info() - print to the console, "Account owner: name", "Account balance: balance"

"""

class BankAccount(object):
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):