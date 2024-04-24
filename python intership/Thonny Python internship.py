'''dict={}
print("Enter the data: ")
dict['name']=input('name: ')
dict['age']=input('age: ')
dict['sem']=input('sem: ')
dict['branch']=input('branch: ')
dict['college']=input('college: ')
print('data of student: ')
print(dict)
print("Data in col wise: ")

# key are print

for i in dict:
    print(i)
del dict['name']
print('name is del: ')
print(dict)

# values are print

for i in dict:
    print(dict[i])'''
    
# ITEMS METHODE ACCESS BOTH {KEY:VALUE'S} ITEM---->return--->TUPLE
stu={'name':'ns loni','age':21,'sem':3}
print(stu)
for i in stu.items():
    print(i)
    
print(sorted(stu))
print(len(stu))

copy=stu.copy()
print(copy)
#print(copy.pop(1))
print(copy)

