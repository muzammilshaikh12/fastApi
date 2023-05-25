from fastapi import FastAPI

from typing import Optional

from pydantic import BaseModel

app = FastAPI()

@app.get('/name')
def index():
    return {
        "name":"fastApi"
    }

@app.get('/about')
def index():
    return {
        "about":"Crazy Python Framework"
    }


# path parameters
@app.get('/square/{number}')
def squareFunction(number:int = 10):
    try:
     return {
        "data":f"The Square of number {number} is {number*number}"
    }
    except:
          return {"error":'Oops Something went wrong !!!'}

# query parameters
@app.get('/blogs')
def blogs(limit:int = 10,published:bool = True,sort: Optional[str]=None):
    try:
     if(published):  
        return {"data":f'{limit} published blogs from Db'}
     else:
        return{"data":f'{limit} blogs from db'}
    except:
        return {"error":'Oops Something went wrong !!!'}
    
# post request
class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]

@app.post('/createBlog')
def createBlog(request:Blog):
    try:
        return {"message":f'Your Blog has been successfully created with title {request.title}'}
    except:
        return {"error":'Oops Something went wrong !!!'}