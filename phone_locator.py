import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

# Remplacez le numéro par celui que vous souhaitez analyser
phone_number = phonenumbers.parse("+324333333333")

# Localisation du numéro
location = geocoder.description_for_number(phone_number, "fr")  # "fr" pour obtenir la localisation en français
carrier = carrier.name_for_number(phone_number, "fr")
is_valid = phonenumbers.is_valid_number(phone_number)

if is_valid is True:
    ans = "valid"
else:
    ans = "invalid"

print(f"The cellphone is located in : {location}, Using {carrier}, the number is {ans}.")