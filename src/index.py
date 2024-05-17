from fastapi import FastAPI

from src.dtos.ISayHelloDto import ISayHelloDto
from src.amz import getSellerJson

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/hello")
async def hello_message(dto: ISayHelloDto):
    return {"message": f"Hello {dto.message}"}


@app.get("/etsy/{keyword}")
async def getEtsySel(keyword: str):

    return {"links": "", "json": ""}


@app.get("/etsy/req/{keyword}")
async def getEtsySel(keyword: str):

    return {"links": "", "json": ""}



@app.get("/amz/seller/{sellerid}")
async def getAmzSellerJson(sellerid: str):
    data=getSellerJson(sellerid)
    return data