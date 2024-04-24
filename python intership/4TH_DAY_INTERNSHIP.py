'''ns:{'sem':3,'branch':'cse','college':'BiTM Ballary'}
sg:{'sem':3,'branch':'eee','college':'BiTM Ballary'}
loni:{'sem':3,'branch':'eee','college':'BiTM Ballary'}

s=[ns+sg+loni]
for i in s:
    print(i)'''

# print('Hi')
#
# student=dict(student={
#     "name":"NS_LONI",
#     "age":21,
#     "sem":3,
#     'sem':3, #-------->Dublicate Not Allowed
# })
# print(student)

'''word="nagarajloni"
vowel="aeiou"
res=[char for char in word if char in vowel]
print(res)
result=[char for char in word if char not in vowel]
print(result)
print(word[0:10:3])
print(word[::-1])
print(word[::-3])

print('hi')
# print(word[0:11])
# for i in range(word[0:11]):
#     print(i,end="-")

# ,sep='-')'''
# word="nagarajloni"
# res=[char for char in word if char in word[::1]] #n-a-g-a-r-a-j-l-o-n-i-
# for i in res:
#     print(i,end='-')
#
# sep='-'.join(word[::2])
# print(sep)
#
# for i in range(0,len(word)):
#     if(i%3==0 and i!=0):
#         print('-',end='')
#     else:
#         print(word[i],end='')

'''
# FILE HANDLING
file_read=open("ns.txt","a")
# if file_read:
#     print("open")
# data=file_read.read()
# print(data)
file_read.write("aaaaaaaaaaa")
print(file_read)
if file_read:
    print('succ')
file_read.close()'''

#  INBUILT METHOD'S LIST,DICT,TUP,STRING,SET,FILE HANDLING,,,*** READ THE DATA

'''file= open("ns.txt","r")                        # r--.reading  # w--->writing  # x --->creating new file   # a -->writing and appending
data = file.read()
                                                      # b-->binary mode    # t-->text mode     # + ---->updating
print(data)
print(data[0:10])

file.close()'''
'''
# STRING
str1="Nagarj"
str2="Loni"
#1
print(str1)
print(str2)
name=str1+str2
print(name)
#2
print(len(str1))
#3
print(type(str2))
#4
print(str2[1])
#5
print(str2[:3])
#6
print(str2.endswith("i"))
#7
print(str2.capitalize())
#8
print(str2.replace("loni","LONI"))
#9
print(str2.find("i"))
#10
print(str1.count("a"))


#13
print(str2.isalnum())
#14
print(str2.isalpha())
#15
print(str2.isspace())
#MANY IN is'''


# FILEHANDLING
# READ

'''file= open("file.txt","r")
data = file.read()
print(data)
print(type(data))
file.close()'''

# WRITING

'''file= open("file.txt","w")
file.write("I Am Nagaraj loni")

print(data)
file.close()'''

# READ
'''
with open("file.txt","r")as f:
    data=f.read()
    print(data)'''

# REMOVE
'''
import os
os.remove("ns.txt")'''

# Find Element
'''
word="Nagaraj"
with open("file.txt","r")as f:
    data=f.read()
    if(data.find(word)!=-1):
        print("Found")
    else:                                              #o/p====  Found
        print("Not Found")'''

# Replace
'''
with open("file.txt","r") as f:
    data=f.read()

    new_data=data.replace("Nagaraj","NAGARAJ_LONI")          #change in output
    print(new_data)'''


# 1
dict={}

print('name:%s ' %dict['name: '])
print('nam:%s ' %dict['Age: '])
print('names:%s ' %dict['dob: '])
print('namess:%s ' %dict['A-D num: '])
print('namea:%s ' %dict['nae: '])
print('namesa:%s ' %dict['nam: '])
print('nameas:%s ' %dict['nme: '])
print('nameasas:%s ' %dict['ame: '])
print('nameasa:%s ' %dict['me: '])
print('namdse:%s ' %dict['ne: '])
print(dict)
