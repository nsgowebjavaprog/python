class Mango:
    def __init__(self):
        print("what is this")

    def first(self):
        print("first class")

    def second(self,a,b):
        print("second class",(a+b))

    def magical_prime(self,a):
        for i in range(0,a+1):
            if a % i==0:
                print("not prime")
                break
        else:
            print("prime number")


    def neon(self,a):
        num=0
        sq=a*a
        rem=sq%10
        num=num+rem

        print(num=a)

man=Mango()
man.first()
man.second(10,20)
man.magical_prime(101)
man.neon(7)














# num=int(input("Enter the number "))
#
# for i in range(0,num+1):
#     if num>1:
#         if num % i==0