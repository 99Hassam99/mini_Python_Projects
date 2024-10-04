import phonenumbers
from phonenumbers import geocoder


phone_number1 = phonenumbers.parse("+923130422253")
phone_number2 = phonenumbers.parse("+447495360606")


print("\nPhone Numbers Location\n")

print(geocoder.description_for_number(phone_number1,"en"))

print(geocoder.description_for_number(phone_number2,"en"))

