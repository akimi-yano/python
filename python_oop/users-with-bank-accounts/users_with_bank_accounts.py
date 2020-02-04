class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount(int_rate=0.02, balance=0)

    # def make_deposit(self, amount):
    #     if amount>0:
    #         self.account_balance += amount
    #         print("desposit of $" + str(amount) +" completed")
    #     else:
    #         print("amount tyring to widthdraw is smaller than or equal to $0")
    #     return self
    # def make_withdrawal(self, amount):
    #     if amount>0 and amount<self.account_balance:  
    #         self.account_balance -= amount
    #         print("withdrawal of $" + str(amount) +" completed")
    #     elif amount <=0:
    #         print("amount tyring to widthdraw is smaller than or equal to $0")
    #     else:
    #         print(str(self.name) + "'s current balance is smaller than the amount trying to withdraw")
    #     return self
    # def display_user_balance(self):
    #     print(str(self.name) + "'s current balance is $" + str(self.account_balance))
    #     return self
    def transfer_money(self, other_user, amount):
        if amount<self.account.account_balance:
            self.account.account_balance -= amount
            other_user.account.account_balance += amount
            print(str(self.name) + " successfully transferred $" + str(amount) + " to "+ str(other_user.name))
            print(str(self.name) + "'s current balance is $" + str(self.account.account_balance))
            print(str(other_user.name) + "'s current balance is $" + str(other_user.account.account_balance))
        else:
            print(str(self.name) + "'s current balance is smaller than the amount trying to transfer")
        return self

class BankAccount:
    def __init__(self, balance = 0, int_rate = 0.01):
        self.account_balance = balance
        self.int_rate = int_rate
	
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

# akimi=BankAccount(100)
# akimi.deposit(100).deposit(100).withdraw(100).yield_interest().display_account_info()

# akari=BankAccount(200)
# akari.deposit(100).deposit(100).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()

# yuta=BankAccount(0)
# yuta.withdraw(100).display_account_info()
		
# # #USER1
akimi = User("Akimi", "akimi@gmail.com")
# print(akimi.name)
# print(akimi.email)

akimi.account.deposit(1000).deposit(200).deposit(1000).withdraw(100).yield_interest().display_account_info()
glen = User("Glen", "glen@gmail.com")

akimi.transfer_money(glen, 2142)


# # # # #USER2
# yuta = User("Yuta", "yuta@gmail.com")
# print(yuta.name)
# yuta.make_deposit(1000)
# yuta.make_deposit(1000)
# yuta.make_withdrawal(500)
# yuta.make_withdrawal(500)
# yuta.display_user_balance()

# # # # #USER3
# print(glen.name)
# glen.make_deposit(1000) 
# glen.make_withdrawal(500) 
# glen.make_withdrawal(500) 
# glen.make_withdrawal(500) 
# glen.display_user_balance()

# # #Transfer Money
# akimi.transfer_money(glen,100)





