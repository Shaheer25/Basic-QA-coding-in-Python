class Bank:
    def __init__(self,accountNumber,balance):
        self.accountNumber=accountNumber
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        return f"balance{self.balance}"

    def withdraw(self,amount,pin):
        if pin==1234 and amount<self.balance:
            self.balance-=amount
            return f"balance{self.balance}"
        else:
            print("Pin/Insufficient Balance")


accountNumber = int(input("Enter Your Account Number"))
balance = int(input("Enter Your Balance"))
pin = int(input("Enter you security Pin"))

sbi=Bank(accountNumber,balance)


while True:
    print("1.Account Info\n2.Check Balance\n3.Deposit\n4.withdraw")
    choice = input("\nEnter your choice")
    if choice=="":
        break

    if choice=="1":
        print("account number:",sbi.accountNumber)
    elif choice=="2":
        print("Balance:",sbi.balance)
    elif choice=="3":
        amount=int(input("Enter Your Amount"))
        print(sbi.deposit(amount))
    elif choice =="4":
        amount = int(input("Enter Your Amount"))
        print(sbi.withdraw(amount,pin))
    else:
        print("Invalid Choice")

