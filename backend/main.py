from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class BerichtInput(BaseModel):
    stichpunkte: str

@app.post("/bericht")
def erstelle_bericht(data: BerichtInput):
    prompt = f"""
Du bist ein Pflegeassistent. Erstelle aus folgenden Stichpunkten einen sachlichen Pflegebericht:

Stichpunkte: {data.stichpunkte}
"""
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return {"bericht": response.choices[0].message["content"]}
