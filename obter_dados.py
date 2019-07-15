#!/usr/bin/python3
import sys
import json
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def autentica(client_id, client_secret):
    client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)    
    return spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def nome_artista(sp, uri_artista):
    artist = sp.artist(uri)
    return artist['name'].replace(' ','_')

def features_top_tracks(sp, uri_artista):
    top_tracks = sp.artist_top_tracks(uri)
    uri_tracks = []
    for track in top_tracks['tracks']:
        uri_tracks.append(track['uri'])
    return sp.audio_features(uri_tracks)

def converte_json(features, artist):
    with open('features_' + artist.lower() + '.json','w') as fp:
        json.dump(features, fp)
    print('Features convertido para json.')

def converte_csv(features, artist):
    df = pd.DataFrame(features)
    df.to_csv('features_' + artist.lower() + '.csv', index=False)
    print('Features convertido para csv.')

if __name__ == "__main__":
    while True:
        try:
            uri = sys.argv[1]
            spotify = autentica('CLIENT_ID',
                                'CLIENT_SECRET')
            artista = nome_artista(spotify, uri)
            features = features_top_tracks(spotify, uri)
            converte_csv(features, artista)
            converte_json(features, artista) 
            break   
        except spotipy.oauth2.SpotifyOauthError: 
            print('Informe o Client ID & Client Secret.')
            sys.exit()
        except IndexError: 
            print('Informe a URI do Artista.')
            sys.exit()
