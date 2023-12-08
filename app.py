from fastapi import FastAPI
import uvicorn
from mylib.query import Query1, Query2

app = FastAPI()

@app.get("/")
async def root():

    return "Welcome to the grocery database service!"

@app.get("/coffee")
async def get_coffee_info():
    return Query1()

@app.get("/product_count")
async def get_count():
    return Query2

if __name__ == "__main__":
    uvicorn.run(app, port=5000, host="0.0.0.0")