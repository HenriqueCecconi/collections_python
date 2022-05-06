class Account():
    
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0
    
    def __str__(self):
        return f'>>Account Number: {self.account_number}, Balance: {self.balance}<<'
        
    def deposit(self, value):
        self.balance += value


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