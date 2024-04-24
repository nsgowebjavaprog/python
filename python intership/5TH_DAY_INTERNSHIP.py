# FUNCTION WITH DICTIONARY
'''
def nagaraj():
    return "This is my bank balance"

test_dict={"fname":nagaraj,"age":21,"address":"bijapur"}    # nagaraj is a function

print("The original dictionary is : "+str(test_dict))

 # CALLING FUNCTION

res=test_dict["fname"]()

# PRINTING RESULT
print("The required call result:\n" +str(res))      # The required call result:This is my bank balance
'''

# 2
'''
def nagaraj(a,b):        # 300
    print("balnce is :",a+b)


test_dict = {"fname": nagaraj, "age": 21, "address": "bijapur"}  # nagaraj is a function

print("The original dictionary is : " + str(test_dict))

# CALLING FUNCTION

res = test_dict["fname"](100,200)

# PRINTING RESULT
# print("The required call result:\n" + str(res))
'''

# user_password=int(input("Enter The PASSWORD OF USER : "))
# user_email=str(input("Enter The Email of USER : "))
# password=123456
# email="nagarajbijapur@gmail.com"
#
# if(email==user_email):
#     if(password==user_password):
#         print("success")
#
#     else:
#         print("password error")
# else:
#     print("email error")

def withdraw(account, amount):

    if withdraw.count>5:
        print("more then 5 times's")
            if amount > account['balance']:
                print("Insufficient funds!")

            else:
                account['balance'] -= amount
                account['transactions'].append(f"Withdrawal: ${amount}")
                print(f"Withdrawal successful. Remaining balance: ${account['balance']}")



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
#
# user_password=int(input("Enter The PASSWORD OF USER : "))
# user_email=str(input("Enter The Email of USER : "))
# password=123456
# email="nagarajbijapur@gmail.com"
#
# if(email==user_email):
#     if(password==user_password):
#         print("success")
#
#
#     else:
#         print("password error")
#         breakpoint()
# else:
#     print("email error")
#     breakpoint()

# user_password1=int(input("Enter The PASSWORD OF USER : "))
# user_email1=str(input("Enter The Email of USER : "))
# password1=123456
# email1="nagarajbijapur10@gmail.com"
#
# user_password2=int(input("Enter The PASSWORD OF USER : "))
# user_email2=str(input("Enter The Email of USER : "))
# password2=234567
# email2="nagarajloni20@gmail.com"
#
# user_password3=int(input("Enter The PASSWORD OF USER : "))
# user_email3=str(input("Enter The Email of USER : "))
# password3=345678
# email3="nsloni120@gmail.com"
#
# if(email1==user_email1 or email2==user_email2 or email3==user_email3):
#     if(password1==user_password1 or password2==user_password2 or password3==user_password3):
#         print("success")
#
#
#     else:
#         print("password error")
#         breakpoint()
# else:
#     print("email error")
#     breakpoint()

user_password=(input("Enter The PASSWORD OF USER : "))
user_email=(input("Enter The Email of USER : "))
#password1=123456
#email1="nagarajbijapur10@gmail.com"

user_password=(input("Enter The PASSWORD OF USER : "))
user_email=(input("Enter The Email of USER : "))
#password2=234567
#email2="nagarajloni20@gmail.com"

user_password=(input("Enter The PASSWORD OF USER : "))
user_email=(input("Enter The Email of USER : "))
#password3=345678
#email3="nsloni120@gmail.com"

# if(email1==user_email1 or email2==user_email2 or email3==user_email3):
#     if(password1==user_password1 or password2==user_password2 or password3==user_password3):
password=["123456","234567","345678"]
email=["nagarajbijapur10@gmail.com","nagarajloni20@gmail.com","nsloni120@gmail.com"]
# if(email[0] or email[1] or email[2] == user_email3 or user_email1 or user_email2):
#     if(password[0] or password[1] or password[2] == user_password1 or user_password2 or user_password3):
#         print("success")
for i in range(0,len(email)):
    for j in range(0, len(password)):
       if (email[i]==user_email):
           if (password[j] == user_password):
              print("password is correct:")
           else:
               print("email is correct:")
   # for j in range(0,len(password)):
   #     if password[j] == password:


       else:
         print("not matched:")
breakpoint()



#
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