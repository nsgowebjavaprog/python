# 1st-Task
# Prime Numbers B/W Range
'''start=int(input("Enter The Starting Number : "))
end=int(input("Enter The Last Number : "))
for i in range(start,end+1):
    if i>1:
        for j in range(2,i+1):
            if i%j==0:
                break
        else:
            print(i)'''

# 2nd--Task
# Prime Number

'''number=int(input("Enter The Number : "))     #TC==0(n)
if number>1:
    for i in range(2,(number//2)+1):
        if(number % i) == 0:
            print(number,"Not a prime number")
            break
    else:
        print(number,"is Prime Number")
else:
    print(number,"is not prime number")'''

# 3rd---Task
# Date
'''from datetime import date

today = date.today()
print("Today's date:", today)

# 4----Task
# Time

from datetime import datetime

current_dateTime = datetime.now()

print(current_dateTime.year) 

print(current_dateTime.month) 

print(current_dateTime.day) 

print(current_dateTime.hour) 

print(current_dateTime.minute) 

print(current_dateTime.second) 

print(current_dateTime.microsecond) 

# 5th-----Task
# Date and Time
import datetime

# using now() to get current time
current_time = datetime.datetime.now()

# Printing value of now.
print("Time now at greenwich meridian is:", current_time)


# 6th------Task
# Day and Date

import calendar
from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday = ", calendar.day_name[yesterday.weekday()], yesterday.strftime('%d-%m-%Y'))
print("Today = ", calendar.day_name[today.weekday()], today.strftime('%d-%m-%Y'))
print("Tomorrow = ", calendar.day_name[tomorrow.weekday()], tomorrow.strftime('%d-%m-%Y'))'''

# 7-th "X"---->Patter
'''i=0
j=4
for row in range(5):
    for col in range(5):

        if row == i and col == j:       # /
            print("*",end=' ')
            i=i+1
            j=j-1
        elif row == col:              #\
            print("*",end=' ')
        else:
            print(end=' ')
    print()   '''                      # Output : X

# 8th "Z "------>Pattern
# i=1
# j=4
# for row in range(0,6):                  # ******
#     for col in range(0,6):
#         if row == 0 or row == 5:        # ******
#             print('*',end=' ')
#         elif row ==i and col ==j:
#             print('*',end=' ')
#             i=i+1
#             j=j-1
#         else:
#             print(end=' ')
#     print()


# 9th

# NAME=(input("Enter NAME : "))
# name=len(NAME)
#
# for row in range(name):
#     for column in range(name):
#         if row==col or ((row+col)==name-1):
#             print("{0}".format(NAME[col]),end='')
#         else:
#             print(" ",end=" ")
#     print()


'''def printPattern(Str, Len):
    for i in range(Len):
        for j in range(Len):

            if ((i == j) or (i + j == Len - 1)):

                print(Str[j], end="")

            else:

                print(" ", end="")

        print()


Str = "nsloni"

Len = len(Str)

printPattern(Str, Len)
'''

'''import math as mt

def pattern(n):
    i = n - 1
    j = 1
    for i in range(n - 1, -1, -1):

        for j in range(n - 1, i, -1):
            print(' ', end='')

        print(chr(i + 65), end='')

        for j in range(1, i * 2):
            print(' ', end='')

        if (i >= 1):
            print(chr(i + 65), end='')

        print()
# taking size from the user
n = 5
# function calling
pattern(n)'''
