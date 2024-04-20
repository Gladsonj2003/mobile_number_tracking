import phonenumbers
import folium
from phonenumbers import geocoder, carrier

from opencage.geocoder import OpenCageGeocode

from myphone import number  # Assuming this imports the phone number you want to parse

# Parse the phone number
pepnumber = phonenumbers.parse(number)

# Get the location information
location = geocoder.description_for_number(pepnumber, "en")
print("Location:", location)

# Get the carrier information
service_pro = phonenumbers.parse(number)
carrier_info = carrier.name_for_number(service_pro, "en")
print("Carrier:", carrier_info)

# Initialize the OpenCage Geocode with your API key
key = '43bbea309ce54d53befc067d44a6b12f'
geocoder = OpenCageGeocode(key)

# Query the location information
query = str(location)
results = geocoder.geocode(query)
#print("Geocode Results:", results)

lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']

print(lat,lng)

myMap=folium.Map(location=[lat,lng],zoom_start= 9)
folium.Marker([lat,lng],popup=location).add_to(myMap)

myMap.save("mylocation.html")