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
#Variables para acceder a los datos de los artistas
nombres = []
Tipo = []
Uri=[]
Popularidad = []
seguidores = []
carga=[]
Origen=[]
