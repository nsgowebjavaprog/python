# TASK-1
# 1.Account Creation
# TASK_2
# 2.Deposit
# 3.Withdraw
# 4.Mini-Statement
# 5.Close


# Banking System
class Bank:
    bankname="Canara Bank"
    branch="Canara Bank Main Road Atharg"

    #Creating an a acccount

    def __init__(self,username,pan,address):
        self.username=username
        self.pan=pan
        self.address=address
        self.balance=0.0
        print(f"Hello {username} congratulations! your Account is Created successfully")

    # 1.DEPOIST
    def deposit(self,amount):
        self.balance=self.balance + amount
        print(f"{amount} Deposited successfully")

    # 2.WiTH_DRAW
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance = self.balance - amount
            print(f"{amount} Withdraw is successfully")
        else:
            print("You don't have that much of amount ")

    # 3.MINISTATEMENT
    def ministatement(self):
        print(f"Your account balence is {self.balance}")


print("Wel-Come To Canara Bank Athrga-586112")
username =input("Enter use Name : ")
pan =input("Enter the pan_Card number : ")
address =input("Enter the address of User : ")
# b----->Object
b=Bank(username,pan,address)


while True:
    print("Select your option : ")
    print(" 1:Deposit\n 2:Withdraw\n 3:Ministatement\n  4:Stop\n ")
    option = int(input(""))

    if option == 1:
        amount=float(input("Enter the deposit amount: "))
        b.deposit(amount)

    if option == 2:
        withdraw=float(input("Enter the WithDraw amount: "))
        b.withdraw(amount)

    if option == 3:
        b.ministatement()


    if option == 4:
        print("Thank You ")
        break