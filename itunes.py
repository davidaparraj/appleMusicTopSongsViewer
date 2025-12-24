import requests
import json


class Artist():
    def __init__(self, name: str, songs: int):
        self.__name = name
        self.__songs = songs

    def requestInfo(self):
        #Request the information of one artist from itunes API
        url = "https://itunes.apple.com/search"
        params = {"entity": "song", "limit": self.__songs, "term": self.__name}
        response = requests.get(url, params=params)
        return response.json() # Return the response as JSON
    
    def showInfo(self, results: dict):
        for i, result in enumerate(results["results"], start=1):
            print(f"{i:>2}. {result["trackName"]} - {result["collectionName"]} ({result["releaseDate"][:4]})") # Slice release date to show only year
    
    # Functions to raise exceptions for artist's name and number of songs
    @staticmethod
    def checkArtist(name):
        if not isinstance(name, str):
            raise TypeError("Enter a valid name") # Raise exception if data not inserted correctly
    @staticmethod
    def checkSongs(songs):
        if not isinstance(songs, int):
            raise TypeError("Enter a valid number")

    # Accesors
    @property
    def name(self):
        return self.__name
    @property
    def songs(self):
        return self.__songs


def main():
    # Loop to check for correct input
    while True:
        try:
            name = input("Enter the name of the desired artist: ")
            Artist.checkArtist(name)
            songs= int(input("Enter the amount of songs to display: "))
            Artist.checkSongs(songs)
        except TypeError as e:
            print(f"Invalid input: {e}")
        break

    # Create instance of Artist class
    artist = Artist(name, songs)
    artist_data = artist.requestInfo() # The data we requested gets back as JSON

    # Write data in new file
    with open(f"{artist.name}.json", "w") as file:
        json.dump(artist_data, file, indent=4)

    # Show data with instance method
    artist.showInfo(artist_data)

if __name__ == "__main__":
    main()
