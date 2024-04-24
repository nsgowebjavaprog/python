# code

# def Zellercongruence(day, month, year):
# 	days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
# 	if (month < 3):
# 		month += 12
# 		year -= 1
# 	c = year // 100
# 	year = year % 100
# 	h = (c // 4 - 2 * c + year + year // 4 + 13 * (month + 1) // 5 + day - 1) % 7
# 	return days[(h + 7) % 7]
#
#
# print(Zellercongruence(20,4,2024)) # date (dd/mm/yyyy)

# 1
# class OverloadingDemo:
#     def add(self,x,y):
#         print(x+y)
#
#     def add(self,x,y,z):
#         print(x+y+z)
#
# obj=OverloadingDemo()
# obj.add(10,20)
#
# obj.add(10,20,30)

# taken --> OBJECT IS INPUT IN USING __repr__ {MAGICAL METHOD}----->RETURN THE STRING
#   __ for its "private attributes"