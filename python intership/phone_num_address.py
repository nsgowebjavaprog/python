# Program to find carrier and region 
# of a phone number 
import phonenumbers 
from phonenumbers import geocoder, carrier 
  
# Parsing String to Phone number 
phoneNumber = phonenumbers.parse("+918618822808") 
  
# Getting carrier of a phone number 
Carrier = carrier.name_for_number(phoneNumber, 'en') 
  
# Getting region information 
Region = geocoder.description_for_number(phoneNumber, 'en') 
  
# Printing the carrier and region of a phone number 
print(Carrier) 
print(Region)

# California---->+12096540524
# india---->+919876543210
#United Kingdom--->+447441907219