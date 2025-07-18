import faiss
import json
import numpy as np
from fastapi import FastAPI,Request
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
app=FastAPI()
templates = Jinja2Templates(directory="app/templates")

app.add_middleware(
     CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

model = SentenceTransformer('all-MiniLM-L6-v2')
index=faiss.read_index("app/model/qa_index.faiss")
with open("app/model/qa_answers.json","r") as f:
    answers=json.load(f)

class QueryRequest(BaseModel):
    query:str

@app.get("/")
def welcome_message():
    return {"message": "Welcome to the Health Chatbot!"}


@app.get("/chat", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "chat": []})

@app.post("/chat")
async def get_answers(request:QueryRequest):
    query=request.query
    query_vector=model.encode([query]).astype("float32")
    D,I=index.search(query_vector,1)
    results=answers[I[0][0]]
    return {"answer": results}