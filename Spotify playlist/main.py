from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import spotipy

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials("xdd", "xdd"))

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()

URL = "https://www.billboard.com/charts/hot-100/"

input_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")

URL = URL + input_date + "/"
print(URL)
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
first_song = soup.find(name="ul", class_="o-chart-results-list-row // lrv-a-unstyle-list lrv-u-flex u-height-200 u-height-100@mobile-max u-height-100@tablet-only lrv-u-background-color-white a-chart-has-chart-detail")
songs_list = [first_song.h3.text.split("\t\t\t\t\t")[1].split('\t\t')[0]]

music_tags = soup.find_all(name="li", class_="o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light lrv-u-padding-l-050 lrv-u-padding-l-1@mobile-max")
for song in music_tags:
    songs_list.append(song.h3.text.split("\t\t\t\t\t")[1].split('\t\t')[0])

# to be continued...
# 2019-06-01