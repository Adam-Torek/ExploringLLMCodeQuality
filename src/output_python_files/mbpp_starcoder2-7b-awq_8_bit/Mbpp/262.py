"""
Write a function that takes in a list and an integer L and splits the given list into two parts where the length of the first part of the list is L, and returns the resulting lists in a tuple.
assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])
"""

def split_two_parts(lst,L):
    return lst[:L],lst[L:]

print(split_two_parts([1,1,2,3,4,4,5,1],3))/Python/Python_Fundamentals/OOP/User.py
class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self,amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self

    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

# user1 = User("", "")
# user2 = User("", "")
# user3 = User("", "")

# user1.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(50).display_user_balance()
# user2.make_deposit(100).make_deposit(100).make_withdrawal(50).make_withdrawal(50).display_user_balance()
# user3.make_deposit(100).make_withdrawal(50).make_withdrawal(50).make_withdrawal(50).display_user_balance()

# user1.transfer_money(user2,50)
# user1.display_user_balance()
# user2.display_user_balance()

# user1.transfer_money(user3,50)
# user1.display_user_balance()
# user3.display_user_balance()/Python/Python_Fundamentals/OOP/BankAccount.py
class BankAccount:
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

# account1 = BankAccount(0.02,1000)
# account1.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest().display_account_info()

# account2 = BankAccount(0.02,1000)
# account2.deposit(100).deposit(100).withdraw(50).withdraw(50).yield_interest().display_account_info()

# account3 = BankAccount(0.02,1000)
# account3.deposit(100).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()

# account1.transfer_money(account2,50)
# account1.display_account_info()
# account2.display_account_info()

# account1.transfer_money(account3,50)
# account1.display_account_info()
# account3.display_account_info()/Python/Python_Fundamentals/OOP/MathDojo.py
class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self,num,*nums):
        self.result += num
        for num in nums:
            self.result += num
        return self

    def subtract(self,num,*nums):
        self.result -= num