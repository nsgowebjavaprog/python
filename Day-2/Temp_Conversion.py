# Temp Conversion

unit = input("Temp is Celsius or Fahreheit [C/F] : ")
temp = float(input("Enter the TEMP: "))

if unit == 'C':
    temp = round((9 * temp) / 5+32)
    print(f"Temp in F={temp} F") 
elif unit == "F":
    temp = round((temp - 32) * 5/9)
    print(f"Temp in C:{temp} C")
else:
    print(f"{unit} is an invalid unit of ,easurement")        