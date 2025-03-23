from flask import Flask, render_template, request
import pandas as pd
import random

app = Flask(__name__)

# Cargar el dataset real desde archivo CSV
df = pd.read_csv("cleaned_dataset.csv")


emocion_a_cluster = {
    "felicidad": 2,
    "fiesta": 2,
    "motivacion": 3,
    "intensidad": 3,
    "relajacion": 1,
    "tristeza": 1,
    "balance": 0,
    "concentracion": 0
}

emocion_a_nombre = {
    "felicidad": "Siempre Feliz, Siempre Happy",
    "fiesta": "Mueve lo que Dios te dio",
    "motivacion": "Con to'sino pa' qué",
    "intensidad": "Let's Fcking Go!",
    "relajacion": "Paz Interior",
    "tristeza": "Salganse de Instagram, quiero estar solo",
    "balance": "Chill de cojones",
    "concentracion": "Saludo al Sol"
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generar", methods=["POST"])
def generar():
    emocion = request.form["emocion"]
    cluster_id = emocion_a_cluster.get(emocion, 2)
    nombre_playlist = emocion_a_nombre.get(emocion, "Mi Playlist")

    playlist = df.sample(n=5).to_dict(orient="records")

    return render_template("playlist.html", emocion=emocion.capitalize(), nombre_playlist=nombre_playlist, playlist=playlist)


if __name__ == "__main__":
    app.run(debug=True)
