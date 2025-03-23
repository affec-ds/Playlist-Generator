import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

# Configurar la autenticación con Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="user-library-read"  # Permiso para leer la biblioteca del usuario
))

# Probar la autenticación obteniendo el perfil del usuario actual
try:
    user_info = sp.current_user()
    print("✅ Autenticación exitosa.")
    print(f"Usuario: {user_info['display_name']} ({user_info['id']})")
except Exception as e:
    print("❌ ERROR en la autenticación:", e)
