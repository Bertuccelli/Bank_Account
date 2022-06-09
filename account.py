# from user import bank_account


class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        # BankAccount.all_balances.append(self)
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
            self.balance -= amount
    def display_account_info(self):
        print("Balance:", self.balance )
    def yield_interest(self):
        self.balance += self.balance * self.int_rate
    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_balances:
            sum += account.balance
        return sum

user1 = BankAccount(0.01500, 100)
user2 = BankAccount(0.01500, 100)

user1.deposit(600).deposit(150).withdraw(80).deposit(120).display_account_info()

user2.deposit(650).deposit(800).withdraw(120).withdraw(50).withdraw(200).withdraw(200).yield_interest.display_account_info()

