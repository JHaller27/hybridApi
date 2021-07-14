from typing import Optional
from fastapi import FastAPI
import models
import scraper


app = FastAPI(title="Hybrid Calisthenics API")


@app.get("/", response_model=models.Response)
def home():
    return scraper.get_exercises()


@app.get("/debug", response_model=models.Debug)
def debug():
    import os
    keys = [k for k in os.environ.keys()]
    return models.Debug(data={"os_environ_keys": keys})
