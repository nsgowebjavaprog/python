# CLASS
'''
print("CLASSESS........")
item1='phone'
item1_price=100
item1_quantity=5
item1_total_price=item1_price * item1_quantity
print(item1_total_price)'''

#1
'''
class Item:
    def calculate_total_price(self,x,y):
        return  x*y


item1=Item()
item1.name='Phone'
item1.price=10000
item1.quantity=5
print(item1.calculate_total_price(item1.price , item1.quantity))

item2=Item()
item2.name='Laptop'
item2.price=100000
item2.quantity=2
print(item2.calculate_total_price(item2.price , item2.quantity))

 random_str = 'aaa'
 print(random_str.upper())'''

# 2 CONSTRUCTOR,  __init__
'''
class Item:
    def __init__(self,name):
        print(f"Hello Friend: {name}")         #Hello Friend: Phone
    def calculate_total_price(self,x,y):       #Hello Friend: Laptop
        return  x*y


item1=Item('Phone')
item1.name='Phone'
item1.price=10000
item1.quantity=5                 # Hello Friend
                                 # Hello Friend
item2=Item('Laptop')
item2.name='Laptop'
item2.price=100000
item2.quantity=2         '''

# 3
'''
class Item:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price = price
        self.quantity = quantity

        # def calculate_total_price(self):
        #     return self.price * self.quantity

item1 = Item('Phone',10000,5)
item2 = Item('Laptop',58653,2)
print(item1.name)
print(item1.price)
print(item1.quantity)

print(item2.name)
print(item2.price)
print(item2.quantity)

# print(item1.calculate_total_price())
#
# print(item2.calculate_total_price())

#OUTPUT:
# Phone
# 10000
# 5
# Laptop
# 58653
# 2                
'''

# MOSH---CLASS
'''
class Class_name:
    # FUNCTION
    def move(self):
        print("move")
    def draw(self):
        print("draw")

Class_name1 = Class_name()
Class_name1.move()
Class_name1.name="NS_LONI"
print(Class_name1.name)
Class_name1.draw()'''

# CONSTRUCOT------IS A FUNCTION-->CREATING OBJECT
'''
class Class_name:
    # FUNCTION
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def move(self):
        print("move")
    def draw(self):
        print("draw")

#costructor
Class_name=Class_name(10,20)
Class_name.x=11
print(Class_name.x)

#class

# Class_name1 = Class_name()
# Class_name1.move()
# Class_name1.name="NS_LONI"
# print(Class_name1.name)
# Class_name1.draw()'''

# EX___1
'''class Person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print("NSLONi")

    def name(self):
        print(f"Hi i am{self.name}")


ns=Person("NAGARAJ LONI")
# print(ns.name)                   # NAGARAJ LONI
ns.talk()       #NSLONi
'''

# INHERITANCE
'''

class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")

class Cat(Mammal):
    def annoing(self):
        print("ANNONIG")
dog=Dog()
dog.walk()     # walk
dog.bark()     # bark

cat=Cat()
cat.walk()         # walk
cat.annoing()      # ANNONIG
'''

Info={}
Info['Name']=input('Name: ')
Info['Age']=input('Age: ')
Info['DOB']=input('DOB: ')
Info['Aadhar_number']=input('Aadhar_Num: ')
Info['Debit_Card_Num']=input('Debit_Card_Num: ')
Info['Mob_Num']=input('Mob_Num: ')
Info['Pincode']=input('Pincode: ')
Info['Height']=input('Height: ')
Info['Tax']=input('Tax: ')
print(Info)
# file= open("Info.txt","a")
# file.write(Info)
# print(Info)
for key,value in Info.items():
    print(f"{key} --> {value}")


# ADD
# Info['Age: ']=20.1

# DELETE
# del ['Age']

# ONLY KEY
print("KEY'S OF STUDENT : ")
for key in Info.keys():   #
    print(key)

# ONLY VALUE

print("VALUE'S OF STUDENT : ")
for value in Info.values():
    print(value)




