class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        if amount>0:
            self.account_balance += amount
            print("desposit of $" + str(amount) +" completed")
        else:
            print("amount tyring to widthdraw is smaller than or equal to $0")
        return self

    def make_withdrawal(self, amount):
        if amount>0 and amount<self.account_balance:  
            self.account_balance -= amount
            print("withdrawal of $" + str(amount) +" completed")
        elif amount <=0:
            print("amount tyring to widthdraw is smaller than or equal to $0")
        else:
            print(str(self.name) + "'s current balance is smaller than the amount trying to withdraw")
        return self
    
    def display_user_balance(self):
        print(str(self.name) + "'s current balance is $" + str(self.account_balance))
        return self

    def transfer_money(self, other_user, amount):
        if amount<self.account_balance:
            self.account_balance -= amount
            other_user.account_balance += amount
            print(str(self.name) + " successfully transferred $" + str(amount) + " to "+ str(other_user.name))
            print(str(self.name) + "'s current balance is $" + str(self.account_balance))
            print(str(other_user.name) + "'s current balance is $" + str(other_user.account_balance))
        else:
            print(str(self.name) + "'s current balance is smaller than the amount trying to transfer")
        return self

# #USER1
akimi = User("Akimi", "akimi@gmail.com")
print(akimi.name)
print(akimi.email)

akimi.make_deposit(1000).make_deposit(200).make_deposit(1000).make_withdrawal(100).display_user_balance()

# # # #USER2
yuta = User("Yuta", "yuta@gmail.com")
print(yuta.name)
yuta.make_deposit(1000).make_deposit(1000).make_withdrawal(500).make_withdrawal(500).display_user_balance()

# # # #USER3
glen = User("Glen", "glen@gmail.com")
print(glen.name)
glen.make_deposit(1000).make_withdrawal(500).make_withdrawal(500).make_withdrawal(500).display_user_balance()

# #Transfer Money
akimi.transfer_money(glen,100)