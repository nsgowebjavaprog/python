# Eg: Matrix, Excel etc..

fruits = ["a","s","f","e"]
veg = ["qw","qw","er","ww"]
meat = ["asa","wew","qwe","ere"]

_2d = [fruits, veg, meat]

print(_2d)

# [['a', 's', 'f', 'e'], ['qw', 'qw', 'er', 'ww'], ['asa', 'wew', 'qwe', 'ere']]

print(_2d[0]) # ['a', 's', 'f', 'e']

print(_2d[1][1])  # qw

# Execise-1
all_in_one = [['a', 's', 'f', 'e'], ['qw', 'qw', 'er', 'ww'], ['asa', 'wew', 'qwe', 'ere']]
 
for i in all_in_one:
    for j in i:
        print(j, end=" ") 
    print()    
'''
a s f e
qw qw er ww
asa wew qwe ere
'''
