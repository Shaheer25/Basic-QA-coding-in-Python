class Bank:
    def __init__(self,balance,accountNumber):
        self.balance = balance
        self.accountNumber=accountNumber

    def deposit(self, amount):
        self.balance += amount
        return "balance:",self.balance

    def withdraw(self,amount):
        if amount > self.balance:
            return "Insufficient Balance"
        else:
            self.balance-=amount
            return "balance:",self.balance


accountNumber = int(input("Enter Your Account Number"))
balance = int(input("Enter Your Balance"))
shaheer= Bank(accountNumber,balance)


choice = int(input("Enter you Choice\n1.Account Info\n2.Check Balance\n3.deposit\n4.withdraw\n"))

if choice == 1:
    print("Account Number",shaheer.accountNumber)
elif choice==2:
    print("balance:",shaheer.balance,)
elif choice==3:
    amount = int(input("Enter the Amount to Deposit"))
    print(shaheer.deposit(amount))
elif choice == 4:
    amount = int(input("Enter the Amount to Withdraw"))
    print(shaheer.withdraw(amount))
