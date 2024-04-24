# 1.LIST

'''list1=["BANANA","APPLE","CHERRY"]
print(list1)

list2=list()
print(list2)

list=[3,'colllege',3.5,'colllege']
print(list)

for i in list:
    print(i)

if 'colllege' in list:
    print('found')
else:
    print('not found')

print(len(list1))

p=list1.pop()
print(p)

q=list1.reverse()
print(q)

list1.sort()
print(list1)

list1.reverse()
print(list1)

new_list= list1+list
print(new_list)

#----------------------->COPY()

branch=["CSE",'AI&ML','DS','AI','EEE','ECE']
dublicate_branch=branch.copy()
print(dublicate_branch)

branch.append("CIVIL ENGINEERING")
print(branch)

num=[1,2,3,4,5,6,7,8,9]
squ=[a*a for a in num]
print(num)
print(squ)  '''


# TUPLES---->in-mute

'''tuple1='max'  # string
tuple2 = 'max',

print(type(tuple1))
print(type(tuple2))

tuple=('a','s','d','g','s','a')
print(tuple)

print(tuple.count('a'))
print(tuple[::-1])

new_tuple=('coder',21,'bijapur')
name,age,adr=new_tuple
print(name)
print(age)
print(adr)
'''

# 2.DICTIONARY ------------>MUTE
'''
dict1={"name":'coder','age':21,'adr':'bijapur'}
print(dict1)

dict1['email']='coder258@gmail.com'
print(dict1)

del dict1['adr']
dict1.pop('age')
print(dict1)

if 'name' in dict1:
    print('Wow... Selected,,,')
else:
    print('Try again')

# EXCEPTION
try:
    print(dict1['name'])
except:
    print('something Error')

for key in dict1.keys():
    print(key)

for value in dict1.values():
    print(value)

for key,value in dict1.items():
    print(key,':',value)

dict2={'NAME':'CODER','AGE':21,'ADR':'BIJAPUR','EMAIL':'coder258@gmail.com'}
dict3={'NAME':'HACKER','AGE':20.9,'ADR':'VIJAYAPUR'}

dict2.update(dict3)
print(dict2)

diction={'name':'cse','age':21,'sem':3,'branch':'cse-ds'}
print(diction)
value=diction['name']
print(value)
'''

# 3.SETS{}--->MUTEABLE--------->UN-ORDER
'''
set={1,2,3,4,5,6,7,8,9}
print(set)
for i in set:
    print(i)

set1={}
print(set1)
print(type(set1))

odd={1,3,5,7,9}
even={2,4,6,8,10}
prime={2,3,5,7}
union=odd.union(even)
print(union)

intersection=odd.intersection(prime)
print(intersection)

setA={1,2,3,4,5,6,7,8,9}
setB={1,2,3,10,11,12}

diff = setA.difference(setB)
print(diff)

diff1 = setA.symmetric_difference(setB)
print(diff1)

setA.update(setB)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
print(setA)

setA.intersection_update(setB)  #{1, 2, 3, 10, 11, 12}
print(setA)

setA.symmetric_difference_update(setB)
print(setA)

a={1,2,3,4,5,6,7,8,9}
b={1,2,3,10,11,12}
a.symmetric_difference_update(b)
print(a)

a.issubset(b)
print(a)

b.issubset(a)
print(b)

b.isdisjoint(b)
print(b)

a.issuperset(b)
print(a)

#________________>> COPY()

a=b.copy()
print(a)

a=frozenset([1,2,3,4])   #frozenset({1, 2, 3, 4})
print(a)
'''

# 4.STRING--->IMMUTABLE

'''string='programmer'
char=string[1]
print(char)

sub_string = string[0:8]
print(sub_string)

print(string[:])
print(string[::-1])

string1='coder always'
string2=' like problems->for program'
string3=string1+string2
print(string3)

if 'oz' in string3:
    print("YES")
else:
    print("NO")

str= '         Hello            Heloo           '
print(str.strip())
print(str.lstrip())
print(str.rsplit())

string4='Hello Google'
print(string4.startswith('Hello')) # True
print(string4.startswith('hello'))  # False
print(string4.endswith('Hello'))
print(string4.endswith('Google'))

print(string4.find('lo'))    # 3
print(string4.count('l'))
print(string4.replace("Google","AI"))

print(string4.split(' '))

list = ['a']*10
print(list)
string5 = ''.join(list)
print(string5)

var = 3
string5='The number is %d' %var
print(string5)

string5 = f'The number is {var}'
print(string5)
'''

