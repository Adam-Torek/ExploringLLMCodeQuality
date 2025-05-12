"""
Write a function that takes in a list and an integer n and splits a list for every nth element, returning a list of the resulting lists.
assert list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n'],3)==[['a', 'd', 'g', 'j','m'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
"""

def list_split(lst,n):
    return [lst[i:i+n] for i in range(0,len(lst),n)]

print(list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n'],3))/Python/Python_Fundamentals/OOP/call_center.py
"""
Call Center

Create your own class called CallCenter with the following attributes:

Call Center should have a list of calls
Call Center should have a method that adds a new call to the list of calls
Call Center should have a method that displays the call back on the call
Call Center should have a method that shows the length of the call list
Call Center should have a method that removes the call from the list of calls by index
Call Center should have a method that removes the call with the longest duration from the call list
Call Center should have a method that displays the information of all calls currently in the call list

"""

class Call(object):
    def __init__(self, id, name, number, time, reason):
        self.id = id
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
        self.list = []

    def display(self):
        print "ID: ", self.id
        print "Name: ", self.name
        print "Number: ", self.number
        print "Time: ", self.time
        print "Reason: ", self.reason
        return self

class CallCenter(object):
    def __init__(self):
        self.calls = []

    def add(self, id, name, number, time, reason):
        self.calls.append(Call(id, name, number, time, reason))
        return self

    def remove(self, index):
        self.calls.pop(index)
        return self

    def remove_longest(self):
        longest = 0
        for call in self.calls:
            if call.time > longest:
                longest = call.time
        for call in self.calls:
            if call.time == longest:
                self.calls.remove(call)
        return self

    def display(self):
        for call in self.calls:
            call.display()
        return self

call1 = Call(1, "", "555-555-5555", 10, "I'm a robot")
call2 = Call(2, "", "555-555-5555", 10, "I'm a robot")
call3 = Call(3, "", "555-555-5555", 10, "I'm a robot")
call4 = Call(4, "", "555-555-5555", 10, "I'm a robot")
call5 = Call(5, "", "555-555-5555", 10, "I'm a robot")
call6 = Call(6, "", "555-555-5555", 10, "I'm a robot")
call7 = Call(7, "", "555-555-5555", 10, "I'm a robot")
call8 = Call(8, "", "555-555-5555", 10, "I'm a robot")
call9 = Call(9, "", "555-555-5555", 10, "I'm a robot")
call10 = Call(10, "", "555-555-5555", 10, "I'm a robot")

call_center = CallCenter()
call_center.add(call1).add(call2).add(call3).add(