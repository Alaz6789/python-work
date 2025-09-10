class BankAccount:
    # 1. cobn
    #  2. properties
    # 3. functionsalities
    def __init__(self,name,acNum,amount):
        self.balance = amount
        self.accountHolder = name
        self.accNum = acNum
        print(f"account for {self.accountHolder} is created")
    def displayInfo(self):
        pass
    def checkBalance(self):
        print(f"{self.accountHolder} balance is {self.balance}")
    def withdraw(self):
        amount = int(input("How much do you want to withdraw: "))
        if amount > self.balance:
            print("Insufficient value")
            return
        self.balance = self.balance - amount
        print(f"You have withdrawn {amount}")
        self.checkBalance()
    def deposit(self):
        amount = int(input("How much do you want to deposit: "))
        self.balance = self.balance + amount
        print(f"You have deposited {amount}")
        self.checkBalance()
        
        
alif = BankAccount("Alif Azher","234562",500)
akash = BankAccount("akash kumar roy","45674",300)
akash.checkBalance()
alif.withdraw()
alif.deposit()