# 4.COLLECTION

'''from collections import Counter

a='aaaaabbbbsss'
my_Counter=Counter(a)       # Counter({'a': 5, 'b': 4, 's': 3})
print(my_Counter)

print(my_Counter.most_common(1))                         # [('a', 5)]
print(my_Counter.most_common(1)[0][0])    # a
'''

# 5.ITERTOOLS

# from itertools import  product

'''
a=[10]
b=[30]
prod = product(a,b,repeat=2)
print(list(prod))
from itertools import  permutations

a =[10,20,30]
product=permutations(a,3)
print(list(product))

from itertools import combinations
a=[10,20,30,40]
comb=combinations(a,2)
print(list(comb))   

from itertools import accumulate
a=[1,2,3,4]
acc=accumulate(a)
print(a)
print(list(acc))    # [1, 3, 6, 10]


from itertools import groupby

def less_than_3(x):          # x -------->lambad function
    return  x < 3

a=[1,2,3,4]
group_obj = groupby(a,key=less_than_3)
for key,value in group_obj:
    print(key,list(value))
    '''

# 6.LAMBDA FUNCTIONS

'''add = lambda x: x+10   # 15
print(add(5))

def add_function(x):
    return x+10

multi = lambda x,y: x*y
print(multi(3,7))       # 21


list=[(1,2),(2,3),(6,7),(4,2),(9,1)]
reversed_list= sorted(list)

print(list)
print(reversed_list)

# a = [1,2,3,4,5,6]
# b = map(lambda x: x*2, a)
# print(list (b))

# filter

a = [1,2,3,4,5,6,7,8,9]
b = filter(lambda x:x%2==0,a)
print(list(b))

b = filter(lambda x:x%2!=0,a)
print(list(b))

c = [x for x in a if x%2==0]
print(c)

from functools import reduce
a1=[1,2,3,4]
product_a1=reduce(lambda  x,y: x*y,a1)       # 24
print(product_a1)
'''

# 7. EXCEPTION'S  and ERRoRS

'''try:
    a=5/0
except:
    print('error in diviison by zero')

try:
    b=5/0
except Exception as e:
    print(e)

try:
    s=5/1
    b=s+'aaa'
except Exception as e:
    print(e)
except TypeError as a:
    print('Type eroooor',a)
finally:
    print('final block')

class Value_To_High_Error(Exception):
    pass

class Value_To_Small_Error(Exception):

     def __init__(self,message,value):

         self.message= message
         self.value = value

def test_value(x):

    if x>100:
        raise Value_To_High_Error('Value is HiGH')
    if x<5:
        raise  Value_To_Small_Error('Value is smaall',x)

try:
    test_value(101)

except Value_To_High_Error as e:
    print(e)
except Value_To_Small_Error as e:
    print(e.message, e.value)
'''

# 8.JSON
'''


# JavaSrcipt Object Notation ---->lightWeight data format use for data Exchange
# Used in web application

{
    'first_name':'coder',
    'last_name':'programer',
    'hobbies':['coding','decoding','programming','running'],
     'age':21,
    'has_college':True,
    'college':[
        {
         'college_name':'BiTM Ballari',
            'course':'CSE'
        },
        {
            'college_name':'BIPU Badagandi',
            'course':'PUC'
        }
    ]
}'''

