from fastapi import FastAPI
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, 'processed', 'clean_data.csv')

app = FastAPI()

df = pd.read_csv(CSV_PATH)
df = df.dropna()

@app.get("/")
def home():
    return {"message": "Heatmap Bharat API is running"}

@app.get("/heatmap")
def get_heatmap():
    try:
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}