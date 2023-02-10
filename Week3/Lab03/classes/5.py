class BankAccount:
    def __init__(self):
        balance = float(input())
        self.balance = balance
    
    def depos(self):
        dep = float(input())
        self.balance += dep
        print("Your balance:", self.balance)
    def withdraw(self):
        wdr = int(input())
        if wdr <= self.balance:
            self.balance -= wdr
            print("Your balance has been successfully withdrawn!")
        else:
            print("Insufficient balance")
    def urbalnc(self):
        print("Your balance:", self.balance)

bnk = BankAccount()
bnk.depos()
bnk.withdraw()
bnk.urbalnc()
