import phonenumbers
from test import number
from phonenumbers import geocoder,carrier
from termcolor import colored

ch_nmber=phonenumbers.parse(number,"CH")
print(colored('[+]','blue'),geocoder.description_for_number(ch_nmber,"en")) 
service_nmber=phonenumbers.parse(number,"RO")
print(colored('[+]','blue'),carrier.name_for_number(service_nmber,"en"))
