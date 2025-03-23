import time
import pandas as pd
import requests

# Función para obtener características de canciones en lotes más pequeños


def obtener_features(track_ids, batch_size=10, max_retries=3):
    """
    Obtiene características de canciones en lotes pequeños con reintentos en caso de fallos.
    """
    all_features = []

    for i in range(0, len(track_ids), batch_size):
        batch = track_ids[i:i + batch_size]
        print(f"🔄 Procesando lote {i}-{i + batch_size} de {len(track_ids)}...")

        retries = 0
        while retries < max_retries:
            try:
                # Hacemos la solicitud a MusicBrainz u otra API
                response = requests.get(
                    f"https://api.spotify.com/v1/audio-features?ids={','.join(batch)}")
                response.raise_for_status()  # Si hay error, lanza una excepción

                data = response.json()
                all_features.extend(data["audio_features"])

                print(f"✅ Lote {i}-{i + batch_size} procesado correctamente.")
                break  # Salir del bucle si la solicitud fue exitosa

            except requests.exceptions.RequestException as e:
                print(f"❌ Error en lote {i}-{i + batch_size}: {e}")
                retries += 1
                time.sleep(10)  # Esperar 10 segundos antes de reintentar

        if retries == max_retries:
            print(
                f"⚠ Lote {i}-{i + batch_size} omitido tras {max_retries} intentos fallidos.")

    return pd.DataFrame(all_features)
