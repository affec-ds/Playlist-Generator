# 🎧 Playlist Generator

### Autor: Affectus Jaureguizar
### Fecha: 20 de Marzo, 2025

---

## 📄Descripción del Proyecto

Aplicación web interactiva que recomienda canciones según el estado emocional del usuario, utilizando clustering de características acústicas. Desarrollada con **Python**, **Flask** y un dataset real de más de 20.000 canciones.

---

## 🧠 Objetivo del Proyecto

Construir un sistema de recomendación musical que entregue playlists personalizadas, alineadas al estado emocional seleccionado por el usuario, mediante técnicas de análisis exploratorio y aprendizaje no supervisado.

---

## 🚀 Demo desplegada

👉 [Probar la aplicación en Render](https://playlistgenerator-vwec.onrender.com/)

---

## 🛠️ Tecnologías Utilizadas

- Python 3
- Jupyter Notebook
- Flask
- Pandas · Scikit-learn · Matplotlib · Seaborn
- HTML + Bootstrap (interfaz simple)

---

## 🧬 Metodología

1. **Dataset**  
   Más de 20.000 canciones con variables como `valence`, `energy`, `danceability` y `tempo`. Obtenido a través de [Google Dataset Search](https://datasetsearch.research.google.com/), con redirección a Kaggle.

2. **EDA**  
   Análisis exploratorio para comprender la distribución emocional de las canciones y su agrupamiento natural.

3. **Clustering**  
   Uso de K-Means para segmentar las canciones en clusters representativos de distintos estados emocionales ("moods").

4. **Recomendación**  
   El usuario selecciona una emoción y la app devuelve canciones pertenecientes al cluster más alineado a ese estado emocional.

5. **Despliegue Web**  
   El flujo fue migrado a Flask para transformar el proyecto en una aplicación web funcional y accesible.

---

## 🎯 Funcionalidades principales

- Selección de emoción desde la interfaz.
- Recomendación automática de canciones según estado emocional.
- Regeneración de playlist con la misma emoción.
- Opción de cambiar de emoción y generar una nueva playlist.
- Flujo de usuario limpio, visual simple y funcionamiento estable.

---

## ▶️ Cómo ejecutar este proyecto

1. **Clona este repositorio:**
   ```bash
   git clone https://github.com/affec-ds/Playlist-Generator.git

2. **Navega al directorio del proyecto:**
   cd Playlist-Generator
3. **Instala las dependencias:**
   pip install -r requirements.txt
4. **Ejecuta la aplicación localmente:**   
   flask run

---

## 📩 Contacto

💼[Conectemos en LinkedIn](https://cl.linkedin.com/in/affectusjaureguizar)

💼[GitHub](https://github.com/affec-ds)
