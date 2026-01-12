import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
soup=BeautifulSoup(response.text,"html.parser")
all_movies= soup.find_all(name="h2")
movie_titles= [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("top_100_movies.txt","w",encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
print(movie)

