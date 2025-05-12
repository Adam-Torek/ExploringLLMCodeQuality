"""
Write a function that takes in two tuples and performs mathematical division operation element-wise across the given tuples.
assert division_elements((10, 4, 6, 9),(5, 2, 3, 3)) == (2, 2, 2, 3)
"""

def division_elements(tuple1, tuple2):
    return tuple(x / y for x, y in zip(tuple1, tuple2))

print(division_elements((10, 4, 6, 9),(5, 2, 3, 3)))/Python/Python_Fundamentals/OOP/User.py
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

# user1 = User("", "")
# user2 = User("", "")
# user3 = User("", "")

# user1.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()
# user2.make_deposit(100).make_deposit(200).make_withdrawal(50).make_withdrawal(50).display_user_balance()
# user3.make_deposit(100).make_withdrawal(50).make_withdrawal(50).make_withdrawal(50).display_user_balance()

# user1.transfer_money(user2, 100)
# user1.display_user_balance()
# user2.display_user_balance()

# user1.transfer_money(user3, 100)
# user1.display_user_balance()
# user3.display_user_balance()

# user2.transfer_money(user3, 100)
# user2.display_user_balance()
# user3.display_user_balance()

# user1.transfer_money(user2, 100)
# user1.display_user_balance()
# user2.display_user_balance()

# user1.transfer_money(user3, 100)
# user1.display_user_balance()
# user3.display_user_balance()

# user2.transfer_money(user3, 100)
# user2.display_user_balance()
# user3.display_user_balance()

# user1.transfer_money(user2, 100)
# user1.display_user_balance()
# user2.display_user_balance()

# user1.transfer_money(user3, 100)
# user1.display_user_balance()
# user3.display_user_balance()

# user2.transfer_money(user3, 100)
# user2.display_user_balance()
# user3.display_user_balance()

# user1.transfer_money(user2, 100)
# user1.display_user_balance()
# user2.display_user_balance()

# user1.transfer_money(user3, 100)
# user1.display_user_balance()
# user3.display_user_balance()

# user2.transfer_money(user3, 100)
# user2.display_user_balance()
# user3.display_user_balance()

# user1.transfer_money(user2, 100)
# user1.display_user_balance()
# user2.display_user_balance()

# user1.transfer_money(user3,