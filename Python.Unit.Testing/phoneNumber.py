
import re
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier



def isvalid(phone_num):
    pattern=re.compile('^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$')
    return pattern.match(phone_num)

phone_num=input("Please Enter Your Phone Number: ")
phone_number = phonenumbers.parse(phone_num,"CH")
ro_number = phonenumbers.parse(phone_num,"RO")
valid = phonenumbers.is_valid_number(phone_number)

if isvalid(phone_num):
    print (valid)
    print(f"{phone_number} is a valid phone number.")
    print(geocoder.description_for_number(phone_number,"en"))
    print(carrier.name_for_number(ro_number,"en"))

else:
    print(f"{phone_number} is not a valid phone number.")
