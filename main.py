from fastapi import FastAPI
import pandas as pd

# from data_preprocessing import pipe_prepocessing

df =pd.read_csv('spotify_tracks.csv')

app = FastAPI()

# Count of songs per year
@app.get("/")
def read_root():
    df = pd.read_csv('spotify_tracks.csv')

    countByYear = df.groupby(['year']).size().to_dict()
    test = df.head().to_dict()

    return {"message": "Bienvenue sur FastAPI !", "songsByYear": countByYear}

# Name and artists with parameter year
@app.get("/year/{year}")
def songs_by_year(year: int):
    df = pd.read_csv('spotify-data.csv')

    filtered = df[df['year'] == year]
    songs = filtered[['name', 'artists']].to_dict(orient='records')

    return {"year": year, "songs": songs}

# Count songs per artist per year
@app.get("/artist/{year}")
def song_per_artist(year: int):
    df = pd.read_csv('spotify-data.csv')

    filtered = df[df['year'] == year]
    songsPerArtist = filtered.groupby(['artists']).size().sort_values(ascending=False).to_dict()

    return {"year": year, "songsPerArtist": songsPerArtist}

# Acousticness per year
@app.get("/acousticness-per-year")
def acousticness():
    df = pd.read_csv('spotify-data.csv')

    average = df.groupby('year')['acousticness'].mean().sort_values(ascending=False).to_dict()

    return {"average_acousticness": average}

# Positivness depending on the mode
@app.get("/positivness-mode")
def positivness():
    df = pd.read_csv('spotify-data.csv')

    positivness = df.groupby('mode')['valence'].mean().sort_values(ascending=False).to_dict()
    mode = df.groupby(['mode']).size().to_dict()
    sum = df.describe()

    return {"sum": sum, "positivness": positivness, "mode": mode}



@app.post("/items/")
def create_item(item: dict):
    return {"message": "Item créé avec succès", "item": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    return {"message": "Item mis à jour avec succès", "item_id": item_id, "item": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": "Item {item_id} supprimé avec succès"}
