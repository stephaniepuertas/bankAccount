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
        pass



    def yield_interest(self):
        pass

