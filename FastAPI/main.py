from fastapi import FastAPI
import uvicorn

from calc import plus 

app = FastAPI()


@app.get("/")
def index():
    return {"data": "blog list"}

@app.get("/blog/unpublished")
def unpublished():
    return {'data': 'unpubulished'}

@app.get('/blog/{id}')
def show():
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

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    item_id = plus(item_id, item_id)
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)