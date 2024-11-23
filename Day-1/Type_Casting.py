# String, Int, Float, Boolean --> Explicit & Implicit

name = "NS LONI"
age = 20
now_student = True
grade_for_4 = 3.5


print(type(name))
print(type(age))
print(type(now_student))
print(type(grade_for_4))

'''
<class 'str'>
<class 'int'>
<class 'bool'>
<class 'float'>
'''

# Explicit

age = float(age)
print(f"Now Age is:-{type(age)}") # Now Age is:-<class 'float'>

grade_for_4 = int(grade_for_4)
print(grade_for_4) # 3

now_student = str(now_student)
print(f"Boolean now: {now_student}")
print(type(now_student))
'''
Boolean now: True
<class 'str'>
'''

age = bool(age)
print(age) # True  | if age= 0 --> false

name = bool(name)
print(name) # True

# Implicit

x = 10
y = 10.0

x = x/y
print(x) 
# 1.0