# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())

array = list(map(int, input().split()))
set_a = set(map(int,input().split()))
set_b = set(map(int,input().split()))

happiness = 0
for i in array:
    if i in set_a:
        happiness+=1
    elif i in set_b:
        happiness -=1
    else:
        pass
        
print(happiness) 