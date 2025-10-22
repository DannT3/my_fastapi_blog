from fastapi import FastAPI
from src.api.routers import post_routers

app = FastAPI()

@app.get('/')
def root():
    return {"message": "Hello World!"}

app.include_router(post_routers.router)
    

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", reload=True)

