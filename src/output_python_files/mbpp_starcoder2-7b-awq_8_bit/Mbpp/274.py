"""
Write a python function that takes in a positive integer n and finds the sum of even index binomial coefficients.
assert even_binomial_Coeff_Sum(4) == 8
"""

def even_binomial_Coeff_Sum(n):
    sum = 0
    for i in range(0, n+1, 2):
        sum += binomial_Coeff(n, i)
    return sum

print(even_binomial_Coeff_Sum(4))
/Python/Python_Fundamentals/OOP/call_center.py
class Call(object):
    def __init__(self, unique_id, caller_name, caller_phone_number, time_of_call, reason_for_call):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.caller_phone_number = caller_phone_number
        self.time_of_call = time_of_call
        self.reason_for_call = reason_for_call

    def display(self):
        print "Unique ID: " + str(self.unique_id)
        print "Caller Name: " + self.caller_name
        print "Caller Phone Number: " + self.caller_phone_number
        print "Time of Call: " + self.time_of_call
        print "Reason for Call: " + self.reason_for_call

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = 0

    def add(self, call):
        self.calls.append(call)
        self.queue_size += 1
        return self

    def remove(self):
        self.calls.pop(0)
        self.queue_size -= 1
        return self

    def info(self):
        for call in self.calls:
            call.display()
        print "Queue Size: " + str(self.queue_size)
        return self

    def sort_by_time(self):
        self.calls.sort(key=lambda call: call.time_of_call)
        return self

    def sort_by_name(self):
        self.calls.sort(key=lambda call: call.caller_name)
        return self

    def sort_by_phone(self):
        self.calls.sort(key=lambda call: call.caller_phone_number)
        return self

    def sort_by_reason(self):
        self.calls.sort(key=lambda call: call.reason_for_call)
        return self

call1 = Call(1, "", "555-555-5555", "12:00", "I need to talk to you")
call2 = Call(2, "", "555-555-5555", "12:00", "I need to talk to you")
call3 = Call(3, "", "555-555-5555", "12:00", "I need to talk to you")
call4 = Call(4, "", "555-555-5555", "12:00", "I need to talk to you")
call5 = Call(5, "", "555-555-5555", "12:00", "I need to talk to you")
call6 = Call(6, "", "555-555-5555", "12:00", "I need to talk to you")
call7 = Call(7, "", "555-555-5555", "12:00", "I need to talk to you")
call8 = Call(8, "", "555-555-5555", "12:00", "I need to talk to you")
call9 = Call(9, "", "555-555-5555", "12:00", "I need to talk to you")
call10 = Call(10, "", "555-555-5555", "12:00", "I need to talk to you")

call_center = CallCenter()
call_center.add(call1).add(call2).add(call3).add(call4).add(call5).add(call6).add(call7).add(call8).add(call9).