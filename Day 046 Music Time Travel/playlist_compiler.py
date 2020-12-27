from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

BILLBOARD_URL = 'https://www.billboard.com/charts/hot-100/'
SPOTIFY_ID = os.getenv('SPOTIFY_ID')
SPOTIFY_KEY = os.getenv('SPOTIFY_KEY')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')


input_data = input("Which year do you want to travel to? Type in the format YYYY-MM-DD: ")

billboard_response = requests.get(f'{BILLBOARD_URL}{input_data}')
billboard_response.raise_for_status()

soup = BeautifulSoup(billboard_response.text, 'html.parser')
song_titles = [song.getText() for song in
               soup.find_all('span', 'chart-element__information__song text--truncate color--primary')]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    client_id=SPOTIFY_ID,
    client_secret=SPOTIFY_KEY,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    cache_path="token.txt"))
user_id = sp.current_user()["id"]

song_uris = []
for song in song_titles:
    result = sp.search(q=f"track:{song}", type="track", limit=1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
playlist_name = f'Billboard_{input_data}'
new_playlist = sp.user_playlist_create(user_id, playlist_name, public=False, description='Billboard Playlist')
new_playlist_id = new_playlist['id']

sp.playlist_add_items(new_playlist_id, song_uris)
