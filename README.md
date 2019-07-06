# Obtendo features das melhores músicas do Spotify

Script para obtenção de features das melhores músicas de um artista pela API do Spotify em formatos JSON e CSV. 

## Objetivo
Analisar diversas características da música e visualizar graficamente como estão distrubuídos esses dados.

### API

O [Spotipy](https://github.com/plamere/spotipy), biblioteca Python, suporta todos os recursos da API do Spotify Web, incluindo o acesso a todos os endpoints e autorização do usuário. Para obter detalhes sobre os recursos, recomendo que você leia a documentação da [API do Spotify](https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/).

### URI  
A URI do Spotify (Uniform Resource Indicator) é um link que você pode encontrar no menu Compartilhar de qualquer faixa, álbum ou Perfil do Artista no Spotify.

#### Obtendo URI
1. Abra o Spotify e procure por um artista.

2. Clique em 'More'
<p>
  <img src="https://i.ibb.co/y8S3d6R/nirvana.png" width="550">
</p>

3. Clique em 'Share' e em seguida 'Copy Spotify URI'
<p>
  <img src="https://i.ibb.co/mJ4Z1Ww/nirvana2.png" width="550">
</p>

### Running
1. Clone esse repo
```
$ git clone https://github.com/sidney-neto/features-spotipy
$ cd features-spotipy/
```

2. Execute Python informando como argumento a URI
```
$ python3 obter_dados.py [URI]
```

3. Dados
```
features_nirvana.csv
features_nirvana.json
```
### Features
- acousticness - Valores de 0,0 a 1,0 que representam a acústica.
- analysis_url - URL HTTP pra acesso de análise da música.
- danceability - Valores de 0,0 a 1,0 que representam a dancibilidade.
- duration_ms - Duração em milissegundos.
- energy - Valores de 0,0 a 1,0 que representam a energia.
- id - ID da música.
- instrumentalness - Valores de 0,0 a 1,0 que representam a instrumentalidade.
- key - Valores para classe de afinação.
- liveness - Valores de 0,0 a 1,0 que representam se há presença de público (Show ao vivo).
- loudness - Valor de sonoridade em decibéis (dB).
- mode -Indica a modalidade
- speechiness - Valores de 0,0 a 1,0 que representam a fonação.
- tempo - Tempo total em batidas por minuto (BPM).
- time_signature - Numero de batidas em cada barra.
- track_href - Link para detalhamento de música.
- type - Tipo de objeto.
- uri - Spotify URI.
- valence - Valores de 0,0 a 1,0 que representam a positividade.
