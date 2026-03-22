from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os

app = FastAPI()

# CORS (must be right after app creation)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Path setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, 'processed', 'clean_data.csv')

# Load data
df = pd.read_csv(
    CSV_PATH,
    usecols=["City", "Date", "AQI", "lat", "lon", "intensity"],
    nrows=1000
)

df = df.dropna()

# Home route
@app.get("/")
def home():
    return {"message": "Heatmap Bharat API is running"}

# Heatmap route with filters
@app.get("/heatmap")
def get_heatmap(
    city: str = Query(None),
    start_date: str = Query(None),
    end_date: str = Query(None),
    min_aqi: int = Query(None),
    max_aqi: int = Query(None)
):
    data = df.copy()

    if city:
        data = data[data["City"].str.lower() == city.lower()]

    if start_date and end_date:
        data["Date"] = pd.to_datetime(data["Date"])
        data = data[
            (data["Date"] >= start_date) &
            (data["Date"] <= end_date)
        ]

    if min_aqi is not None:
        data = data[data["AQI"] >= min_aqi]

    if max_aqi is not None:
        data = data[data["AQI"] <= max_aqi]

    return data.to_dict(orient="records")