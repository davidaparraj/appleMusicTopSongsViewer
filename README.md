# Apple Music Top Songs Viewer (Python)

## Overview
This Python program retrieves and displays the **top songs** of a given artist using the **iTunes Search API** based on user input.  
It was developed to practice **API integration**, **JSON data handling**, and **Python data structures**, while reinforcing clean and readable program design.  
The program saves the results in a JSON file if anyone wants to use it for data analysis.

---

## Features
- Fetches an artist’s top tracks from the iTunes API based on the user's input. 
- Displays song titles, album names, and release years in a formatted output.  
- Handles user input for any artist name.
- Parses and structures JSON data from API responses.
- Implements basic error handling for invalid or missing inputs.

---

## Concepts Practiced
- REST API requests using the `requests` library  
- JSON parsing and dictionary traversal  
- Data organization and string formatting in Python

# Example Output
Enter the name of the desired artist: 

Enter the amount of songs to display: 

The Weeknd top 5 results:

 1. Call Out My Name - My Dear Melancholy, (2018)
 2. Blinding Lights - Blinding Lights - Single (2019)
 3. Die For You - Starboy (2016)
 4. One Of The Girls - The Idol Episode 4 (Music from the HBO Original Series) - Single (2023)
 5. I Feel It Coming (feat. Daft Punk) - Starboy (2016)

## How to Run
1. Clone this repository:  
   git clone https://github.com/davidaparraj/appleMusicTopSongsViewer.git  
   cd appleMusicTopSongsViewer
3. Install dependencies:
   pip install requests
4. Run the program:
   python itunes.py

## Author
**David Parra**  
Computer Science Sophomore @ Florida Polytechnic University  
 Concentrations: Software Engineering & Machine Learning  
 [LinkedIn](https://linkedin.com/in/davidaparraj) | [GitHub](https://github.com/davidaparraj)

