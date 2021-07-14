from fastapi import FastAPI
import models
import scraper


app = FastAPI(title="Hybrid Calisthenics API")


@app.get("/", response_model=models.Response)
def home():
    return scraper.get_exercises()
