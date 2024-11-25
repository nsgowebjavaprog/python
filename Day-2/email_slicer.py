email = "nsloni123@gmail.com"

index = email.index("@")

username = email[:index]
domain = email[index+1:]

print(f"Your name: {username} and domain is: {domain}")

# Your name: nsloni123 and domain is: gmail.com