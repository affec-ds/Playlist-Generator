import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import os
from dotenv import load_dotenv
import time

# Cargar variables de entorno
load_dotenv()

# Autenticación con Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="playlist-read-private"
))

# Leer archivo CSV
df_playlist = pd.read_csv("playlist_sin_caracteristicas.csv")

# Filtrar solo los IDs válidos
track_ids = df_playlist["Track_ID"].dropna().unique().tolist()
track_ids = [track_id for track_id in track_ids if isinstance(track_id, str)]

print(f"🔍 Canciones válidas a procesar: {len(track_ids)}")

# Función para obtener audio features por lotes de 50


def obtener_features(track_ids):
    features = []
    for i in range(0, len(track_ids), 50):
        batch = track_ids[i:i+50]
        try:
            response = sp.audio_features(batch)
            if response:
                features.extend(response)
            else:
                print(f"⚠️ Lote vacío en rango [{i}-{i+50}]")
        except Exception as e:
            print(f"❌ Error en lote [{i}-{i+50}]: {e}")
        time.sleep(0.3)  # Pequeña pausa para evitar sobrecarga
    return features


# Obtener las características
audio_features = obtener_features(track_ids)

# Limpiar y convertir a DataFrame
df_features = pd.DataFrame([f for f in audio_features if f is not None])

# Renombrar y seleccionar columnas
df_features = df_features[["id", "danceability", "energy", "valence", "tempo"]].rename(columns={
    "id": "Track_ID",
    "danceability": "Danceability",
    "energy": "Energy",
    "valence": "Valence",
    "tempo": "Tempo"
})

# Unir con el dataset original
df_final = df_playlist.merge(df_features, on="Track_ID", how="left")

# Guardar resultado final
df_final.to_csv("playlist_completa.csv", index=False)
print("✅ ¡Listo! Archivo guardado como 'playlist_completa.csv'")
