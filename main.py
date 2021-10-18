import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint

album_in = 'https://open.spotify.com/album/6OQ9gBfg5EXeNAEwGSs6jK?si=OivWWXdtTd6ea4v4mQpIhw' #album url 

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials()) #spotify connection 


# data collection 
results = spotify.album(album_in)
n_tracks = results['total_tracks']
cover_art = results['images'][0]['url']

album_tracks = []
for track in results['tracks']['items']:
    album_tracks.append(track['name'])

print(cover_art)
print(album_tracks)