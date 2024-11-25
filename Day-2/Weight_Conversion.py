# Weight Conversion

weight = float(input("Enter the WEIGHT:"))
unit = input("Enter the unit [K/P]: KG/Pounds")

if unit == "K":
    weight = weight * 2.205
    unit = "lbs"
elif unit == "L":
    weight = weight / 2.205    
    unit = "kgs"
else:
    print(f"{unit} was not valid") 

print(f"Your weight is : {weight} {unit}")           