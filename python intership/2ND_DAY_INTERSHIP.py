# CONDITIONAL STATEMENT

'''if (condition_1):
    print("STATEMENTS")
elif(condition_2):
    print("STATEMENTS")
else:
    print("STATEMENTS")'''

# 1ST
# age1=int(input("Enter Age: "))
# age2=int(input("Enter Age: "))
# if age1>age2:
#    age3=age1+age2
#    print(age3)
# else:
#     age3 = age1 - age2
#     print(age3)

# 3rd
'''user_password=int(input("Enter The PASSWORD OF USER : "))
user_email=str(input("Enter The Email of USER : "))
password=123456
email="nagarajbijapur@gmail.com"
otp=1234
if(email==user_email):
    if(password==user_password):
        print("success")
        user_otp=int(input("enter OTP: "))
        if (otp == user_otp ):
            print("Enter appppppppp your OTP is correct;")
        else:
            print("OTP error")
    else:
        print("password error")
else:
    print("email error")'''


#4
'''num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
if (num1 == num2):
    print("Both are eq...")
elif num1 > num2:
    print("num1 is greater")
else:
    print("num2 is greaetr")'''

# 5th program

# num1=int(input("Enter num1: "))
# num2=int(input("Enter num2: "))
# print('num1 is greater' if num1>num2 else 'num2 is greate' if num1 < num2 else'equal')

# 1st-Task     {ternary}
'''lemon=int(input("Enter no.of lemon:"))
print('lemon is less' if lemon <21 else 'lemon is more' if lemon >21 else 'sufficient lemon')

# 2nd--Task    {Greatest of 5 numbers}
num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
num3=int(input("Enter num3: "))
num4=int(input("Enter num4: "))
num5=int(input("Enter num5: "))
print('num1 is greater' if num1>num2 and num1>num3 and num1 > num4 and num1 >num5 else 'num2 is greate'
 if num2 > num3 and num2>num4 and num2 >num5 else'num3 is greater' if num3>num4 and num3>num5 else 'num4 is greater' if num4>num5 else 'num5 is greater')
'''
# 3rd---Task    {print name in kannnad}


#print((chr(3240)+chr(3206)+chr(3223)+chr(3206)+chr(3248)+chr(3206)+chr(3228)))  #ನಆಗಆರಆಜ
# print(chr(3240)+chr(3206), end="")
# print(chr(3223), end="")
# print(chr(3248)+chr(3206), end="")
# print(chr(3228))

#print(chr(3240)+chr(3206))


# kannad="\u0CA8"
# print(kannad)


'''kannada_nagaraj = '\u0CA8' + '\u0CBE' + '\u0C97' + '\u0CB0' + '\u0CBE' + '\u0C9C'

print(kannada_nagaraj)'''

#  4-th
'''print(chr(97))
print(ord('a'))

for i in range(ord('A'),ord('Z')):
    print(ord(chr(i))) '''

# 5-th program
# for i in range(1,6):
#     for j in range(1,6):
#         print('*',end='' )
#     print()
#
# # 6
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end='' )
#     print()
#
# # 7
# for i in range(1, 6):
#      for j in range(1, i + 1):
#        print(j, end='')
#      print()
#
# # 8
#
# for i in range(1, 6):
#     for j in range(1, i + 1):
#        print('*', end='')
#     print()
#
# # 9
# #print("NS")
# for i in range(65,70):
#     for j in range(65,i+1):
#         print(chr(i),end='' )
#     print()
#
# for i in range(65,70):
#     for j in range(65,i+1):
#         print(chr(j),end='' )
#     print()

         #10 th Program
# for i in range(1,11):
#     print(i/10,end=' ')     # 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0

# name="abcdefg"
# length=len(name)
# for i in range(length):
#      for j in range(length):
#          if i==j and length-i-1:
#           print(name)
#      print()

# 11-th

# import math
# print(math.floor(2.9))
# print(round(2.9))
# print(round(2.6))
# print(round(2.5))
# print(math.factorial(5))
# print(math.fabs(5))
# a=math.sqrt(25)
# print(a)
# #print greatset no.
# a=math.ceil(2.00)      #----> 3
# print(a)
# print(math.ceil(-2.01))  # -2


# def prime_num():
#     num=int(input("Enter the number : "))
#     i=1
#     while i<num:
#         # if num / i != 0:
#            print("Prime number : ",num/i!=0)
#            i+=1
# prime_num()

print('hi')