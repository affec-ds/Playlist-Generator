import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configurar autenticación con Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope=""
))

# ID de la playlist a extraer
PLAYLIST_ID = "6Wuuat5PpV1RPTLF7ewZVL"

# Función para extraer TODAS las canciones de la playlist


def obtener_canciones_playlist(playlist_id):
    offset = 0  # Controla la posición en la playlist
    canciones = []  # Lista para almacenar los datos

    while True:
        # Pedimos 100 canciones por solicitud
        results = sp.playlist_tracks(playlist_id, offset=offset, limit=100)
        tracks = results["items"]

        if not tracks:
            break  # Si no hay más canciones, terminamos el proceso

        for item in tracks:
            track = item["track"]
            if track:
                canciones.append({
                    "Artist": track["artists"][0]["name"],
                    "Track": track["name"],
                    "Album": track["album"]["name"],
                    "Danceability": None,  # Se llenará después con características de audio
                    "Energy": None,
                    "Valence": None,
                    "Tempo": None,
                    "Track_ID": track["id"]
                })

        offset += 100  # Avanzamos al siguiente bloque de 100 canciones
        # Mostramos el progreso
        print(f"Descargadas {len(canciones)} canciones...")

    return pd.DataFrame(canciones)


# Obtener todas las canciones
df_playlist = obtener_canciones_playlist(PLAYLIST_ID)

# Guardar los datos en un CSV
df_playlist.to_csv("playlist_sin_caracteristicas.csv", index=False)

print("✅ Playlist extraída correctamente. Archivo guardado: playlist_sin_caracteristicas.csv")
