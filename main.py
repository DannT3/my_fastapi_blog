from fastapi import FastAPI, Header, status, Response
from fastapi.responses import JSONResponse, HTMLResponse
import time

app = FastAPI()

@app.get('/')
def root():
    time.sleep(5)
    return {"message": "Hello World!"}
    

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", reload=True)

