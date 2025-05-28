from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os
from fastapi.middleware.cors import CORSMiddleware  # ✅ CORS-Import

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# ✅ CORS aktivieren
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # oder: ["http://localhost:5173"] für gezielte Freigabe
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
