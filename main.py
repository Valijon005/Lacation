import phonenumbers
import opencage
import folium
from myphone import numbers

from phonenumbers import geocoder

pepnumbers = phonenumbers.parse(numbers)
lacation = geocoder.description_for_number(pepnumbers, "en")
print(lacation)


from phonenumbers import carrier
service_pro = phonenumbers.parse(numbers)
print(carrier.name_for_number(service_pro, "en"))


from opencage.geocoder import OpenCageGeocode

key = 'd6385b140eb14ed09e77553377bc276c'

geocoder = OpenCageGeocode(key)
query = str(lacation)
results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

# myMap = folium.Map(lacation=[lat, lng], zoom_start=9)
# folium.Marker([lat,lng], popup=lacation).add_to(myMap)

# myMap.save("myLocation.html")



