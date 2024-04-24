# 1st--Program --List

# list=[]
# n=int(input("Enter tne size of Liat : "))
# for i in range(0,n):
#     #print(i)
#     ele=int(input("Enter the Element's : "))
#     list.append(ele)
# print(list)



# 2nd--Program
# n=[10,20,30]
# s=[12,122,12]
# l=n+s
# print(l)               #[10, 20, 30, 12, 122, 12]
# print(type(l))          #<class 'list'>
# print(min(l))           #10
# print(max(l))           #122
# print(max(n))

#3rd

# num=[1,2,3,4,5,6]
# num.append(12)
# print(num)
# num.insert(0,100)
# print(num)
# num.remove(5)
# print(num)
# # num.clear()
# print(num)
# num.pop()
# print(num)
# num.index(3)
# num.count(1)
# num.sort()
# print(num)
# num.reverse()
# print(num)

# 4th-Program
# n=[10,25,37,40,57,65]
# for i in n:
#     if i %10==7:
#         print(i)
# # print(sum)

#  5th Program

# n=[10,25,37,40,57,65]
# sum=0
# for i in n:
#     if i %10==0:
#         print(i)
#         sum+=i
#print(sum)

# 6th dublicate

# n=[10,20,30,40,50,30,50,12,12,12,12,121,21,2,12,12,1,212,121,212,2,1]
# y=[]
# for i in n:
#     if i not in y:
#         y.append(i)
# print(y)

# n=[]
# num=int(input("Enter tne size of Liat : "))
# for i in range(0,num):
#     ele = int(input("Enter the Element's : "))
#     n.append(ele)
# print(n)
# y=[]
# num2=int(input("Enter tne size of Liat : "))
# for i in range(0,num2):
#     ele = int(input("Enter the Element's : "))
#     y.append(ele)
# print(y)
#
# # y=[10,20,30,40,50]
# # n=[60,70,80,90,100,20]
# a=[]
# for i in n:
#      if i  in y:
#          a.append(i)
# print(a)




# IMP

# five_value=[]
# num=int(input("Enter tne size of Liat : "))
# for i in range(0,num):
#     ele = int(input("Enter the Element's : "))
#     five_value.append(ele)
# print(five_value)
# for k in five_value:
#     print(k)
# if num > 1:
#
#     for i in range(2, (num//2)+1):
#
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")

'''
five_value = []
num = int(input("Enter tne size of List : "))
for j in range(0, num):
    ele = int(input("Enter the Element's : "))
    five_value.append(ele)
print(five_value)
for k in five_value:
    print(k)
if k > 1:

    for i in range(2, (k // 2) + 1):

        if (k % i) == 0:
            print(k, "is not a prime number")
            break
    else:
        print(k, "is a prime number")
else:
    print(k, "is not a prime number")

#
for y in five_value:
    if  y/4==0:
        print("Leap  Year : ",y)
        break
    else:
        print("Not leap year")
print()'''
#Tuple

'''tup=(1,2,3,2,4,5,)
print(tup)
print(type(tup))

#Methods
print(tup.index(1))
print(tup.count(2))'''
#
# name=()
# # name1=input("Enter 1: ")
# # name2=input("Enter 2: ")
# # name3=input("Enter 3: ")
#
# name = name + (4,)
# name = name + (5,)
# name = name + (6,)
# name = name + (7,)
#
# for i in range(0,5):
#     name+=(i,)
#
#
# # name.append(name1)
# # name.append(name2)
# # name.append(name3)                   #AttributeError: 'tuple' object has no attribute 'append'
# print(name)
'''
tup=["A","B","C","A","A","B","D"]
print(tup.sort())
print(tup)
print(tup.insert(0,"a"))
print(tup)
print(tup.remove("a"))
print(tup)
print(tup.pop())
print(tup)
print(tup.index(3))
print(tup)
print(tup.reverse())
print(tup)
'''

# five_value = []
# num = int(input("Enter tne size of List : "))
# for i in range(0, num):
#     ele = int(input("Enter the Element's : "))
#     five_value.append(ele)
# print(five_value)
#
#
# # num = 15
# # i=1
# flag = 0
# for j in range(five_value[0],five_value[4]):
#     if j % i==0:
#       flag = 1
#       # i+=1
#       break
#     if flag == 1:
#         print('Not Prime')
#     else:
#         print("Prime")

# SET
# un-order
set={"a","b","c","d","e","a","s","b","d"}
print(type(set))
print(set)
print(len(set))
print(set.add("ZZZZ"))
print(set)

# UNION

a={1,2,3,4,5}
b={3,4,5,6,7}
c={6,7,8,9,10}
print(a.union(b,c))    #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

a={1,2,3,4,5}
b={3,4,5,6,7}
c={6,7,8,9,10}
print(a|b|c)

# INTERSECTION
a={1,2,3,4,5}
b={3,4,2,6,7}
c={6,4,2,9,10}
print(a.intersection(b,c))      #{2, 4}

a={1,2,3,4,5}
b={3,4,2,6,7}
c={6,4,2,9,10}
print(a&b&c)

#  IiiiiiiiiiiiiiimmMMMMMMMMMPPPPPPPPPPPPPPPPPPPP
day1={"m_day","t_day","w_day","s_day"}
day2={"m_day","t_day","sasasasa","asasasas","asasa"}     # {'s_day', 'w_day'}
print(day1-day2)



day1={"m_day","t_day","w_day","s_day"}
day2={"m_day","t_day","sasasasa","asasasas","asasa"}
print(day1.difference(day2))

# SYMMENTRIC
 #  INTERSECTION OPOOSITE
a={1,2,3,4,5,6}
b={1,2,9,8,10}       # {3, 4, 5, 6, 8, 9, 10}
c=a^b
print(c)

day1={"m_day","t_day","w_day","s_day"}                    # IT OUTPUT IS BASED ON VALUE STORED IN INDEX WHEN BOTH [0] ETC INDEX IS SAME > SAME BUT MORE
day2={"m_day","t_day","sasasasa","asasasas","asasa"}
print(day1>day2)      # --------------------------------------------># False
print(day1<day2)       # --------------------------------------------># False
print(day1==day2)      # --------------------------------------------># False