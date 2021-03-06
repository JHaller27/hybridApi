from bs4 import BeautifulSoup
import requests
import re
import models


def get_exercises() -> list[models.ExerciseType]:
    sub_heading_regex = re.compile(r"^(?P<pos>\d+).*")

    response = requests.get("https://www.hybridcalisthenics.com/routine")

    soup = BeautifulSoup(response.content, features="html.parser")
    start_h1 = soup.find("h1")

    while "How Should We Do".lower() not in start_h1.text.lower():
        start_h1 = start_h1.find_next("h1")

    all_h1s = start_h1.find_all_next("h1")
    workouts = [h.text for h in all_h1s]

    all_h3s = start_h1.find_all_next("h3")

    sub_workouts = [[]]
    prev_id = -1

    for h in all_h3s:
        if mo := sub_heading_regex.match(h.text):
            pos = int(mo['pos'])
            if pos < prev_id:
                sub_workouts.append([])
            prev_id = pos

            p = h.find_next("p")

            sub_workouts[-1].append((h.text, p.text))

    retv = []
    for w, sws in zip(workouts, sub_workouts):
        retv.append(models.ExerciseType(name=w, exercises=[]))

        for sw, goal in sws:
            retv[-1].exercises.append(models.Exercise(name=sw, goal=goal))

    return retv
