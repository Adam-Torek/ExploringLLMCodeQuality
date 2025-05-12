"""
Write a python function that takes in a non-negative number and returns the number of prime numbers less than the given non-negative number.
assert count_Primes_nums(5) == 2
"""

def count_Primes_nums(num):
    if num < 2:
        return 0
    primes = [2]
    x = 3
    while x <= num:
        for y in range(3,x,2):
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    return len(primes)

print(count_Primes_nums(5))
/Python/Python_Fundamentals/OOP/call_center.py
"""
Call Center

Create your own class called CallCenter with the following attributes:

call_id
caller_name
caller_phone_number
time_of_call
reason_for_call

Create three methods:

call(): This should take in all the information from the user to create the call and append it to the call center’s queue.

def call(self, call_id, caller_name, caller_phone_number, time_of_call, reason_for_call):

display(): This should print out all the information in the call center’s queue.

def display(self):

remove(): This should remove the first call on the queue, but should also remove the call from the call center’s queue.

def remove(self):

Have the CallCenter class inherit the Queue class.

"""

class CallCenter(object):
    def __init__(self, call_id, caller_name, caller_phone_number, time_of_call, reason_for_call):
        self.call_id = call_id
        self.caller_name = caller_name
        self.caller_phone_number = caller_phone_number
        self.time_of_call = time_of_call
        self.reason_for_call = reason_for_call
        self.calls = []

    def call(self, call_id, caller_name, caller_phone_number, time_of_call, reason_for_call):
        self.calls.append(call_id, caller_name, caller_phone_number, time_of_call, reason_for_call)

    def display(self):
        for call in self.calls:
            print(call)

    def remove(self):
        self.calls.pop(0)
/Python/Python_Fundamentals/OOP/math_dojo.py
"""
Math Dojo

Create a Python class called MathDojo that has the methods add and subtract. Have these 2 functions take at least 1 parameter.

Then create a new instance called md. It should be able to do the following task:

md.add(2).add(2,5).subtract(3,2).result

which should perform 0+2+(2+5)-(3+2) and return 4.

"""

class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, *args):
        for arg in args:
            if type(arg) is list:
                for item in arg:
                    self.result += item
            else:
                self.result += arg
        return self

    def subtract(self, *args):
        for arg in args:
            if type(arg) is list:
                for item in arg:
                    self.result -= item
            else:
                self.result -= arg
        return self

md = MathDojo()
print(md.add(2).add(2,5).subtract(3,2).result)
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
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insufficient funds: Charging a