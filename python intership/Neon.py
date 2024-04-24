
while True:
    x=int(input("enter a no :"))
    if(x==0):
        print("the program has been terminated")
        break
    p=x**2
    sum=0
    while (p!=0):
        rem=p%10
        sum=sum+rem
        p=p//10
    if(sum==x):
        print("number  is neon")
    else :
        print("number  no is not neon number ")
