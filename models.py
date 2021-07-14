from typing import Any
from pydantic import BaseModel


class Exercise(BaseModel):
    name: str
    goal: str


class ExerciseType(BaseModel):
    name: str
    exercises: list[Exercise]

