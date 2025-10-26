import json
import requests
import sys

#if len(sys.argv) != 2:
    #sys.exit()
artist = "Kendrick Lamar"

#Request the information of one artist from itunes
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + artist)

# print(response.json()) The data we requested gets backs as json
#print(json.dumps(response.json(), indent=2)) #the data is indented and is better organized


o = response.json()
for result in o["results"]:
    print(result["trackName"])
