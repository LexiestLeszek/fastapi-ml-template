# main file

import uvicorn
from os import getenv
from fastapi import FastAPI
from pydantic import BaseModel
from model import predict_pipeline
from model import __version__ as model_version

app = FastAPI()

class TextIn(BaseModel):
    text: str

class PredictionOut(BaseModel):
    language: str

@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}

@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    language = predict_pipeline(payload.text)
    return {"language": language}

if __name__ == "__main__":
    port = int(getenv("PORT", 8000))
    uvicorn.run("main:app",host="0.0.0.0",port=port,reload=True)