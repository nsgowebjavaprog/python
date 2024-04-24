'''num=[1,3,2,-5,-3,6,8]
neg_sum=0
even_sum=0
odd_sum=0
for i in num:
    if (i < 0):
        neg_sum+=i
        print(neg_sum)   # -8
    elif (i % 2 == 0):  
        even_sum+=i
        print(even_sum)   # 16
    else:
        odd_sum+=i
        print(odd_sum) ''' # 4
        
        
val=[2,4,-3,1,-5,7]
neg_val=max(i for i in val if i<0)
pos_val=max(j for j in val if j%2==0)

print(neg_val)
print(pos_val)