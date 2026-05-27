
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import random

app = FastAPI()

gpt_url = "https://chatgpt.com/"
google_url = "https://www.google.com/"
youtube_url = "https://www.youtube.com/"

mapp = {}
mapp_2={}
def mapping_to_different_value():

    
    mapp[google_url] = "http:127.0.0.1:8000/google"
    mapp[gpt_url] = "http:127.0.0.1:8000/gpt"
    mapp[youtube_url] = "http:127.0.0.1:8000/youtube"

    print(mapp)

mapping_to_different_value()

def random_number_generator():
    num = random.randint(1,10)
    return num

def url_builder():
    local_host_url = "http:127.0.0.1:8000/"
    num = str(random_number_generator())
    new_url = local_host_url + num
    return new_url,num

@app.get("/get_url")
def get_short_url():
    return mapp

@app.get("/create_url_shortner")
def create_url_shortner(url: str):

    print(f"old URL : {url}")
    new_url,num = url_builder()
    print(f"new URL : {new_url}")
    mapp[num] = new_url
    mapp_2[num] = url
    response = {
        "old_url":url,
        "new_url":new_url
    }
    return response


@app.get("/{url}")
def get_old_url(url: str):
    print(mapp)
    print(mapp[url])
    return RedirectResponse(url = mapp_2[url])


@app.get("/google")
def test():
    print(mapp[google_url])
    print("hi")
    return RedirectResponse(url ="https://google.com")

@app.get("/gpt")
def test():
    return RedirectResponse(url=gpt_url)

@app.get("/youtube")
def test():
    return RedirectResponse(url=youtube_url)
