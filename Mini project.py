class Bankaccount:
    def __init__(self, Username, Balance=0):
        self.name = Username
        self.balance = Balance

    def deposit(self, dep):
        if dep > 0:
            self.balance += dep
            print(f"Rs{dep} deposited successfully")
            print("Balance :", self.balance)
        else:
            print("Invalid entry!")

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!!")
        elif 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Rs{amount} withdrawn")
            print("Balance: Rs ", self.balance)
        else:
            print("Invalid entry")

    def balancecheck(self):
        print("Your Balance is Rs ", self.balance)


def login():
    print("Welcome to DAD Bank")
    Username = input("Enter user Name :")
    Balance = float(input("Enter initial Deposit :Rs"))
    jcb = Bankaccount(Username, Balance)

    while True:
        print('''
        1.Deposit
        2.Withdrawal
        3.Check balance
        4.Exit''')

        bal = int(input("Enter your Choice :"))
        if bal == 1:
            Deposit = float(input("Enter Deposital amount :Rs"))
            jcb.deposit(Deposit)
        elif bal == 2:
            Withdraw = float(input("Enter Withdrawal amount :Rs"))
            jcb.withdrawal(Withdraw)
        elif bal == 3:
            jcb.balancecheck()
        elif bal == 4:
            print("Thank you, Visit Again!")
            break
        else:
            print("Enter a valid Choice")


login()
