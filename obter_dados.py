import sys
import json
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Autenticação com a API Spotify
client_credentials_manager = SpotifyClientCredentials(client_id = 'CLIENT_ID',
                                                      client_secret='CLIENT_SECRET')
# Objeto Spotipy
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

# Argumento
uri = sys.argv[1]

# Obtendo nome do artista
artist = sp.artist(uri)
artist = artist['name'].replace(' ','_')

# Obtendo melhores tracks
top_tracks = sp.artist_top_tracks(uri)

# Obtendo 'uri' das melhores tracks
uri_tracks = []
for track in top_tracks['tracks']:
    uri_tracks.append(track['uri'])

# Obtendo 'features'
features = sp.audio_features(uri_tracks)

# Convertendo para JSON
with open('features_' + artist.lower() + '.json','w') as fp:
    json.dump(features, fp)

# Convertendo para CSV
df = pd.DataFrame(features)
df.to_csv('features_' + artist.lower() + '.csv', index=False)
