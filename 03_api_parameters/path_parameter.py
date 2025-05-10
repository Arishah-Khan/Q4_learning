from fastapi import FastAPI , Path
from pydantic import BaseModel


app = FastAPI()

class Book(BaseModel):
    title : str
    author : str
    price : int
    
@app.get("/books/{bookId}")
async def read_book(bookId : int = Path(... , title = "The ID of the book" , ge = 1)):
    return {
        "bookId" : bookId
    }
    
@app.post("/book/{bookId}")
async def create_book(bookId:int = Path(... , title = "The ID Of The Book" , ge = 1) , book : Book = ...):
    return {
        "bookId" : bookId,
        "book" : book
    }