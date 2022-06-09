class User:
    # class attributes get defined in the class
    bank_name = "First National Dojo"
    # now our method has two paremeters
    def __init__(self, name, email_address):
        # we assign them accordingly
        self.name = name
        self.email = email_address
        # the balance is set to $0
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.name)
print(guido.bank_name)
print(guido.account_balance)
print(monty.name)
print(monty.bank_name)
print(monty.account_balance)

# guido.bank_name = "Dojo Credit Union"
# User.bank_name = "Bank of Dojo"

class bank_account:
    bank_name = "first National Dojo"
    all_accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        bank_account.all_accounts.append(self)
    def withdraw(self, amount):
        if bank_account.can_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self
    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum