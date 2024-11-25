foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f"Your total is: ${total}")

'''
Enter a food to buy (q to quit): ty
Enter the price of a ty: $67
Enter a food to buy (q to quit): ty
Enter the price of a ty: $78
Enter a food to buy (q to quit): ty
Enter the price of a ty: $78
Enter a food to buy (q to quit): ty
Enter the price of a ty: $678
Enter a food to buy (q to quit): rtrt
Enter the price of a rtrt: $676
Enter a food to buy (q to quit): q
----- YOUR CART -----
ty ty ty ty rtrt
Your total is: $1577.0
'''