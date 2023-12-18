import uvicorn
from fastapi import FastAPI
from api import promt
app = FastAPI(
    docs_url='/api/docs'
)

app.include_router(promt.router, prefix="/api/v1/promt")


@app.get("/")
async def root():
    return {"messege": "Hello world"}

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host='localhost',
        port=8005
    )