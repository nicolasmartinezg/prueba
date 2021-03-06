from datetime import datetime, timezone

import requests

import pandas as pd
from sqlalchemy import create_engine

CLIENT_ID = '567b140cbd6748f9ae12d351df345f9a'
CLIENT_SECRET = '84860973650546f2b849837e4967f5a5'

AUTH_URL = 'https://accounts.spotify.com/api/token'
headers = {'Authorization': 'Bearer BQBCp0wqeo9uTIiG9nWEv9KZ97J2Pbw-UtQGWeV-5lgMjYrN4RvFTuhhQi8e3vXLE8mr6y218iI5igxp6zRh47Oe1o2rhy7B2k_oMpRXCI2EpWZsweTBI5beL9JJzPMlnz9oonpHpoe-QgQBqmSpl_V7s3zzyk'}
# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

BASE_URL = 'https://api.spotify.com/v1/'

#Variables para acceder a los datos de los artistas que me entrega la api en forma de json cuando se hace la conexion
nombres = []
Tipo = []
Uri=[]
Popularidad = []
seguidores = []
carga=[]
Origen=[]

artistas_id = ['36QJpDe2go2KgaRleHCDTp', '5M52tdBnJaKSvOpJGz8mfZ', '2ye2Wgw4gimLv2eAKyk1NB', '1zng9JZpblpk48IPceRWs8', '74ASZWbe4lXaubB36ztrGX','3fMbdgg4jU18AjLCKBhRSm' ]
for artista_id in artistas_id:
            r = requests.get(BASE_URL + 'artists/' + artista_id + '/top-tracks?market=ES' ,
                             headers=headers,
                             params={'include_groups': 'album', 'limit': 50})
            data = requests.get(BASE_URL + 'artists/' + artista_id ,
                             headers=headers,
                             )


artista_data=data.json()
tracks_data=r.json()["tracks"]



#variables para acceder a los datos  necesarios de las canciones que me entrega la api en forma de json
nombresTracks = []
TipoTrack = []
PopularidadTracks = []
Artistas = []
Fecha = []
id = []
urlTracks = []
Album = []
Generos = []
cargaTrack = []
OrigenTracks = []

nombres.append(artista_data["name"])
Tipo.append(artista_data['type'])
Uri.append(artista_data['uri'])
Popularidad.append(artista_data['popularity'])
seguidores.append(artista_data['followers']['total'])
now = datetime.now()
carga.append(now.replace(tzinfo=timezone.utc).timestamp())
Origen.append(artista_data['href'])

datosArtista = {'nombre': nombres,'Tipo':Tipo,'Uri':Uri,'popularidad':Popularidad,'seguidores':seguidores,'FechaCarga':carga,'Origen':Origen}
artistas = pd.DataFrame(data=datosArtista)
print(artistas)

tracks=[]
for track in tracks_data:

                OrigenTracks.append(track['href'])
                nombresTracks.append(track['name'])
                TipoTrack.append(track['type'])
                Artistas.append(track["artists"][0]["name"])
                Album.append(track["album"]["name"])
                PopularidadTracks.append(track["popularity"])
                Fecha.append(track["album"]["release_date"])
                id.append(track["id"])
                Generos.append(artista_data["genres"])
                urlTracks.append(track["uri"])
                now = datetime.now()
                cargaTrack.append(now.replace(tzinfo=timezone.utc).timestamp())
                OrigenTracks.append(track['href'])

datosCanciones = {'ID':id,'nombre': nombresTracks, 'Tipo': TipoTrack, 'Uri': urlTracks, 'popularidad': PopularidadTracks,'artista':Artistas,'FechaDeLanzamiento':Fecha,'Generos':Generos,'FechaCarga':cargaTrack}
Tracks = pd.DataFrame(data=datosCanciones)

print(Tracks)


engine = create_engine('postgresql://postgres:nicolas05@127.0.0.1:5432/datawarehouse')
artistas.to_sql('Artist', con=engine, index=False)