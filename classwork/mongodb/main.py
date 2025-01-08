from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
import uvicorn
import json

DATABASE ='library'
COLLECTION= 'books'
mongo_uri = 'mongodb://localhost:27017'

app = FastAPI()

client = AsyncIOMotorClient(mongo_uri)

db = client[DATABASE]

@app.get('/books', response_class=JSONResponse)
async def getBooks():
  books_collection = db[COLLECTION]

  book_cursor = books_collection.find()
  books = await book_cursor.to_list()
  for book in books:
    book["_id"] = str(book["_id"])
  return books

if __name__ == '__main__':
  uvicorn.run('main:app', port=3001, reload=True)