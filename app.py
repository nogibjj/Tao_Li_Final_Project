from fastapi import FastAPI
import uvicorn
from mylib.query import Query1, Query2
from urllib.parse import unquote
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        html = f.read()
    return HTMLResponse(content=html, status_code=200)

@app.get("/grocery_info/{grocery_name}")
async def get_grocery_info(grocery_name: str):
    decoded_grocery_name = unquote(grocery_name)
    return Query1(decoded_grocery_name)

@app.get("/product_count/{count}")
async def get_count(count: int):
    return Query2(count)

if __name__ == "__main__":
    uvicorn.run(app, port=5000, host="0.0.0.0")