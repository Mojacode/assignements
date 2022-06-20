# class BankAccount:
#     interest_rate= 1.01
#     balance= 0
#     def __init__(self, int_rate, balance): 
#         self.interest= int_rate
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         return self

#     def withdraw(self, amount):
#         if self.balance >= 0:
#             self.balance -= amount
#         else:
#             print ("Insufficient funds: Charging a $5 fee")
#             self.balance -= 5
#         return self

#     def display_account_info(self):
#         print(f"Balance {self.balance}")

#     def yield_interest(self):
#         self.balance = self.balance * BankAccount.interest_rate
#         return self

#     # @classmethod
#     # def showallacc(cls):
#     #     print(cls.display_account_info)
#     #     print(cls.display_account_info)

# acc1 = BankAccount(0 , 200)
# acc2 = BankAccount(0 ,300)

# acc1.deposit(50).deposit(50).deposit(50).withdraw(100).yield_interest().display_account_info()
# acc2.deposit(90).deposit(21).withdraw(50).withdraw(10).withdraw(11).withdraw(22).yield_interest().display_account_info()

# # BankAccount.showallacc()

class BankAccount:
    accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()


savings = BankAccount(.05,1000)
checking = BankAccount(.02,5000)

savings.deposit(10).deposit(20).deposit(40).withdraw(600).yeild_interest().display_account_info()
checking.deposit(100).deposit(200).deposit(400).withdraw(60).yeild_interest().display_account_info()

BankAccount.print_all_accounts()



