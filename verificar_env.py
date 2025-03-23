import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Obtener valores de las variables de entorno
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

# Verificar si se cargaron correctamente
if client_id and client_secret and redirect_uri:
    print("✅ Variables de entorno cargadas correctamente.")
    # Ocultar parte del ID por seguridad
    print(f"SPOTIPY_CLIENT_ID: {client_id[:5]}********")
    print(f"SPOTIPY_REDIRECT_URI: {redirect_uri}")
else:
    print("❌ ERROR: No se cargaron las variables de entorno. Revisa el archivo .env.")
