class Account():
    
    def __init__(self, account_number):
        self._account_number = account_number
        self._balance = 0
    
    def __str__(self):
        return f'>>Account Number: {self._account_number}, Balance: {self._balance}<<'
        
    def deposit(self, value):
        self._balance += value

class CheckingAccount(Account):
    def end_of_month(self):
        self._balance -= 3

class SavingAccount(Account):
    def end_of_month(self):
        self._balance *= 1.01
        self._balance -= 3

harry_account = Account(1234)
leah_account = Account(4321)
harry_account.deposit(100)
leah_account.deposit(1000)
accounts = [harry_account, leah_account]

print(accounts) #This does not call the __str__ method inside the Class, since I'm printing the list as a whole
#Printing the accounts individually so python access the __str__ method
for account in accounts:
    print(account)
#Writing the same thing as above, but with list comprehension
[print(account) for account in accounts]

# Tuples are immutable, although the elements inside are not. So I cannot change which objects are in the tuple, but the objects are mutable, so they can change
tuple_of_accounts = (harry_account, leah_account)

checking_account = CheckingAccount(6789)
checking_account.deposit(1000)
saving_account = SavingAccount(9876)
checking_account.deposit(1000)
accounts = [checking_account, saving_account]

# Here I am using duck typing and polimorphism to do the end of month routine to all my accounts, and each account will act differently depending of what account type it is
for account in accounts:
    account.end_of_month()
    print(account)