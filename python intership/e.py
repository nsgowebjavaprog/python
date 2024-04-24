import phonenumbers
from phonenumbers import geocoder

my_number = phonenumbers.parse("+918618822808")
print(geocoder.description_for_number(my_number, "ru"))