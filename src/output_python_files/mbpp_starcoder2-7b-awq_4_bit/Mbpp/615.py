"""
Write a function which takes a tuple of tuples and returns the average value for each tuple as a list.
assert average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)))==[30.5, 34.25, 27.0, 23.25]
"""

def average_tuple(tup):
    return [sum(i)/len(i) for i in tup]

print(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))))
/Python/Python_Fundamentals/OOP/call_center.py
"""
Call Center

Create your own class called CallCenter that will simulate the call center by creating call objects as it receives them.

Your call center instance should be able to:

Add calls
Remove calls
Does a call exist?
What is the length of the call center?
"""

class CallCenter(object):
    def __init__(self):
        self.calls = []

    def add(self, call):
        self.calls.append(call)
        return self

    def remove(self, call):
        self.calls.remove(call)
        return self

    def info(self):
        print "There are {} calls in the queue".format(len(self.calls))
        return self

    def display(self):
        for call in self.calls:
            print "Caller: {}, ID: {}, Time: {}, Reason: {}".format(call.caller_name, call.caller_id, call.time, call.reason)
        return self

class Call(object):
    def __init__(self, caller_name, caller_id, time, reason):
        self.caller_name = caller_name
        self.caller_id = caller_id
        self.time = time
        self.reason = reason

call1 = Call("", "1234567890", "10:00", "I need help")
call2 = Call("", "1234567890", "10:00", "I need help")
call3 = Call("", "1234567890", "10:00", "I need help")
call4 = Call("", "1234567890", "10:00", "I need help")
call5 = Call("", "1234567890", "10:00", "I need help")

call_center = CallCenter()
call_center.add(call1).add(call2).add(call3).add(call4).add(call5).info().display()
/Python/Python_Fundamentals/OOP/math_dojo.py
"""
Math Dojo

Create a Python class that does the following:

has data members called "integers" and "sum" that are both initially 0 for each instance of the class
has an instance method called add that takes any number of arguments. add adds each argument to the "sum" data member
has an instance method called subtract that takes any number of arguments. subtract subtracts each argument from the "sum" data member
"""

class MathDojo(object):
    def __init__(self):
        self.integers = 0
        self.sum = 0

    def add(self, *args):
        for arg in args:
            if type(arg) == list or type(arg) == tuple:
                for i in arg:
                    self.integers += i
            else:
                self.integers += arg
        self.sum += self.integers
        return self

    def subtract(self, *args):
        for arg in args:
            if type(arg) == list or type(arg) == tuple:
                for i in arg:
                    self.integers -= i
            else:
                self.integers -= arg
        self.sum -= self.integers
        return self

md = MathDojo()
print md.add(2).add(2,5).subtract(3,2).sum
/Python/Python_Fundamentals/OOP/bank_account.py
"""