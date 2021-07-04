from fastapi import FastAPI
import uvicorn

from . import schemas

app = FastAPI()

@app.post('/blog')
def create(request: schemas.Blog):
    return request

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)