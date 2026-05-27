from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import random

app = FastAPI()

mapp = {}

def generate_id():
    return str(random.randint(1000,9999))

@app.get("/create")
def create(url: str):

    short_id = generate_id()

    mapp[short_id] = url

    return {
        "short_url": f"http://127.0.0.1:8000/{short_id}"
    }

@app.get("/{short_id}")
def redirect(short_id: str):

    if short_id not in mapp:
        return {"error":"URL not found"}

    return RedirectResponse(url=mapp[short_id])
