from turtle import title
from fastapi import FastAPI

app=FastAPI(
    title="QR Menu Application",
    
)


@app.get("/")
def home():
    return {"Message":"Welcome to QR-Menu"}