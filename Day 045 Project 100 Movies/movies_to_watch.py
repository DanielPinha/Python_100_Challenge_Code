from bs4 import BeautifulSoup
import requests

empire_response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
empire_response.raise_for_status()

empire_content = empire_response.text
soup = BeautifulSoup(empire_content, 'html.parser')

movies_text = soup.find_all('h3', 'title')
movies_title = [movie.getText() for movie in movies_text]
movies_title.reverse()

with open('movies.txt', mode='w', encoding='utf-8') as file:
    file.write("Movies To Watch:")
    for movie in movies_title:
        file.write('\n'+movie)
