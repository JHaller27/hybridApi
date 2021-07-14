from typing import Optional
from fastapi import FastAPI
import models
import scraper


app = FastAPI(title="Hybrid Calisthenics API")


@app.get("/", response_model=list[models.ExerciseType])
def home():
    return scraper.get_exercises()


@app.get("/debug", response_model=models.Debug)
def debug():
    import os
    keys = {k: v for k, v in os.environ.items()}
    return models.Debug(data={"os_environ_keys": keys})
