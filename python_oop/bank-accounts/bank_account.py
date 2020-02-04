
class BankAccount:
    def __init__(self, balance = 0, interest = 0.01):
        self.account_balance = balance
        self.int_rate = interest
	
    def deposit(self, amount):
        if amount>0:
            self.account_balance += amount
            print("+$" + str(amount))
           
        else:
            print("trying to deposit less than ore equal to $0")
        return self
        
    def withdraw(self, amount):
        if amount>0:
            if amount>self.account_balance:
                print("Insufficient funds: Charging a $5 fee")
                self.account_balance -= 5
            else:
                self.account_balance -= amount
                print("-$" + str(amount))
        else:
            print("trying to withdraw less than ore equal to $0")
        return self
                
    def yield_interest(self):
        if self.account_balance>0:
            self.int_rate += self.account_balance* self.int_rate
        else:
            self.int_rate = 0
        print("+$" + str(self.int_rate))
        self.account_balance += self.int_rate
        return self
    
    def display_account_info(self):
        print("Balance: $" + str(self.account_balance))
        return self

akimi=BankAccount(100)
akimi.deposit(100).deposit(100).withdraw(100).yield_interest().display_account_info()

akari=BankAccount(200)
akari.deposit(100).deposit(100).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()

yuta=BankAccount(0)
yuta.withdraw(100).display_account_info()
		
