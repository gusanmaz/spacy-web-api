from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import requests
import uvicorn
import spacy


class Item(BaseModel):
    text: str


app = FastAPI()
nlp = spacy.load("en_core_web_sm")


@app.post("/text2sent")
async def create_item(item: Item):
    doc = nlp(item.text)
    sent_list = []
    for sent in doc.sents:
        sent_list.append(sent.text)
    return sent_list


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
