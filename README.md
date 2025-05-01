# 🎬 MovieMeld

**MovieMeld** is a fun and simple web app built with Streamlit that helps two users discover movies they’re both likely to enjoy. Based on shared preferences like genre, runtime, reviews, and release era, the app returns a short list of movie suggestions—complete with posters, overviews, and key details.

> **Data source:** [IMDb Top 1000 Movies Dataset](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows)

---

## 🚀 Demo

Try it live on **[Streamlit Cloud](https://moviemeld.streamlit.app/)**

---

## 🔍 Features

- Dual-user input: each user selects their preferences for:
  - Favorite genres
  - IMDb rating
  - Runtime
  - Release category (Modern or Classic)
- Smart matching algorithm using similarity scoring
- Returns 3 random top-matching movies
  - Includes poster, title, director, runtime, and overview

---

## 🛠️ Tech Stack

- **Python**
- **Pandas**
- **Streamlit** – for the interactive user interface

---

## 💡 Potential Improvements

- **Expanded Dataset**  
  Currently, MovieMeld uses a static CSV of the top 1,000 IMDb titles. While it's a high-quality dataset, it can lack diversity—particularly for niche preferences (e.g., short biographical films)—which may result in weaker recommendations.

- **Richer Preferences**  
  Adding more filters such as age-appropriateness, language, or tone (e.g., dark, lighthearted, romantic) could improve the recommendation quality even further.
