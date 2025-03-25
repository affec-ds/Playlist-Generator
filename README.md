# 🎧 Playlist Generator

### Author: Affectus Jaureguizar  
### Date: March 20, 2025  

---

## 📄 Project Description

An interactive web application that recommends songs based on the user’s emotional state using clustering of acoustic features. Built with **Python**, **Flask**, and a real dataset of over 20,000 songs.

---

## 🧠 Project Objective

To develop a music recommendation system that generates personalized playlists aligned with the user's selected emotional state, using exploratory data analysis and unsupervised learning techniques.

---

## 🚀 Live Demo

👉 [Try the app on Render](https://playlistgenerator-vwec.onrender.com/)

---

## 🛠️ Technologies Used

- Python 3
- Jupyter Notebook
- Flask
- Pandas · Scikit-learn · Matplotlib · Seaborn
- HTML + Bootstrap (simple interface)

---

## 🧬 Methodology

1. **Dataset**  
   More than 20,000 songs containing variables like `valence`, `energy`, `danceability`, and `tempo`, obtained through [Google Dataset Search](https://datasetsearch.research.google.com/) and redirected to Kaggle.

2. **EDA (Exploratory Data Analysis)**  
   Visual exploration of audio variables to understand the emotional distribution and natural grouping of songs.

3. **Clustering**  
   K-Means clustering is used to group songs into clusters representing different emotional "moods".

4. **Recommendation**  
   The user selects an emotion, and the app recommends songs from the cluster that best matches that emotional state.

5. **Web Deployment**  
   The workflow was migrated to Flask, transforming the project into a functional and accessible web application.

---

## 🎯 Key Features

- Emotion selection from the interface.
- Automatic playlist generation based on the selected emotion.
- Option to regenerate a playlist with the same emotion.
- Option to switch emotion and generate a new playlist.
- Clean user flow, simple design, and stable functionality.

---

## ▶️ How to Run Locally

1. **Clone this repository:**
   ```bash
   git clone https://github.com/affec-ds/Playlist-Generator.git

2. Navigate to the project directory:
   ```bash
   cd Playlist-Generator

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the Flask application locally:
   ```bash
   flask run

---

## 📩 Contact
Visit my full GitHub profile: github.com/affec-ds
