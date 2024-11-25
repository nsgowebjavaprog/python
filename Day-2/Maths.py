# 1. Arithmatic Operation [ +=, -=, *=, /=, **, %]
'''
friends = 3

 friends = friends + 6  # 7

 friends += 6  # 7

 friends = friends ** 6  # 729


print(friends)

'''

# 2. Maths
'''
x = 3.14
a = 2
b = 3
y = -4
z = 5

res = round(x) # 3
res = abs(y) # 4
res = pow(a,b) # 8

res = max(a,b,x,y,z) # 5

print(res)

'''

# Math-Modules

'''
import math

print(math.pi) # 3.141592653589793

print(math.e) # 2.718281828459045

print(math.sqrt(9)) # 3.0

print(math.ceil(9.2)) # 10

print(math.floor(7.3)) # 7

print(math.floor(8.8)) # 8
'''

# 4. Ex-1

# Area of Circumference
'''
import math

radius = float(input("Enter the radius:"))  

# round 3.2 == 3
# round 4.8 == 5

circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)} cm") 
# The circumference is: 31.42 cm
'''

# Area of Circle
'''
import math

radius = float(input("Enter the radius:"))  

# round 3.2 == 3
# round 4.8 == 5

circle = math.pi * pow(radius ,2)

print(f"The circle is: {round(circle, 2)} cm") 
# Enter the radius:4
# The circle is: 50.27 cm
'''

# Hypotenues Calculator
'''
# c = root a^2 + b^2

import math

a = int(input("Enter the a:"))
b = int(input("Enter the b:"))

c = math.sqrt(pow(a,2) + pow(b,2))

print(f"C is {c} cm")
# Enter the a:17
# Enter the b:14
# C is 22.02271554554524 cm
'''