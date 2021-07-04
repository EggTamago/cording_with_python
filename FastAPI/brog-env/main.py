from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

from typing import Optional

app = FastAPI()


@app.get("/blog")
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # only get 10 pblished blogs
    if published:
        return {"data": f'{limit} published blog from the db'}
    else:
        return {"data": f'{limit} blog from the db'}

@app.get("/blog/unpublished")
def unpublished():
    return {'data': 'unpubulished'}

@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id }

# pathの記述は上から順番に該当するものないか検索される
# 「unpublish」が{id}より後ろにあると{id}で検索かかって失敗する
'''
@app.get("/blog/unpublished")
def unpublished():
    return {'data': 'unpubulished'}
'''

@app.get('/blog/{id}/comments')
def comments(id: int):
    # fetch commetns of blog with id = id
    return {'data': {'10', '20'} }


# BaseModel扱うと引数簡略化できる
class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    return { "data" : f"blog is created with {blog.title}"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)