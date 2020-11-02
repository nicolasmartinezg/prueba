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
artistas_id = ['2ye2Wgw4gimLv2eAKyk1NB', '1zng9JZpblpk48IPceRWs8', '74ASZWbe4lXaubB36ztrGX','3fMbdgg4jU18AjLCKBhRSm','36QJpDe2go2KgaRleHCDTp', '5M52tdBnJaKSvOpJGz8mfZ',]
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


#Variables para acceder a los datos de los artistas que me entrega la api en forma de json cuando se hace la conexion
nombres = []
Tipo = []
Uri=[]
Popularidad = []
seguidores = []
carga=[]
Origen=[]
