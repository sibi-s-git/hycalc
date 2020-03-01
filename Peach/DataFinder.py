import hypixel
import requests
import json
import base64
import io
import nbt

#setting API key
API_KEYS = ['f7200f1d-cc21-44c6-ba14-9f3a06a1486a']
hypixel.setKeys(API_KEYS)

#getting player info

#ign = input("Enter Your In Game Username Here: ")
ign = "hax_gaming"

#profile = input("Enter Your Preffered Profile: ")
profile = "Coconut"

profileId0 = "', 'cute_name': '" + profile 

Player = hypixel.Player(ign)

#defining decrypter

def decode_inventory_data(raw):
   data = nbt.nbt.NBTFile(fileobj = io.BytesIO(base64.b64decode(raw)))
   print('===============data=====')
   print(data.pretty_tree())

#requesting information for first link

url = "https://api.hypixel.net/player?key=f7200f1d-cc21-44c6-ba14-9f3a06a1486a&name=" + ign
response = requests.get(url)

#finding profile id for second link

json_response = response.json()
json_profile = json_response['player']['stats']['SkyBlock']['profiles']
profileStr = str(json_profile)
secondProfile = profileStr.find(profileId0)
firstProfile = profileStr.find("id")
print(firstProfile)
AccFirstProfile = firstProfile + 6
print(AccFirstProfile)
completeProfileId= profileStr[AccFirstProfile:secondProfile]
print(completeProfileId)

#requesting information for second link

newUrl = "https://api.hypixel.net/skyblock/profile?key=f7200f1d-cc21-44c6-ba14-9f3a06a1486a&profile=" + completeProfileId
newResponse = requests.get(newUrl)
newJson_response = newResponse.json()

#finding data values in new link

myValue = newJson_response['profile']['members'][completeProfileId]['inv_armor']['data']
data = decode_inventory_data(myValue)


myValue1 = newJson_response['profile']['members'][completeProfileId]['inv_contents']['data']
data = decode_inventory_data(myValue1)


myValue2 = newJson_response['profile']['members'][completeProfileId]['talisman_bag']['data']
data = decode_inventory_data(myValue2)



