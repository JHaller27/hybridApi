from typing import Any, Optional
from fastapi import FastAPI
import models
import scraper


app = FastAPI(title="Hybrid Calisthenics API")


@app.get("/", response_model=list[models.ExerciseType])
def home():
    return scraper.get_exercises()


@app.get("/debug", response_model=dict[str, Any])
def debug():
    import os
    keys = {k: v for k, v in os.environ.items()}
    return {"os_environ_keys": keys}
