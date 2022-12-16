from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
import requests
import spotipy

spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-public",
        redirect_uri="http://example.com",
        client_id="****",
        client_secret="****",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = spotify.current_user()["id"]

URL = "https://www.billboard.com/charts/hot-100/"

input_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")

URL = URL + input_date + "/"
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
first_song = soup.find(name="ul", class_="o-chart-results-list-row // lrv-a-unstyle-list lrv-u-flex u-height-200 u-height-100@mobile-max u-height-100@tablet-only lrv-u-background-color-white a-chart-has-chart-detail")
songs_list = [first_song.h3.text.split("\t\t\t\t\t")[1].split('\t\t')[0]]
first_artist = soup.find(name="div", class_="lrv-u-flex u-align-items-center@mobile-max")
artist_list = [first_artist.p.text]

music_tags = soup.find_all(name="li", class_="o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light lrv-u-padding-l-050 lrv-u-padding-l-1@mobile-max")
for song in music_tags:
    artist_list.append(song.span.text.split('\n\t\n\t')[1].split('\n')[0])
    songs_list.append(song.h3.text.split("\t\t\t\t\t")[1].split('\t\t')[0])

year = input_date.split('-')[0]
spotify_list = []
index = 0
for track in songs_list:
    spotify_list.append(spotify.search(
            q=f"track: {track} artist: {artist_list[index]}",
            limit=1,
            type='track'
        )['tracks']['items'][0]['uri']
    )
    index += 1
spotify_playlist = spotify.user_playlist_create(user=user_id, name=f"{input_date} Billboard 100", public=True, description=f"This playlist contains Billboard Top 100 tracks for {input_date}")
spotify_playlist_id = spotify_playlist['id']

spotify.playlist_add_items(playlist_id=spotify_playlist_id, items=spotify_list, position=None)