# 9 RANDOM NUMBERS
'''

import random

a=random.uniform(1,10)   # 3.7625401519429866
print(a)

b=random.randint(1,10)    # 5
print(b)

c=random.normalvariate(0,1)    # 1.6716385630297932
print(c)

list = list('abcdefghij')
d = random.sample(list,3)      # ['i', 'a', 'h']
print(d)

e= random.choices(list,k=3)        # ['b', 'b', 'h']
print(e)

f = random.shuffle(list)         # ['a', 'c', 'i', 'h', 'g', 'j', 'b', 'f', 'd', 'e']
print(list)

g=random.seed(2)
print("Seed: ",g)       # Seed:  None


import secrets

a= secrets.randbits(4)     # 4--{any numbeer}
print(a)
'''

# import numpy as np
#
# a= np.random.randint(0,10,(3,4))
# print(a)


# 10.DECORATORS

# 1. FUNCTION DECORATORS
# 2. CLASS DECORATORS

# In Python, a decorator is a design pattern that allows you to modify the
# functionality of a function by wrapping it in another function.
'''
def start_end_decorator(func):

    def wrapper():
        print('start')
        func()
        print('end')
    return wrapper

def print_name():
    print("Alexa")

print_name = start_end_decorator(print_name)    # start
                                                 # Alexa
print_name()                                     # end

'''

'''
def start_end_decorator(func):

    def wrapper( ):
        print('start')
        func()
        print('end')
    return wrapper

def print_name():
    print("Alexa")

print_name = start_end_decorator(print_name)
print_name()'''


'''
import functools

def repeat(num_times):
    def decoder_repeat(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(num_times):
                result = func(*args,**kwargs)
            return result
        return wrapper
    return decoder_repeat

@repeat(num_times=4)                     # HellO : ALexaaaa.....
def greet(name):                         # HellO : ALexaaaa.....
    print(f"HellO : {name}")             # HellO : ALexaaaa.....
greet("ALexaaaa.....")                  # HellO : ALexaaaa.....


class CountCalls:

    def __init__(self,func):
        self.func = func
        self.num_calls =0

    def __call__(self,*args, **kwargs):
        self.num_calls +=1
        print(f'This is executed as {self.num_calls} times')
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("HellOOOoOOOOooooooooooooooo,,,,")

say_hello()           # This is executed as 1 times
say_hello()           # HellOOOoOOOOooooooooooooooo,,,,
                      # This is executed as 2 times
                      # HellOOOoOOOOooooooooooooooo,,,,

'''
# 11.GENERATORS     key_word-------> yield
# SYNTAX :    # def function_name():
              # yield statement


# A Generator in Python is a function that returns an
# iterator using the Yield keyword. In this article,
# we will discuss how the generator function works in Python.

'''def mygenerator():
    yield 3
    yield 2
    yield 1

g = mygenerator()
print(sum(g))          # 6
print(sorted(g))         # [1, 2, 3]

"""value = next(g)   # Enter the 3 next get output but when you us 4 next function then get ERRORRRORRR
print(value)

value = next(g)
print(value)

value = next(g)
print(value)"""
"""
value = next(g)
print(value)
"""
"""for i in g:
    print(i)"""
'''

"""def countdown(num):
    print("starting")
    while num > 0:             # OUTPUT: starting
        yield num               # 4
        num -=1                 # 3
                                # 2
cd = countdown(4)               # 1

value = next(cd)
print(value)

print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))"""

# 12. MULTI----THREADING


"""from threading import Thread

def square_numbers():
    for i in range(100):
        i*i

if __name__ =="__main__":
    thread = []
    num_thread = 10

    # creating thread
    for i in range(num_thread):
        thread = Thread(target=square_numbers)
        thread.append(thread)

        # start thread
    for thread in thread:
         thread.start()

        # join Thread
    for thread in thread:
         thread.join()
    print('End main')"""


# 13. FUNCTION ARGUMENT

"""def name(name):
    print(name)

name("Alexa")       # Alexa is an ARGUMENT"""

# 2
"""def foo(a,b,*args, **kwargs):
    print(a,b)                      #1,2

    for arg in args:
        print(arg)                 # 3,4,5

    for key in kwargs:
        print(key,kwargs[key])      # ns_loni 258,coder 1

foo(1,2,3,4,5,ns_loni=258,coder =1)


def foo():
    global  number
    number =10

number = 0
foo()
print(number)    """     # 10











