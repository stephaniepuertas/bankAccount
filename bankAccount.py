# The class should also have the following methods:
    # deposit(self, amount) - increases the account balance 
    # by the given amount
    # withdraw(self, amount) - decreases the account balance by the 
            # given amount if there are sufficient funds; 
            # if there is not enough money, print a message 
            # "Insufficient funds: Charging a $5 fee" and deduct $5
    # display_account_info(self) - print to the console: eg. "Balance: $100"
    # yield_interest(self) - increases the account balance 
            # by the current balance * the interest rate (as long as the balance is positive)

class BankAccount:
    def __init__(self, int_rate, balance=0):
        # properties/attributes
        self.int_rate=int_rate
        self.balance=balance


    def deposit(self, amount):
        self.balance+=amount
        return self


    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            self.balance-=5
            print("Insufficient Funds")
        return self


    # static methods have no access to any attribute
    # only to what is passed into it
    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

    def display_account_info(self):
        print (self.balance)
        return self

    def yield_interest(self):
        if (self.balance) > 0: 
            self.balance += self.balance *self.int_rate
        return self


# sample bank acc
# bankaccount1=BankAccount(.02,100)
# bankaccount1.yield_interest()
# bankaccount1.display_account_info()


# create two accounts:
#acc 1
bankaccount1=BankAccount(.02,0)
bankaccount1.deposit(50).deposit(50).deposit(5).withdraw(5).yield_interest().display_account_info()


#acc2
bankaccount2=BankAccount(.05,100)
bankaccount2.deposit(100).deposit(100).withdraw(5).withdraw(5).withdraw(5).withdraw(5).yield_interest().display_account_info()
