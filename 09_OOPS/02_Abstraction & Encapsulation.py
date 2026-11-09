# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance

class Account:
    #   Encapsulation
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self, amt):
        self.balance -= amt
        print("Rs.", amt, "was debited!")

    def credit(self, amt):
        self.balance += amt
        print("Rs.", amt, "was credited!")

    def get_balance(self):
        print("The remaining balance is:", self.balance)

user1 = Account(5000, 123456)
user1.debit(2000)       #   Abstraction
user1.credit(5000)
user1.get_balance()