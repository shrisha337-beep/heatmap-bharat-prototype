from fastapi import FastAPI # type: ignore
import pandas as pd # type: ignore
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, 'processed', 'clean_data.csv')

app = FastAPI()

df = pd.read_csv(
    CSV_PATH,
    usecols=["City", "Date", "AQI", "lat", "lon", "intensity"],
    nrows=1000
)

df = df.dropna()
@app.get("/")
def home(): # type: ignore
    return {"message": "Heatmap Bharat API is running"}

@app.get("/heatmap")
def get_heatmap(): # type: ignore
    try:
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}
    
from fastapi import FastAPI, Query # type: ignore
import pandas as pd # type: ignore
import os

app = FastAPI()

# Correct path handling
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, 'processed', 'clean_data.csv')

# Load limited + useful data
df = pd.read_csv(
    CSV_PATH,
    usecols=["City", "Date", "AQI", "lat", "lon", "intensity"],
    nrows=1000
)

df = df.dropna()

@app.get("/")
def home():
    return {"message": "Heatmap Bharat API is running"}


@app.get("/heatmap")
def get_heatmap(
    city: str = Query(None),
    start_date: str = Query(None),
    end_date: str = Query(None),
    min_aqi: int = Query(None),
    max_aqi: int = Query(None)
):
    data = df.copy()

    # 🔹 Filter by city
    if city:
        data = data[data["City"].str.lower() == city.lower()]

    # 🔹 Filter by date range
    if start_date and end_date:
        data["Date"] = pd.to_datetime(data["Date"])
        data = data[
            (data["Date"] >= start_date) &
            (data["Date"] <= end_date)
        ]

    # 🔹 Filter by AQI range
    if min_aqi is not None:
        data = data[data["AQI"] >= min_aqi]

    if max_aqi is not None:
        data = data[data["AQI"] <= max_aqi]

    return data.to_dict(orient="records")    