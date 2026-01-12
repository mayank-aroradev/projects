import requests
from bs4 import BeautifulSoup

date = input("Enter the date in this format YYYY-MM-DD: ")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}

url = f"https://musicchartsarchive.com/singles-chart/{date}"
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

rows = soup.find_all("tr", class_=["odd", "even"])

song_names = []
for row in rows:
    song = row.find("a")
    if song:
        song_names.append(song.get_text().strip())

print(song_names)

