import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint
import requests
import os 

album_in = 'https://open.spotify.com/album/6OQ9gBfg5EXeNAEwGSs6jK?si=OivWWXdtTd6ea4v4mQpIhw' #album url 

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials()) #spotify connection 


# data collection 
results = spotify.album(album_in)
album_name = results['name']
n_tracks = results['total_tracks']
cover_art = results['images'][0]['url']

album_tracks = []
for track in results['tracks']['items']:
    album_tracks.append(track['name'])

print(cover_art)
print(album_tracks)
print(album_name)

#retrieve image and place in new folder
img_data = requests.get(cover_art).content
filename = album_name + "/cover.png"
os.makedirs(os.path.dirname(filename), exist_ok=True)

with open(filename, 'wb') as handler:
    handler.write(img_data)

