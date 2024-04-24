class Magical_Prime_Num():
    def isMagic(n):
        sum = 0

        while (n > 0 or sum > 9):
            if (n == 0):
                n = sum
                sum = 0
            sum = sum + n % 10
            n = int(n / 10)

        return True if (sum == 1) else False

    n = 13
    if (isMagic(n)):
        print("Magic Number")
    else:
        print("Not a magic Number")


class Neon():
    while True:
        x = int(input("enter a no :"))
        if (x == 0):
            print("the program has been terminated")
            break
        p = x ** 2
        sum = 0
        while (p != 0):
            rem = p % 10
            sum = sum + rem
            p = p // 10
        if (sum == x):
            print("number  is neon")
        else:
            print("number  no is not neon number ")


class Reverse_String():
    def reverse(s):
        str = ""
        for i in s:
            str = i + str
        return str

    s = "BiTM_BALLARI_COLLEGE"

    print("The original string is : ", end="")
    print(s)

    print("The reversed string(using loops) is : ", end="")
    print(reverse(s))


class Bank():
    def withdraw(account, amount):
        if amount > account['balance']:
            print("Insufficient funds!")
        else:
            account['balance'] -= amount
            account['transactions'].append(f"Withdrawal: ${amount}")
            print(f"Withdrawal successful. Remaining balance: ${account['balance']}")

    def deposit(account, amount):
        account['balance'] += amount
        account['transactions'].append(f"Deposit: ${amount}")
        print(f"Deposit successful. Remaining balance: ${account['balance']}")

    def get_balance(account):
        return account['balance']

    def get_transaction_history(account):
        return account['transactions']

    # Create an account dictionary
    account = {
        'balance': 1000,
        'transactions': []
    }

    # Dictionary to map user choices to functions
    choices = {
        '1': deposit,
        '2': withdraw,
        '3': get_balance,
        '4': get_transaction_history
    }

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '5':
            print("Exiting program.")
            break

        if choice in choices:
            if choice == '1' or choice == '2':
                amount = float(input("Enter amount: "))
                choices[choice](account, amount)
            else:
                print(choices[choice](account))
        else:
            print("Invalid choice. Please try again.")

class Main()