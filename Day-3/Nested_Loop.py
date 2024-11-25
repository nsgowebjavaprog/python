# for i in range(4):
#     for j in range(1, 10):
#         print(j, end=" ")
#     print()
        
# 1 2 3 4 5 6 7 8 9 
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9
# 1 2 3 4 5 6 7 8 9

row = int(input("Enter the no.of Rows:"))
col = int(input("Enter the no.of cols:"))
symbol = input("Enter the no.of symbol:")

for i in range(4):
    for j in range(1, 10):
        print(symbol, end=" ")
    print()
        