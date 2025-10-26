import requests

# Function to raise exceptions for artist's name and number of songs
def checkArtist(name):
    if not isinstance(name, str):
        raise TypeError("Enter a valid name") # Raise exception if data not inserted correctly

def checkSongs(songs):
    if not isinstance(songs, int):
        raise TypeError("Enter a valid number")
    
# Loop to check for correct input
while True:
    try:
        artist = input("Enter the name of the desired artist: ")
        checkArtist(artist)
        songs = int(input("Enter the amount of songs to display: "))
        checkSongs(songs)
    except TypeError as e:
        print(f"Invalid input: {e}")
    break

#Request the information of one artist from itunes API
url = "https://itunes.apple.com/search"
params = {"entity": "song", "limit": songs, "term": artist}
response = requests.get(url, params=params)
    
# The data we requested gets back as JSON
o = response.json()
# Organize data to show top songs of artist and other details
print(f"{artist} top {songs} results:\n")
for i, result in enumerate(o["results"], start=1):
    print(f"{i:>2}. {result["trackName"]} - {result["collectionName"]} ({result["releaseDate"][:4]})") # Slice release date to show only year
