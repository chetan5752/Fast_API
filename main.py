from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app=FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published:bool=True # for default value if we dont not pass value of published
    rating:Optional[int]=None

my_posts=[{"title":"title of post 1","content":"content of post 1","id":1},{"title":"Favorite","content":"I like pizza","id":2}]
 
def find_post(id):
    for p in my_posts:
        if p['id']==id:
            return p
        
def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id']==id:
            return i

@app.get("/",description="This is my first route") #we can fast description in fastapi port
def root():
    return {"Message":"Successfully completed"}

# @app.post("/create")
# def create_post(payload:dict=Body(...)):
#     print(payload)
#     return {"message":"Successfully created"}

@app.get("/posts")
def get_post():
    return {"message":my_posts}

@app.get("/posts/latest")
def get_latest_post():
    post=my_posts[len(my_posts)-1]
    return {"detail":post}

@app.get("/posts/{id}")
def get_post_id(id:int,response:Response):
    post=find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} was not found")
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {"message":f"post with id: {id} not found"}
    return {"Post detail":post}

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_post(post:Post):
    post_dict=post.model_dump() # model_dump is used instead of dict
    post_dict["id"]=randrange(0,1000000)
    my_posts.append(post_dict)
    return {"message":post_dict}

@app.put("/posts/{id}")
def update_post(id:int,post:Post):
    index=find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} not found")
    post_dict=post.model_dump()
    post_dict['id']=id
    my_posts[index]=post_dict
    return {"data":post_dict}

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    index=find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)