"""This module allows you to quickly get the coordinates
of a building by address in any city of Ukraine"""
import requests as rq


base_path = "https://nominatim.openstreetmap.org/search?q="
print("""Enter the address you want to geolocate.
 Please, enter names of objects correctly.
 Ukrainian or English, case insensitive. 
 Example (ukr/eng):
 Oblast(region): Донецька / Donetsk
 Settlement: Костянтинівка / Kostiantynivka
 Street: Богдана Хмельницького / Bohdana Khmelnytskoho
 Number: 23""")
oblast = input("Enter an oblast(region) name: ").strip()
settlement = input("Enter a settlement name: ").strip().replace(' ', '%20')
street = input("Enter a street name: ").strip().replace(' ', '%20')
number = input("Enter a house/building number: ").strip()
url = base_path + f"{number}+{street}+{settlement}+{oblast}+Ukraine&format=geocodejson"
req = rq.get(url)
if req:
    geodata = req.json()
    features = geodata["features"]
    if features:
        coords = features[0]["geometry"]["coordinates"]
        print(f"Latitude {coords[1]}, Longtitude {coords[0]}")
    else:
        print("Not found. Please, check the correctness of the entered data.")
else:
    print("Request error:", req.status_code)
