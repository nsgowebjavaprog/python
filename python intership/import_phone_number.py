import phonenumbers 
  
 # parse-----> Python programming language that allows for
        # parsing and converting code into machine language.  
  
phone_number = phonenumbers.parse("+911234123456") 
   
valid = phonenumbers.is_valid_number(phone_number) 
   
possible = phonenumbers.is_possible_number(phone_number) 
   
print(valid) 
print(possible) 