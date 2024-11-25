'''
name = "NSLONI"
mob_num = "6361-544-673"
print(len(name))
print(name.find("N"))
print(name.rfind("N")) #rev
print(name.capitalize()) #only first
print(name.upper())
print(name.lower())
print(name.isdigit()) # false
print(name.isalpha()) #True
print(name.isalnum())
print(mob_num.count("-")) #2

print(mob_num.replace("-","--"))
'''

# Ex-1

# valid user_name

username = input("Enter the user-name: ")

username.isalpha()

username.find(" ")
if len(username) > 12:
    print(f"User name should be less than 12 letters{username}")

elif not username.find(" ") == -1:
    print("ur name don't have space")

elif not username.isalpha():
    print("usename having digits")

else:
    print(f"WEL-COME {username}")    